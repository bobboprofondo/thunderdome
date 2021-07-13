import time
import argparse

import animations
import devpixel

    
def main():
    # get list of leds and their coords
    strip = devpixel.ProxyAdafruitNeopixel
    animations.simpleTest(strip(), (0, 255, 0), 5)
    # animations.colorWipe(strip, (0,255,0), 5)
    
main()