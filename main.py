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
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Recaptcha.recaptcha import Recaptcha

"""
> reCAPTCHA 이미지를 분석하여 정답 타일을 찾고, 인간처럼 보이는 웹 브라우저 상호작용을 통해 해당 타일을 클릭한다.

- Google reCAPTCHA demo page에 접속
- reCAPTCHA 박스를 클릭하여 이미지 캡챠를 트리거한다.
- 캡챠 이미지를 스크린샷으로 저장하고, 저장된 이미지를 분석하여 정답 타일 클릭한다.
- 만약 캡챠가 여러 단계로 구성되어 있다면, 각 단계를 해결한다.
"""


# Initialize selenium, model, class list
rekt = Recaptcha() 

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
#driver = webdriver.Chrome(r"../chromedriver.exe", options=options) # options
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install())
with open("rc_class.json", 'r', encoding='utf-8') as f:
    rc_class = json.load(f)

# 인간처럼 보이는 마우스 움직임을 시뮬레이션하기 위해, Bezier curve를 사용해 마우스의 움직임 경로 생성
def human_click(start_element=None, end_element=None, target_points=30):
    if start_element is None: # 마우스 움직임의 시작 지점이 주어지지 않은 경우,
        start_element = driver.find_element_by_xpath("/html") 
        start_xy = (randint(30, 60), randint(30, 60))
        action = ActionChains(driver)
        action.move_to_element(start_element)
        action.move_by_offset(start_xy[0], start_xy[1])
        action.perform()
    else:
        start_xy = (start_element.location["x"], start_element.location["y"])
    end_xy = (end_element.location["x"], end_element.location["y"])

    # Bezier Curve 생성 3
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
    rand = uniform(min, max)
    time.sleep(rand)


def main():
    # Open chromedriver selenium
    driver.get("https://www.google.com/recaptcha/api2/demo")
    driver.switch_to.default_content()
    iframes = driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])

    # Click reCaptcha box
    check_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "recaptcha-anchor"))
    )
    human_click(end_element=check_box)

    # Screenshoot image
    sleep_uniform(3, 5)
    driver.switch_to.default_content()
    iframes = driver.find_elements_by_tag_name("iframe")
    driver.switch_to.frame(iframes[2])

    # Check ReCaptcha type
    try:
        instruction = driver.find_element_by_xpath(
            r'//*[@id="rc-imageselect"]/div[2]/div[1]/div[1]/div[2]/span'
        ).text
    except:
        try:
            instruction = driver.find_element_by_class_name(
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
                driver.find_element_by_id(r"recaptcha-verify-button")
            except:
                break
    else:
        correct_tile = solve_captcha()
        click_tiles(correct_tile)
        # Click verify button
        click_next()


def click_next():
    next_button = driver.find_element_by_id(r"recaptcha-verify-button")
    human_click(end_element=next_button)


def solve_captcha():
    global driver
    driver.find_element_by_tag_name("table").screenshot("web_screenshot.png")
    max_column = len(driver.find_elements_by_tag_name("tr"))

    # Inference
    img = Image.open("web_screenshot.png")  # PIL image
    return rekt.inference(img, max_column)


def click_tiles(results):
    global driver
    max_column = len(driver.find_elements_by_tag_name("tr"))

    correct_class = driver.find_element_by_xpath(
        r'//*[@id="rc-imageselect"]/div[2]/div[1]/div[1]/div/strong'
    ).text
    if correct_class in rc_class:
        correct_class = rc_class[correct_class]
    else:
        # raise ValueError("This script didnt support that class yet.")
        print("This script doesn't support that class yet. Skipping...")
        return
              
    # Click tiles
    tiles = driver.find_elements_by_tag_name("td")
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
