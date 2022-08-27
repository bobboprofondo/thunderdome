import argparse
import time
from rpi_ws281x import *

import animations
import data.leds as leds

l = leds.leds

# LED strip configuration:
LED_COUNT      = len(l)  # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Thunderdome Preferred Colours
TD_BLUE = Color(0, 51, 240)
TD_PURPLE = Color(30, 0, 30)
TD_TEAL = Color(0, 153, 153)
TD_MAGENTA = Color(204, 0, 153)
TD_OFF = Color(0, 0, 0)

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    # TODO Fails when debugging on WSL Debian, as only runs on Raspberry Pi hardware. Handle different hardware somehow
    strip.begin() 

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            #print ('Color wipe animations.')
            # animations.colorWipe(strip, TD_BLUE, 15)  # Red wipe
            # animations.colorWipe(strip, TD_PURPLE, 55)  # Red wipe
            # animations.colorWipe(strip, TD_TEAL, 250)  # Red wipe
            # animations.colorWipe(strip, TD_MAGENTA, 30)  # Red wipe
            # animations.colorWipe(strip, TD_OFF, 50)
            # animations.fadeinandout(strip, l, TD_BLUE, TD_PURPLE, fade_ms=4500)
            # animations.fadeinandout(strip, l, TD_PURPLE, TD_TEAL, fade_ms=4500)
            # animations.fadeinandout(strip, l, TD_TEAL, TD_MAGENTA, fade_ms=4500)
            # animations.fadein(strip, l, TD_MAGENTA, TD_BLUE, fade_ms=4500)

            # animations.rainbowloop(strip, l, loop_ms=2000)
            animations.rainbowfade(strip, l, brightness=0.25, fade_ms=10000, hold_ms=20000)

            # animations.colorWipe(strip, TD_OFF, wait_ms=200)
            
    except KeyboardInterrupt:
        if args.clear:
            animations.colorWipe(strip, TD_OFF, wait_ms=10)
