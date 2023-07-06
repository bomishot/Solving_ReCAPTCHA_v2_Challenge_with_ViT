# Solving ReCAPTCHA v2 Challenge using Classification-based Approach with Vision Transformer

학부 논문




![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)   ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)  
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

![image](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/ae84d8f1-b0b1-49d8-8238-a68dc74f6b19)


| project name | Solving ReCAPTCHA v2 Challenge using Classfication-based Approach with Vision Transformer | 
| ------------ | -------------- |
| project period | 2023.05.16-2023.06.01 |
| member | 개인 | 
| project keywords | Vision Transformer, classification-based approach about small object detection, Recaptcha Challenge |

<br>
<br>

## Project Process
1. 데이터 가져오기
   * 본 연구에서는 Recaptcha v2 Challenge 해결을 위해 kaggle 사이트에서 11,671개의 이미지를 수집하였습니다. 각 이미지는 12개의 카테고리로 분류되어 있습니다.
2. 이미지 데이터 전처리
   * generator로 훈련, 테스트 이미지 데이터를 생성하였습니다.
4. 작은 이미지 데이터 생성
   * 원본 이미지 데이터 3x3 사이즈로 분할하였습니다. 원본 이미지는 약 만개, 생성된 작은 이미지는 약 육만개입니다.
5. 모델링
   * Vision Transformer모델의 B_32(base 32)구조를 선택했습니다. 상대적으로 작은 모델로, 제한된 컴퓨터 리소스와 계산 효율성을 고려해 선택하였습니다.
   * vit_b32구조를 첫번째 층에 추가하였으며, 그 후 BatchNormalization, Dense층을 이용해 12개의 label 분류 모델을 만들었습니다.
6. train_generator에 모델 훈련시키고, 저장
7. 큰 이미지 데이터 분류 성능
8. 작은 이미지 데이터 분류 성능능
  
<br>
<br>
  
## Abstract

한글 요약 : 이 논문은 Vision Transformer를 활용한 분류 기반의 접근 방식을 통해 Recaptcha 챌린지를 해결하는 것을 다루고 있습니다. 기존의 객체 검출 방식인 YOLO의 문제점을 보완하며, 우수한 성능을 보이는 것을 확인하였습니다. 연구에서는 Vision Transformer의 강인한 특성과 작은 객체 분류에 대한 우수성을 설명하고, 이전에 제안된 접근 방식의 이점과 한계를 분석하였습니다. 실험 결과를 통해 제안된 접근 방식의 성능 향상을 입증하고, 작은 객체 분류에 대한 기존 연구와의 차이를 확인하였습니다. 이를 통해 Vision Transformer를 활용한 분류 기반의 접근 방식이 Recaptcha 챌린지에서의 가치와 기여도를 확인할 수 있었습니다.


핵심어 : Vision Transformer, 분류 기반 접근 방식, 작은 객체 분류, Recaptcha 챌린지




본 연구는 ViT 모델을 활용한 객체 검출에 대한 성능 평가와 ReCAPTCHA 챌린지 해결에 대해 분석하였습니다. ViT모델은 YOLO와 비교하여 객체 검출에서의 일부 단점을 보완하였으며, 분류 기반 접근 방식의 장점을 활용하여 ReCAPTCHA 챌린지 해결에 효과적인 도구로 활용될 수 있음을 확인하였습니다.
  
<br>
<br>
    
## Recaptcha challenge 유형 분류

저는 유형을 두 가지로 분류했습니다. 

* Big image

![image](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/f0be1e64-917d-4969-8178-d0e9c229c376)

해당 방법은 클래스 정보가 포함된 이미지를 모두 선택하여 분류하는 방식입니다.  
해당 이미지에서 '자전거인지(0) 자전거가 아닌지(1)'방식으로 이진 분류에서 자전거를 찾는 경우로 분류를 할 것입니다. 다른 클래스로 예측된 경우는 자전거가 아니게 분류됩니다.

* Small image

![image](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/149df818-27a8-47f1-914a-e8bc6eff4ba5)

해당 방법은 사진 한 장을 분할하여 특정한 객체를 찾는 것입니다. 즉, '횡단보도'가 포함된 큰 사진 한 장을 가지고 '횡단보도'만 포함된 타일을 선택하는 것입니다.  
이에 대한 분류는 big image를 통해 훈련된 모델을 가지고 수행할 것입니다. (?)


<br>
<br>
  
## 각 class별 성능
* Big Images

| Class          | Accuracy | F1-score about each class | F1-score about except class | count |
|----------------|----------|------------------|------------------|---------|
| Bicycle        |   0.99   |      1.00        |      0.99        | 580 |
| Bridge         |   0.97   |      0.98        |      0.96        | 568 |
| Bus            |   0.99   |      0.99        |      0.99        | 574 |
| Car            |   0.95   |      0.96        |      0.93        | 567 |
| Chimney        |   0.97   |      0.98        |      0.95        |569|
| Crosswalk      |   0.95   |      0.97        |      0.93        |571|
| Hydrant        |   1.00   |      1.00        |      1.00        |568|
| Motorcycle     |   0.98   |      0.99        |      0.96        | 375|
| Palm           |   0.99   |      0.99        |      0.98        | 571|
| Stair          |   0.96   |      0.97        |      0.94        | 573|
| Traffic Light  |   0.94   |      0.95        |      0.90        | 576|
| Total          |   0.97   |      0.98        |      0.95        | 6092 |

Big image에서 잘못 분류된 케이스입니다. 

![image](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/9529eac0-70cb-4886-a813-806ce453f2f1)

잘못 분류된 이미지들을 보면, 거의 두 물체가 같이있어 두 물체 중 하나로 다른 class를 예측한 것입니다.
이렇게 잘못 분류되는 이미지들을 통해 모델이 작은 객체까지 잘 인지하고 있어, 작은 이미지 분류에서의 작은 객체 검출 측면에서 긍정적인 효과를 보일 것입니다.

<br>


* Small Images

| Class          | Accuracy | F1-score about about class | F1-score except class | count |
|----------------|----------|------------------|------------------|--|
| Bicycle        |   0.92   |      0.95        |      0.78        |899|
| Bridge         |   0.80   |      0.86        |      0.67        |899|
| Bus            |   0.80   |      0.87        |      0.54        |899|
| Car            |   0.90   |      0.93        |      0.81        |899|
| Chimney        |   0.92   |      0.95        |      0.72        |647|
| Crosswalk      |   0.81   |      0.87        |      0.67        |900|
| Hydrant        |   0.92   |      0.94        |      0.88        |899|
| Motorcycle     |   0.87   |      0.92        |      0.58        |728|
| Palm           |   0.88   |      0.91        |      0.81        |900|
| Stair          |   0.78   |      0.87        |      0.29        |899|
| Traffic Light  |   0.92   |      0.95        |      0.81        |899|
| Total          |   0.87   |      0.91        |      0.68        |9468|



대부분의 클래스는 예측을 어느정도 해내었지만, 일부 클래스(stair, bus)에 대해서는 작은 이미지 분류가 어려웠습니다.


본 실험에서 큰 이미지 분류는 평균적으로 97%의 성공률, 작은 이미지 분류는 평균적으로 87%의 성공률로, 총 평균적으로 92%의 성공률으로 ViT모델로 분류 기법을 사용했을 때 성능이 더 향상됨을 보였습니다.



<br>
<br>


## References
[1] Image Recognition for Solving Google’s reCAPTCHA An Investigation of how Different Aspects Affects the Security of Google’s reCAPTCHA  (Stockholm, Sweden 2022) [논문]

[2] Object Detection based Solver for Google's Image reCAPTCHA v2 (2021.4) [논문]

[3] Kaggle Dataset : https://www.kaggle.com/datasets/mikhailma/test-dataset [데이터셋]

[4] AN IMAGE IS WORTH 16X16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE (ICLR, 2021) [논문]



