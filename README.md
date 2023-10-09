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
| project period | 2023.05.16-2023.06.01 / 2023.9.18-2023.10.9 (약 1달 반) |
| member | 개인 | 
| project keywords | Vision Transformer, classification-based approach about small object detection, Recaptcha Challenge |

<br>
<br>

![제목 없는 동영상 - Clipchamp로 제작 (1)](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/9ff56b53-7ce7-4230-bab6-fe37d9e9e372)


# Abstract
본 논문은 Vision Transformer(ViT)를 중심으로 한 분류 기반 접근 방식을 통해 Recaptcha 챌린지를 탐구합니다. YOLO를 활용한 기존 객체 탐지 기법의 한계를 극복하면서 뛰어난 성능 향상을 확인하였습니다. 연구 과정에서 ViT의 견고한 특성과 소형 객체 분류에서의 능력에 주목하였고, 이전 방법론들의 강점과 약점을 철저히 분석하였습니다. 실험 결과를 통해 본 연구의 방법론이 성능 향상을 도출하였으며, 소형 객체 분류와 관련된 기존 연구와의 명확한 차별성을 확인하였습니다. 이러한 결과는 ViT기반의 분류 전략이 Recaptcha 챌린지에 중요한 가치와 기여를 제공함을 보여줍니다.


핵심어 : Vision Transformer, 분류 기반 접근 방식, 소형 객체 분류, Recaptcha 챌린지




## 결론
1.	성능 : Vision Transformer는 YOLO에 비해 전반적으로 더 높은 성능을 보였습니다. 특히, 타겟 클래스의 F1-score에서 큰 차이를 보였습니다. 이는 Vision Transformer가 이미지의 디테일한 정보를 더 잘 캡쳐하고, 분류 성능이 뛰어나다는 것을 나타냅니다.
	
2.	YOLO의 특성 : 이전 논문에서 사용하였던, YOLO는 원래 실시간 객체 탐지를 목적으로 설계되었습니다. 즉, 여러 객체의 위치와 그 객체의 클래스를 동시에 예측하는 것에 최적화되어 있습니다. 반면, reCAPTCHA v2의 문제 설정에서는 단순히 특정 클래스의 객체가 이미지에 포함되어 있는지만 판단하면 됩니다. 이러한 task는 YOLO의 전체 기능이 필요하지 않을 수 있을 것으로 보입니다.

3.	ViT의 특성 : ViT는 이미지를 여러 패치로 나누고 각 패치의 정보를 사용하여 이미지를 분류합니다. 이러한 방식은 전체 이미지에 걸쳐 발생하는 패턴과 관계를 더 잘 학습할 수 있기 때문에, reCAPTCHA v2와 같은 문제에서 효과적일 수 있습니다.

4.	효율성 : ViT는 대규모 데이터에서 훈련되었을 때 특히 더 높은 성능을 발휘합니다. 짧은 훈련시간을 거쳐 만들어진 저의 ViT 모델로도 비교적 높은 정확도와 f1-score을 보였습니다. 이는 ViT가 복잡하고 다양한 배경 속에서도 객체를 잘 분류할 수 있음을 나타냅니다.

5.	적용성 : reCAPTCHA v2와 같은 문제에는 단순한 이진 분류 방식이 더 적합할 수 있습니다. 여러 객체를 동시에 탐지하고 위치를 지정할 필요가 없기 때문입니다. 이러한 관점에서, ViT가 YOLO보다 더 적합한 선택이라고 볼 수 있습니다.


최종적으로, reCAPTCHA v2를 이진 분류 문제로보고, Vision Transformer를 사용하는 것이 더 적절한 선택과 성능을 보일 것으로 판단됩니다. 

본 연구는 ViT 모델을 활용한 객체 검출에 대한 성능 평가와 ReCAPTCHA 챌린지 해결에 대해 분석하였습니다. ViT모델은 YOLO와 비교하여 객체 검출에서의 일부 단점을 보완하였으며, 분류 기반 접근 방식의 장점을 활용하여 ReCAPTCHA 챌린지 해결에 효과적인 도구로 활용될 수 있음을 확인하였습니다.


  

""" 이후 수정..
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



