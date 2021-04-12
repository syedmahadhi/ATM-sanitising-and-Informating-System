from RPLCD import CharLCD

lcd = CharLCD(cols=16, rows=2, pin_rs=26, pin_e=24, pins_data=[22, 18, 16, 12])


def clean():
    lcd.clear()

def pt(text):
    lcd.write_string(text)