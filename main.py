from .voice import talk
from .camera import still
from .camera import rec
from .qr import dectector
from .lcd import clean, pt
from .temprature import temp
from .motor import loop
import time
import webbrowser

t = 101

rec()
pt('Enter your card')
if dectector():
    dectector()
    clean()
    pt('place your hand')
    talk('place your hand near thermometer')
    clean()
    pt(temp())

    if temp() >= t:
        still()
        webbrowser.open(dectector())
        pt(temp()+'High')
        talk('Your temperature is high')
        clean()
    else:
        clean()

    loop()
    time.sleep(10)
