import board
import digitalio
import neopixel
import time

# Setup
NUM_LEDS = 8
LED_PIN = board.GP3
BRIGHTNESS = 0.3

# LED strip setup
leds = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

# button pins
button_pins = [board.GP0, board.GP1, board.GP2, board.GP4]

# buttons setup
buttons = []
for pin in button_pins:
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP  # buttons go LOW when pressed
    buttons.append(btn)


# LED animation functions!!
def gradient_animation():
    # Light up LEDs with a gradient (red to yellow to green)
    colors = [
        (255, 0, 0),    # red
        (255, 64, 0),
        (255, 128, 0),
        (255, 192, 0),
        (255, 255, 0),
        (128, 255, 0),
        (64, 255, 0),
        (0, 255, 0),    # green
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
    # A quick left-to-right wipe
    for i in range(NUM_LEDS):
        leds[i] = (0, 128, 255)
        leds.show()
        time.sleep(0.03)
    time.sleep(0.05)
    set_all((0, 255, 0))  # Back to green


# Startup Animation
gradient_animation()
time.sleep(0.3)
set_all((0, 255, 0))  # green after boot

# Main Loop
while True:
    for btn in buttons:
        if not btn.value:  # Button pressed (LOW)
            press_animation()
            while not btn.value:  # wait until release
                time.sleep(0.01)
    time.sleep(0.01)
