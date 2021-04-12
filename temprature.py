import mlx90614
from machine import I2C, Pin

i2c = I2C(scl=Pin(5), sda=Pin(4))
sensor = mlx90614.MLX90614(i2c)

while True:
    def temp():
        temp = sensor.read_ambient_temp()