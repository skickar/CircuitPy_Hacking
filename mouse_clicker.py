import board
import keypad
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import usb_hid
from adafruit_hid.mouse import Mouse

## Mouse Setup for moving

m = Mouse(usb_hid.devices)
sensitivity = 30
x_value = [0,0,-sensitivity, sensitivity]
y_value = [sensitivity,-sensitivity,0,0]

## Keypad Button Setup

button_pins = (board.D3, board.D6, board.D7, board.D5, board.BUTTON)
button_labels = ["Down", "Up", "Left", "Right", "Click"]
buttons = keypad.Keys(button_pins, value_when_pressed=False, pull=True)

while True:
    button = buttons.events.get()  # see if there are any key events
    if button:                      # there are events!
      if button.pressed and button.key_number == 4: # Check for a click
        m.press(m.LEFT_BUTTON) # Press the mouse button
        print(" Mouse button pressed")
      if button.pressed and button.key_number != 4: # If there is no click
        print(button_labels[button.key_number], "button pressed")
        m.move(x_value[button.key_number], y_value[button.key_number]) # Move the mouse
      if button.released and button.key_number != 4: # If the button is released but not the mouse
        print(button_labels[button.key_number], "button released")
      if button.released and button.key_number == 4: # If the mouse is released
          m.release_all() # Release all mouse buttons
          print(" Mouse button released")
