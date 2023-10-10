# Solving ReCAPTCHA v2 Challenge using Classification-based Approach with Vision Transformer
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)  
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

![image](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/ae84d8f1-b0b1-49d8-8238-a68dc74f6b19)

<br>
<br> 

| project name | Solving ReCAPTCHA v2 Challenge using Classfication-based Approach with Vision Transformer | 
| ------------ | -------------- |
| project period | 2023.05.16-2023.06.01 / 2023.9.18-2023.10.9 (약 1달 반) |
| member | 개인 | 
| project keywords | Vision Transformer, classification-based approach about small object detection, Recaptcha Challenge |


[doc](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/blob/main/%EC%A1%B8%EC%97%85%EB%85%BC%EB%AC%B8.docx)
, [tistory](https://bomishot.tistory.com/38) -> 본 논문에 대한 구체적인 내용이 확인 가능합니다.
<br>
<br>

<img src="https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/f880ce14-ff5b-4a06-92b5-cc94c18ad6be" width="800" height="400"/>

<br>
<br> 

# Abstract
본 논문은 Vision Transformer(ViT)를 중심으로 한 분류 기반 접근 방식을 통해 Recaptcha 챌린지를 탐구합니다. YOLO를 활용한 기존 객체 탐지 기법의 한계를 극복하면서 뛰어난 성능 향상을 확인하였습니다. 연구 과정에서 ViT의 견고한 특성과 소형 객체 분류에서의 능력에 주목하였고, 이전 방법론들의 강점과 약점을 철저히 분석하였습니다. 실험 결과를 통해 본 연구의 방법론이 성능 향상을 도출하였으며, 소형 객체 분류와 관련된 기존 연구와의 명확한 차별성을 확인하였습니다. 이러한 결과는 ViT기반의 분류 전략이 Recaptcha 챌린지에 중요한 가치와 기여를 제공함을 보여줍니다.
<br>
<br> 
핵심어 : Vision Transformer, 분류 기반 접근 방식, 소형 객체 분류, Recaptcha 챌린지

<br>
<br> 

## 목차

1. 서론  
   1.1 연구 배경  
   1.2 연구 주제 설명  
   1.3 기존 연구와 비교  
   1.4 Recaptcha challenge 유형 분류  
2. 연구 방법 및 결과  
   2.1 데이터  
   2.2 Base model : Transfer learning based on Inception v3  
   2.3 모델 선정 : Vision Transformer  
   2.4 모델 훈련  
   2.5 [Vision Transformer 테스트 결과](##테스트_방법의_차별성)
	2.5.1 큰 이미지 분류 성능   
   	2.5.2 작은 이미지 분류 성능 및 라벨링  
   2.6 YOLO 테스트 결과  
3. 결과 분석    
   3.1 [Vision Transformer과 YOLO 모델 성능 비교](##Classification_Report)  
   3.2 [YOLO의 문제점 및 해결 방안](##기존_방법_YOLO의_문제점_해결_예시)
   3.3 실제 Recaptcha 시스템에 적용하여 테스트 (YOLO)    
4. 결론 및 향후 연구 방향    
   4.1 [결론](##결론)  
   4.2 한계점 및 향후 연구 방향  



<br>
<br> 

## 결론
1.	성능 : Vision Transformer는 YOLO에 비해 전반적으로 더 높은 성능을 보였습니다. 특히, 타겟 클래스의 F1-score에서 큰 차이를 보였습니다. 이는 Vision Transformer가 이미지의 디테일한 정보를 더 잘 캡쳐하고, 분류 성능이 뛰어나다는 것을 나타냅니다.
	
2.	YOLO의 특성 : 이전 논문에서 사용하였던, YOLO는 원래 실시간 객체 탐지를 목적으로 설계되었습니다. 즉, 여러 객체의 위치와 그 객체의 클래스를 동시에 예측하는 것에 최적화되어 있습니다. 반면, reCAPTCHA v2의 문제 설정에서는 단순히 특정 클래스의 객체가 이미지에 포함되어 있는지만 판단하면 됩니다. 이러한 task는 YOLO의 전체 기능이 필요하지 않을 수 있을 것으로 보입니다.

3.	ViT의 특성 : ViT는 이미지를 여러 패치로 나누고 각 패치의 정보를 사용하여 이미지를 분류합니다. 이러한 방식은 전체 이미지에 걸쳐 발생하는 패턴과 관계를 더 잘 학습할 수 있기 때문에, reCAPTCHA v2와 같은 문제에서 효과적일 수 있습니다.

4.	효율성 : ViT는 대규모 데이터에서 훈련되었을 때 특히 더 높은 성능을 발휘합니다. 짧은 훈련시간을 거쳐 만들어진 저의 ViT 모델로도 비교적 높은 정확도와 f1-score을 보였습니다. 이는 ViT가 복잡하고 다양한 배경 속에서도 객체를 잘 분류할 수 있음을 나타냅니다.

5.	적용성 : reCAPTCHA v2와 같은 문제에는 단순한 이진 분류 방식이 더 적합할 수 있습니다. 여러 객체를 동시에 탐지하고 위치를 지정할 필요가 없기 때문입니다. 이러한 관점에서, ViT가 YOLO보다 더 적합한 선택이라고 볼 수 있습니다.


최종적으로, reCAPTCHA v2를 이진 분류 문제로보고, Vision Transformer를 사용하는 것이 더 적절한 선택과 성능을 보일 것으로 판단됩니다. 

본 연구는 ViT 모델을 활용한 객체 검출에 대한 성능 평가와 ReCAPTCHA 챌린지 해결에 대해 분석하였습니다. ViT모델은 YOLO와 비교하여 객체 검출에서의 일부 단점을 보완하였으며, 분류 기반 접근 방식의 장점을 활용하여 ReCAPTCHA 챌린지 해결에 효과적인 도구로 활용될 수 있음을 확인하였습니다.



<br>
<br>

## 테스트_방법의_차별성
Recaptcha는 사용자에게 특정 class의 이미지를 선택하도록 요청하는데, 이 때의 상황을 고려하여 recaptcha v2와 같은 시나리오에서의 성능 검증에 초점을 맞추어 test를 진행하였습니다. 특정 클래스의 이미지에 대해, 이진 분류를 통해 모델의 분류 성능을 평가하여, 특정 클래스에 대한 모델의 민감도나 특정 클래스를 잘 걸러내는 능력을 보일 수 있습니다.

구체적인 방법으로는, 
1.	Test input dataset인 생성기 만들기
	A.	각각의 class에 대해 2개의 생성기를 만듭니다. 첫번째 생성기는 해당 클래스의 이미지만 포함합니다. 두번재 생성기는 해당 클래스를 제외한 나머지 모든 클래스의 이미지를 random하게 포함합니다. 
2.	Test 함수 짜기
	A.	예측값과 실제값을 통해 이진 분류로 해석합니다.


이렇게 이진 분류로 test하는 것은 매우 합리적으로 볼 수 있습니다. 
1.	단순성 : 특정 이미지가 주어진 class에 속하는지 아닌지만 판별하면 되므로 복잡한 다중 클래스 분류보다 단순합니다.
2.	높은 정확도 : 이미지가 명확한 class에 속하지 않는 경우에는 이진 분류가 더욱 유리할 수 있습니다.
3.	효율성 : 각 이미지에 대한 분류 결정은 독립적으로 이루어져야하므로, 이진 분류 모델은 다중 클래스 분류 모델보다 계산적으로 더 효율적입니다.
4.	확장성 : 새로운 class를 도입할 때마다 새로운 이진 분류기를 학습시키기만 하면되므로 확장성을 고려했을 때 효율적입니다.

<br>
<br> 

## 기존_방법_YOLO의_문제점_해결_예시
### EX1) Hydrant
![image](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/686ff345-0606-4671-a809-142d60f1bec4)
원본 Hydrant이미지입니다. reCAPTCHA에서의 상황은 “소화전이 포함된 타일을 모두 선택하세요” 입니다.

- YOLO로 돌릴 시,
	- ![image](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/85204dde-34a7-4eed-b319-21f1d777afcd)

- ViT로 돌릴 시,
	- ![image](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/4c9669f9-bdfd-4847-8604-098a95b96036)

YOLO에서의 (0,1)을 bounding box에 의해 초과타일로 포함하여 클래스를 hydrant를 예측하게 됩니다. 하지만 ViT로 돌릴 시, (0,1)을 보면 이의 문제점을 해결해주는 것을 보일 수 있었습니다. 이는 이전 논문의 객체 탐지 문제점인 객체 타일 오버 탐지 부분에서 해결되었음을 보입니다.


### EX2) Car
- ViT로 돌릴 시,
	- ![image](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/068c2bc2-0316-4f16-ad06-9cab26a9da05)
- YOLO로 돌릴 시,
	- ![image](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/69764f2d-fed2-4904-9a21-30a86b5540bb)

YOLO의 3x3크기 이미지에서 (1,2)와, 4x4 크기 이미지에서 (0,2)(1,2)는 초과타일로 볼 수 있습니다. Vision Transformer는 이 초과타일을 not car로 잘 인지해내는 것을 보일 수 있었습니다.

<br>
<br> 

  
## Classification Report
### Vision Transformer
-  Big Images Test
| Class         | Accuracy | F1-score (해당 class) | F1-score (해당 class 제외한 모든 class) | 개수 |
|---------------|----------|-----------------------|---------------------------------------|------|
| Bicycle       | 0.99     | 0.98                  | 0.99                                  | 600  |
| Bridge        | 0.97     | 0.96                  | 0.98                                  | 600  |
| Bus           | 0.98     | 0.97                  | 0.99                                  | 600  |
| Car           | 0.95     | 0.93                  | 0.96                                  | 600  |
| Chimney       | 0.97     | 0.96                  | 0.98                                  | 600  |
| Crosswalk     | 0.95     | 0.92                  | 0.97                                  | 600  |
| Hydrant       | 1.00     | 1.00                  | 1.00                                  | 600  |
| Motorcycle    | 0.99     | 0.98                  | 0.99                                  | 241  |
| Palm          | 0.97     | 0.95                  | 0.98                                  | 600  |
| Stair         | 0.97     | 0.96                  | 0.98                                  | 600  |
| Traffic Light | 0.95     | 0.93                  | 0.97                                  | 600  |
| **Total**     | **0.97** | **0.96**              | **0.95**                              | **6051**  |



Big image에서 잘못 분류된 케이스입니다. 

![image](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/9529eac0-70cb-4886-a813-806ce453f2f1)

잘못 분류된 이미지들을 보면, 거의 두 물체가 같이있어 두 물체 중 하나로 다른 class를 예측한 것입니다.
이렇게 잘못 분류되는 이미지들을 통해 모델이 작은 객체까지 잘 인지하고 있어, 작은 이미지 분류에서의 작은 객체 검출 측면에서 긍정적인 효과를 보일 것입니다.

<br>
- Small images Test

| Class         | Accuracy | F1-score (해당 class가 아닌 small image) | F1-score (해당 class small image) |
|---------------|----------|----------------------------------------|-----------------------------------|
| Bicycle       | 0.92     | 0.95                                   | 0.78                              |
| Bridge        | 0.80     | 0.86                                   | 0.67                              |
| Bus           | 0.80     | 0.87                                   | 0.54                              |
| Car           | 0.90     | 0.93                                   | 0.81                              |
| Chimney       | 0.92     | 0.95                                   | 0.72                              |
| Crosswalk     | 0.81     | 0.87                                   | 0.67                              |
| Hydrant       | 0.92     | 0.94                                   | 0.88                              |
| Motorcycle    | 0.87     | 0.92                                   | 0.58                              |
| Palm          | 0.88     | 0.91                                   | 0.81                              |
| Stair         | 0.78     | 0.87                                   | 0.29                              |
| Traffic Light | 0.92     | 0.95                                   | 0.81                              |
| **Total**     | **0.87** | **0.91**                               | **0.68**                          |



대부분의 클래스는 예측을 어느정도 해내었지만, 일부 클래스(stair, bus)에 대해서는 작은 이미지 분류가 어려웠습니다.


본 실험에서 큰 이미지 분류는 평균적으로 97%의 성공률, 작은 이미지 분류는 평균적으로 87%의 성공률로, 총 평균적으로 92%의 성공률으로 ViT모델로 분류 기법을 사용했을 때 성능이 더 향상됨을 보였습니다.



### YOLO
-  Big images Test
| Class         | Accuracy | F1-score (Target class) | F1-score (Non-target class) | Count |
|---------------|----------|-------------------------|-----------------------------|-------|
| Bicycle       | 0.78     | 0.51                    | 0.86                        | 600   |
| Bus           | 0.76     | 0.44                    | 0.85                        | 600   |
| Car           | 0.76     | 0.51                    | 0.84                        | 600   |
| Hydrant       | 0.92     | 0.86                    | 0.94                        | 600   |
| Motorcycle    | 0.88     | 0.42                    | 0.93                        | 241   |
| Traffic Light | 0.81     | 0.66                    | 0.87                        | 600   |
| **Average Total** | **0.81** | **0.56**              | **0.88**                    | **6051** |





<br>
<br>
## References
[1] Image Recognition for Solving Google’s reCAPTCHA An Investigation of how Different Aspects Affects the Security of Google’s reCAPTCHA  (Stockholm, Sweden 2022) [논문]

[2] Object Detection based Solver for Google's Image reCAPTCHA v2 (2021.4) [논문]

[3] Kaggle Dataset : https://www.kaggle.com/datasets/mikhailma/test-dataset [데이터셋]

[4] AN IMAGE IS WORTH 16X16 WORDS: TRANSFORMERS FOR IMAGE RECOGNITION AT SCALE (ICLR, 2021) [논문]



