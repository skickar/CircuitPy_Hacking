import board
import keypad
import digitalio

## Keypad Button Setup

button_pins = (board.D3, board.D6, board.D7, board.D5)
button_labels = ["Down", "Up", "Left", "Right", ]
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
      if button.released:
        led.value = False
        print(button_labels[button.key_number], "button released!")
