import RPi.GPIO as GPIO

from time import sleep

# Define GPIO to LCD mapping

LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18

# Define some device constants

LCD_WIDTH = 16    # Maximum characters per line

LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

# Timing constants

E_PULSE = 0.0005
E_DELAY = 0.0005

def main():

  # Main program block

  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7

  # Initialise display

  lcd_init()

  while True:
        
    # Send some test

    lcd_string("Enter your card ",LCD_LINE_1)
    sleep(3) # 3 second delay

    # Send some text

    lcd_string(“Place your hand”,LCD_LINE_1)
    sleep(3) # 3 second delay
    
 # Send some text

    lcd_string(“Thanks”,LCD_LINE_1)
    sleep(3)
    GPIO.cleanup()
