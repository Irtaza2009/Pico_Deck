import board
import digitalio
import neopixel
import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Setup
NUM_LEDS = 8
LED_PIN = board.GP3
BRIGHTNESS = 0.3

leds = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

# button pins and actions
button_configs = [
    {"pin": board.GP0, "keys": [Keycode.CONTROL, Keycode.C]},  # Copy
    {"pin": board.GP1, "keys": [Keycode.CONTROL, Keycode.V]},  # Paste
    {"pin": board.GP2, "keys": [Keycode.CONTROL, Keycode.Z]},  # Undo
    {"pin": board.GP4, "keys": [Keycode.CONTROL, Keycode.Y]},  # Redo
]

# buttons setup
buttons = []
for cfg in button_configs:
    btn = digitalio.DigitalInOut(cfg["pin"])
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    buttons.append(btn)

# HID keyboard
keyboard = Keyboard(usb_hid.devices)

# LED animation functions!!
def gradient_animation():
    colors = [
        (255, 0, 0),
        (255, 64, 0),
        (255, 128, 0),
        (255, 192, 0),
        (255, 255, 0),
        (128, 255, 0),
        (64, 255, 0),
        (0, 255, 0),
    ]
    for i in range(NUM_LEDS):
        leds[i] = colors[i]
        leds.show()
        time.sleep(0.05)

def set_all(color):
    for i in range(NUM_LEDS):
        leds[i] = color
    leds.show()

def press_animation():
    for i in range(NUM_LEDS):
        leds[i] = (0, 128, 255)
        leds.show()
        time.sleep(0.02)
    set_all((0, 255, 0))

# Startup Effect
gradient_animation()
time.sleep(0.2)
set_all((0, 255, 0))

# Main Loop
while True:
    for i, btn in enumerate(buttons):
        if not btn.value:  # Button pressed
            press_animation()
            keycombo = button_configs[i]["keys"]
            keyboard.press(*keycombo)
            time.sleep(0.1)
            keyboard.release_all()
            while not btn.value:
                time.sleep(0.01)
    time.sleep(0.01)
