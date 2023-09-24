import math
import torch

# Object Detection
class Recaptcha:
    # 주어진 이미지에서 객체를 탐지하고, 그 결과를 특정한 타일 형식에 맞게 변환하여 반환
    def __init__(self):
        self.model = torch.hub.load("ultralytics/yolov5", "yolov5l", pretrained=True)
        self.names = self.model.names

    def inference(self, img, max_column):
        results = []
        inferesult = self.model(img)
        xy_result = inferesult.xyxy[0] # [x_min, y_min, x_max, y_max, confidence, class]

        for it_result in xy_result:
            class_name = self.names[int(it_result[5])]
            # 95 and 125 are tile size
            if max_column == 3: # 3x3 grid의 경우, 각 grid의 크기는 125x125
                tile_column = math.ceil(float(it_result[0]) / 125.0) # x좌표 (해당 객체가 몇번째 grid에 위치하는지 알수있음.)
                tile_row = math.ceil(float(it_result[1]) / 125.0) # y좌표
            elif max_column == 4: # 4x4 grid의 경우, 각 grid의 크기는 95x95
                tile_column = math.ceil(float(it_result[0]) / 95.0) # x좌표
                tile_row = math.ceil(float(it_result[1]) / 95.0) # y좌표
            results.append(
                {
                    "tile_column": tile_column,
                    "tile_row": tile_row,
                    "confident": float(it_result[4]), 
                    "class": class_name,
                }
            )
        return results
