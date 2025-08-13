
from ultralytics import YOLO
from time import sleep

tick_rate = 1/32
model = YOLO("model.pt")

while 1:
    result = model("screen")
    sleep(tick_rate)
