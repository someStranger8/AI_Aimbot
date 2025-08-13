
from ultralytics import YOLO

# Load a pretrained model
model = YOLO("yolo11n.pt")

results = model.train(data="data.yaml", epochs=100, imgsz=540)
