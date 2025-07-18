import board
import digitalio
import neopixel
import time
import usb_hid

from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Configuration
NUM_LEDS = 8
LED_PIN = board.GP3
BRIGHTNESS = 0.3
PAYLOAD_FILES = ["payload1.txt", "payload2.txt", "payload3.txt", "payload4.txt"]
BUTTON_PINS = [board.GP0, board.GP1, board.GP2, board.GP4]

# Setup
leds = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)
buttons = []

for pin in BUTTON_PINS:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    buttons.append(btn)

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

def gradient_animation():
    colors = [
        (255, 0, 0), (255, 64, 0), (255, 128, 0), (255, 192, 0),
        (255, 255, 0), (128, 255, 0), (64, 255, 0), (0, 255, 0)
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
        leds[i] = (255, 0, 128)
        leds.show()
        time.sleep(0.01)
    set_all((0, 255, 0))

def run_payload(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                elif line.startswith("DELAY "):
                    time.sleep(int(line.split()[1]) / 1000)
                else:
                    layout.write(line)
                    keyboard.send(Keycode.ENTER)
                    time.sleep(0.05)
    except Exception as e:
        print(f"Error running {filename}: {e}")

# Startup
gradient_animation()
time.sleep(0.2)
set_all((0, 255, 0))

# Main Loop
while True:
    for i, btn in enumerate(buttons):
        if not btn.value:
            press_animation()
            run_payload(PAYLOAD_FILES[i])
            while not btn.value:
                time.sleep(0.01)
    time.sleep(0.01)
