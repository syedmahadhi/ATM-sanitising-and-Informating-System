from .voice import engine
from .camera import still
from .camera import rec
from .qr import dectector
from .lcd import lcd_string, GPIO, cleanup
from .temprature import sensor
from .motor import loop
import time
import webbrowser


rec()
lcd_string("Enter your card")
engine.say("Enter your card")
engine.runAndWait()
if dectector():
    dectector()
    GPIO.cleanup()
    lcd_string("place your hand")
    engine.say("Place your hand")
    engine.runAndWait()
    GPIO.cleanup()
    lcd_string(temp())
    
    print "Object Temperature :", sensor.get_object_1()
    if sensor.get_object_1() >= 100:
        still()
        webbrowser.open(dectector())
        lcd_string(temp()+"High")
        engine.say("Your temperature is high")
        engine.runAndWait()
        GPIO.cleanup()
    else:
        clean()

    loop()
    time.sleep(10)
