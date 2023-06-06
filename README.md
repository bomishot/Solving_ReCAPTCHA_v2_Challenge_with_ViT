# Solving ReCAPTCHA v2 Challenge using Classification-based Approach with Vision Transformer

졸업 논문




![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)   ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)   ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)  
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)

![image](https://github.com/bomishot/Solving_ReCAPTCHA_v2_Challenge_with_ViT/assets/97582403/ae84d8f1-b0b1-49d8-8238-a68dc74f6b19)



한글 요약 : 이 논문은 Vision Transformer를 활용한 분류 기반의 접근 방식을 통해 Recaptcha 챌린지를 해결하는 것을 다루고 있습니다. 기존의 객체 검출 방식인 YOLO의 문제점을 보완하며, 우수한 성능을 보이는 것을 확인하였습니다. 연구에서는 Vision Transformer의 강인한 특성과 작은 객체 분류에 대한 우수성을 설명하고, 이전에 제안된 접근 방식의 이점과 한계를 분석하였습니다. 실험 결과를 통해 제안된 접근 방식의 성능 향상을 입증하고, 작은 객체 분류에 대한 기존 연구와의 차이를 확인하였습니다. 이를 통해 Vision Transformer를 활용한 분류 기반의 접근 방식이 Recaptcha 챌린지에서의 가치와 기여도를 확인할 수 있었습니다.


핵심어 : Vision Transformer, 분류 기반 접근 방식, 작은 객체 분류, Recaptcha 챌린지




본 연구는 ViT 모델을 활용한 객체 검출에 대한 성능 평가와 ReCAPTCHA 챌린지 해결에 대해 분석하였습니다. ViT모델은 YOLO와 비교하여 객체 검출에서의 일부 단점을 보완하였으며, 분류 기반 접근 방식의 장점을 활용하여 ReCAPTCHA 챌린지 해결에 효과적인 도구로 활용될 수 있음을 확인하였습니다.



각 class별 성능
* Big Images
| Class          | Accuracy | F1-score about each class | F1-score about except class | count |
|----------------|----------|------------------|------------------|---------|
| Bicycle        |   0.99   |      1.00        |      0.99        | 607 |
| Bridge         |   0.96   |      0.97        |      0.94        | 574 |
| Bus            |   0.99   |      0.99        |      0.98        | 5700 |
| Car            |   0.95   |      0.96        |      0.93        | 5627
| Chimney        |   0.97   |      0.98        |      0.95        |5635|
| Crosswalk      |   0.95   |      0.96        |      0.92        |5696|
| Hydrant        |   1.00   |      1.00        |      1.00        |5693|
| Motorcycle     |   0.87   |      0.92        |      0.58        |
| Palm           |   0.88   |      0.91        |      0.81        |
| Stair          |   0.78   |      0.87        |      0.29        |
| Traffic Light  |   0.92   |      0.95        |      0.81        |
| Total          |   0.87   |      0.91        |      0.68        |





* Small Images

| Class          | Accuracy | F1-score about about class | F1-score except class |
|----------------|----------|------------------|------------------|
| Bicycle        |   0.92   |      0.95        |      0.78        |
| Bridge         |   0.80   |      0.86        |      0.67        |
| Bus            |   0.80   |      0.87        |      0.54        |
| Car            |   0.90   |      0.93        |      0.81        |
| Chimney        |   0.92   |      0.95        |      0.72        |
| Crosswalk      |   0.81   |      0.87        |      0.67        |
| Hydrant        |   0.92   |      0.94        |      0.88        |
| Motorcycle     |   0.87   |      0.92        |      0.58        |
| Palm           |   0.88   |      0.91        |      0.81        |
| Stair          |   0.78   |      0.87        |      0.29        |
| Traffic Light  |   0.92   |      0.95        |      0.81        |
| Total          |   0.87   |      0.91        |      0.68        |










