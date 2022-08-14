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
            animations.colorWipe(strip, Color(100, 0, 120), 50)  # Red wipe
            #animations.colorWipe(strip, Color(0, 255, 0), 100)  # Blue wipe
            #animations.colorWipe(strip, Color(0, 0, 255), 30)  # Green wipe

            print ('Fade Inside Out.')
            animations.fadeinsideout(strip, l, Color(0, 153, 255), Color(180, 180, 0), fade_ms=3000)
            
    except KeyboardInterrupt:
        if args.clear:
            animations.colorWipe(strip, Color(0, 0, 0), wait_ms=10)
