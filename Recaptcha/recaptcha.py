import math
import torch

# Object Detection using YOLO v5 
class Recaptcha:
    """
    이미지에서 객체를 탐지하고, 그 결과를 지정된 타일 형식으로 반환하는 클래스입니다.
    
    속성:
        model: 객체 탐지를 위한 YOLOv5 모델입니다.
        names: 모델이 탐지할 수 있는 클래스의 이름들입니다.
    """

    def __init__(self):
        self.model = torch.hub.load("ultralytics/yolov5", "yolov5l", pretrained=True)
        self.names = self.model.names

    def inference(self, img, max_column):
        """
        이미지에서 추론을 수행하고 결과를 타일 형식으로 반환합니다.
        
        매개변수:
            img: 추론이 수행될 이미지입니다.
            max_column (int): 그리드의 최대 열 수입니다.
            
        반환값:
            results: 탐지된 객체에 대해 타일 열, 타일 행, 신뢰도, 클래스를 포함한 사전의 리스트입니다.
        """
        results = []
        inferesult = self.model(img)
        xy_result = inferesult.xyxy[0] # [x_min, y_min, x_max, y_max, confidence, class]

        # 타일 크기에 대한 상수
        TILE_SIZE_3x3 = 125
        TILE_SIZE_4x4 = 95

        for it_result in xy_result:
            class_name = self.names[int(it_result[5])]

            # 그리드 크기를 결정하고 객체 좌표를 기반으로 타일 열과 행을 계산합니다.
            if max_column == 3:  # 3x3 그리드의 경우, 각 그리드의 크기는 125x125입니다.
                tile_column = math.ceil(float(it_result[0]) / TILE_SIZE_3x3)  # x 좌표
                tile_row = math.ceil(float(it_result[1]) / TILE_SIZE_3x3)  # y 좌표
            elif max_column == 4:  # 4x4 그리드의 경우, 각 그리드의 크기는 95x95입니다.
                tile_column = math.ceil(float(it_result[0]) / TILE_SIZE_4x4)  # x 좌표
                tile_row = math.ceil(float(it_result[1]) / TILE_SIZE_4x4)  # y 좌표

            results.append(
                {
                    "tile_column": tile_column,
                    "tile_row": tile_row,
                    "confident": float(it_result[4]), 
                    "class": class_name,
                }
            )

        return results