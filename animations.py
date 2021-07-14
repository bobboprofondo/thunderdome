#!/usr/bin/env python3
# Author: Bob Forbes (github@bobboprofondo.co.uk)
#
# various animations on a strip of NeoPixels.

import time
import argparse
from rpi_ws281x import Color

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def simpleTest(strip, color, l, wait_ms=50):

    print(strip.numPixels())

    for i in range(strip.numPixels()):
        print(strip.pixels[i])
        time.sleep(wait_ms/1000.0)

def insideout(strip, color, l, wait_ms=500):
    # Alternate colour on inside and outside clusters
    # Setup first run through colour
    if strip.getPixelColor(1) == color: 
        makein = 1
    else:
        makein = 0

    print(makein,color)

    for i in range(strip.numPixels()):
        # Check if inout flag for LED is 1 (In) or 0 (Out)
        print(l[i-1],strip.getPixelColor(i))
        if l[i-1][3] == makein:
            strip.setPixelColor(i, color)
        else:
            strip.setPixelColor(i, Color(0, 0, 0))
        
    strip.show()
    time.sleep(wait_ms/1000.0)
