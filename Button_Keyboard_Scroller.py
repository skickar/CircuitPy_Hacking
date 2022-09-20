import board
import keypad
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

## Keycode Setup for scrolling

KEYCODES = (
    Keycode.DOWN_ARROW,
    Keycode.UP_ARROW,
    Keycode.LEFT_ARROW,
    Keycode.RIGHT_ARROW,
    Keycode.SHIFT,
)

kbd = Keyboard(usb_hid.devices)

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
        kbd.press(KEYCODES[button.key_number])
      if button.released:
        led.value = False
        print(button_labels[button.key_number], "button released!")
        kbd.release(KEYCODES[button.key_number])
