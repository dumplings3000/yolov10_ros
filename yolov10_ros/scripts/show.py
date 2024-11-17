#!/usr/bin/env python3
import torch

# 加载模型
model_path = '/home/user/segmentation/src/yolov10_ros/yolov10_ros/weights/yolov8s.pt'
model = torch.load(model_path)

# 打印模型结构
model_structure = str(model)
print("Model structure:\n\n", model_structure)