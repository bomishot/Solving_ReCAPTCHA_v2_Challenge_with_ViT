import json
import math
import time
from random import randint, uniform

import numpy as np
import scipy.interpolate as si
from PIL import Image
from pyclick import HumanCurve 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Recaptcha.recaptcha import Recaptcha


"""
reCAPTCHA 이미지를 분석하여 정답 타일을 찾고, 
웹 브라우저 상호작용을 통해 해당 타일을 인간처럼 클릭합니다.
"""

# Initialize selenium, model, class list
rekt = Recaptcha() 

# ChromeDriver옵션 설정 및 서비스 초기화
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
service = webdriver.ChromeService(executable_path = r'C:\Users\USER\bomishot\chromedriver-win32\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# class 정보 불러오기
with open("rc_class.json", 'r', encoding='utf-8') as f:
    rc_class = json.load(f)


def human_click(start_element=None, end_element=None, target_points=30):
    """
    인간처럼 보이는 클릭을 시뮬레이션하는 함수
    
    인자:
    - start_element: 클릭의 시작 원소 (None일 경우, 랜덤 위치에서 시작)
    - end_element: 클릭의 종료 원소 (필수)
    - target_points: Bezier curve의 타겟 포인트 수
    
    작동 원리:
    1. 시작 원소의 위치를 계산합니다.
    2. 끝 원소의 위치를 계산합니다.
    3. 시작점과 끝점 사이의 Bezier curve를 계산합니다.
    4. curve를 따라 마우스를 이동시키고, 끝 원소를 클릭합니다.
    """
    if start_element is None: # 마우스 움직임의 시작 지점이 주어지지 않은 경우,
        start_element = driver.find_element(By.XPATH, "/html") 
        start_xy = (randint(30, 60), randint(30, 60))
        action = ActionChains(driver)
        action.move_to_element(start_element)
        action.move_by_offset(start_xy[0], start_xy[1])
        action.perform()
    else:
        start_xy = (start_element.location["x"], start_element.location["y"])
    end_xy = (end_element.location["x"], end_element.location["y"])

    # Bezier Curve 생성 
    curve_point = HumanCurve(
        start_xy, end_xy, upBoundary=0, downBoundary=0, targetPoints=target_points
    ).points

    current_x = start_xy[0]
    current_y = start_xy[1]
    for curve in curve_point:
        action = ActionChains(driver)
        curve_x = curve[0]
        curve_y = curve[1]
        action.move_by_offset(curve_x - current_x, curve_y - current_y)
        current_x += curve_x - current_x
        current_y += curve_y - current_y
        try:
            action.perform()
        except:  # Handle out-of-bound move
            pass
    end_element.click()


# Randomly sleep
def sleep_uniform(min, max):
    """
    일정한 범위의 시간 동안 프로세스를 일시 중지하는 함수.
    
    인자:
    - min: 최소 대기 시간 (초)
    - max: 최대 대기 시간 (초)
    
    작동 원리:
    min과 max 사이에서 무작위로 선택된 시간 동안 스레드를 일시 중지합니다.
    """
    rand = uniform(min, max)
    time.sleep(rand)


def main():
    """
    reCAPTCHA 문제를 해결하는 주요 함수.
    
    작동 원리:
    1. 웹 드라이버를 열고 Google reCAPTCHA 데모 페이지에 접속합니다.
    2. reCAPTCHA 문제 유형을 확인하고 적절한 방식으로 문제를 해결합니다.
    3. 모든 reCAPTCHA 문제가 해결되면 프로세스를 종료합니다.
    """
    driver.get("https://www.google.com/recaptcha/api2/demo")
    driver.switch_to.default_content()
    frames = driver.find_elements(By.TAG_NAME, "iframe")
    if len(frames) > 0:
        driver.switch_to.frame(frames[0])
    else:
        print("No iframe found")

    # Click reCaptcha box
    check_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
    )
    human_click(end_element=check_box)

    # Screenshoot image
    sleep_uniform(3, 5)
    driver.switch_to.default_content()
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframes[2])

    # Check ReCaptcha type
    try:
        instruction = driver.find_element(By.XPATH,
            r'//*[@id="rc-imageselect"]/div[2]/div[1]/div[1]/div[2]/span'
        ).text
    except:
        try:
            instruction = driver.find_element(By.CLASS_NAME,
                r"rc-imageselect-carousel-instructions"
            ).text
        except:
            # 1x verify type
            instruction = None

    if instruction is not None:
        while True:
            correct_tile = solve_captcha()
            click_tiles(correct_tile)

            if (
                instruction != "Click verify once there are none left"
                or len(correct_tile) == 0
            ):
                click_next()

            # Sleep to wait next captcha
            sleep_uniform(3, 5)

            # Check if captcha is solved
            try:
                driver.find_element(By.ID, r"recaptcha-verify-button")
                print('ALL SUCCESS')
            except:
                print('FAIL - not verify-button')
                break
    else:
        correct_tile = solve_captcha()
        click_tiles(correct_tile)
        # Click verify button
        click_next()


def click_next():
    """
    reCAPTCHA의 '다음' 버튼을 클릭하는 함수.
    
    작동 원리:
    "recaptcha-verify-button" 요소를 찾고, human_click 함수를 사용하여 클릭을 시뮬레이션합니다.
    """
    next_button = driver.find_element(By.ID, r"recaptcha-verify-button")
    human_click(end_element=next_button)


def solve_captcha():
    """
    reCAPTCHA 문제를 해결하고, 정답 타일의 인덱스를 반환하는 함수.
    
    작동 원리:
    1. 현재 웹 페이지의 캡챠 이미지를 스크린샷으로 저장합니다.
    2. 저장된 이미지를 모델에 전달하여 인터프리터를 실행합니다.
    3. 반환된 결과를 반환합니다.
    """
    global driver
    driver.find_element(By.TAG_NAME, "table").screenshot("web_screenshot.png")
    max_column = len(driver.find_elements(By.TAG_NAME, "tr"))

    # Inference
    img = Image.open("web_screenshot.png")  # PIL image
    return rekt.inference(img, max_column)


def click_tiles(results):
    """
    주어진 결과를 기반으로 타일을 클릭하는 함수.
    
    인자:
    - results: 모델에서 반환된 결과 (타일의 위치와 클래스 정보 포함)
    
    작동 원리:
    1. 정답 클래스를 결정합니다.
    2. results를 순회하면서 각 타일의 위치와 클래스를 검사합니다.
    3. 일치하는 타일을 human_click 함수를 사용하여 클릭합니다.
    """
    global driver
    max_column = len(driver.find_elements(By.TAG_NAME, "tr"))

    correct_class = driver.find_element(By.XPATH, 
        r'//*[@id="rc-imageselect"]/div[2]/div[1]/div[1]/div/strong'
    ).text
    print('correct class', correct_class)
    print('rc_class', rc_class)
    if correct_class in rc_class:
        correct_class = rc_class[correct_class]
    else:
        raise ValueError("This script didnt support that class yet.")
              
    # Click tiles
    tiles = driver.find_elements(By.TAG_NAME, "td")
    tile_column = 0
    tile_row = 1
    old_tile = None
    # TODO : beautify this shit
    for i, tile in enumerate(tiles, 1):
        tile_column += 1
        for result in results:
            if (
                tile_column == result["tile_column"]
                and tile_row == result["tile_row"]
                and result["class"] == correct_class
            ):
                human_click(start_element=old_tile, end_element=tile, target_points=3)
                old_tile = tile
                break
        if i % max_column == 0:
            tile_row += 1
            tile_column = 0


if __name__ == "__main__":
    main()
