
from ultralytics import YOLO
from time import sleep
from pynput import mouse
import pyautogui

tick_rate = 16
center = (1920/2, 1080/2)

def shoot(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        model = YOLO("model.pt")
        r = model("screen")
        for box in r.boxes:
            names = [result.names[cls.item()] for cls in result.boxes.cls.int()]
            if "ct_head" in names:
                xywh = r.boxes.xywh[names.index("ct_head")]
                pyautogui.move(xywh[0]-center[0],xywh[1]-center[1])
                pyautogui.click()
            elif "ct" in names:
                xywh = r.boxes.xywh[names.index("ct")]
                pyautogui.move(xywh[0]-center[0],xywh[1]-center[1])
                pyautogui.click()

        del model

while 1:
    with mouse.Listener(on_click=shoot) as listener:
        listener.join()
    sleep(tick_rate)
    
