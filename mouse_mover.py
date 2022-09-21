import board
import keypad
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import usb_hid
from adafruit_hid.mouse import Mouse
m = Mouse(usb_hid.devices)

## Mouse Setup for moving

sensitivity = 40
x_value = [0,0,-sensitivity, sensitivity]
y_value = [sensitivity,-sensitivity,0,0]


## Keypad Button Setup

button_pins = (board.D3, board.D6, board.D7, board.D5, board.BUTTON)
button_labels = ["Down", "Up", "Left", "Right", "Shift"]
buttons = keypad.Keys(button_pins, value_when_pressed=False, pull=True)


## Onboard LED Setup

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    button = buttons.events.get()  # see if there are any key events
    if button:                      # there are events!
      if button.pressed:
        led.value = True
        print(button_labels[button.key_number], "button pressed!")
        m.move(x_value[button.key_number], y_value[button.key_number])
      if button.released:
        led.value = False
        print(button_labels[button.key_number], "button released!")
