import board
import touchio
import time
import neopixel
import digitalio
import displayio
import adafruit_framebuf
import adafruit_displayio_sh1106
import busio
from board import SCL, SDA

## Touchpad setup

touch_pad = board.A0  
touch = touchio.TouchIn(touch_pad)
touched = 0

## Screen Setup

displayio.release_displays()
WIDTH = 130 # Change these to the right size for your display!
HEIGHT = 64
BORDER = 1
i2c = busio.I2C(SCL, SDA) # Create the I2C interface.
display_bus = displayio.I2CDisplay(i2c, device_address=0x3c)
display = adafruit_displayio_sh1106.SH1106(display_bus, width=WIDTH, height=HEIGHT) # Create the SH1106 OLED class.

## Neopixel Setup

pixel_pin = board.IO12    # Specify the pin that the neopixel is connected to (GPIO 12)
num_pixels = 1; delay = .1   # Set number of neopixels & delay between color changes in seconds
pixel = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)   # Create neopixel and set brightness to 20%

## Onboard LED Setup

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    if touch.value:
        led.value = True
        pixel[0] = ([50,0,0])
        touched = touched + 1
        print(" Times touched: {}".format(touched))
        time.sleep(1)
    else: 
        led.value = False
        pixel[0] = ([0,50,0])
    time.sleep(0.5)
