#!/usr/bin/env python3
# Author: Bob Forbes (github@bobboprofondo.co.uk)
#
# various animations on a strip of NeoPixels.

import time
from datetime import datetime, timedelta
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

def insideout(strip, l, color1, color2=Color(0, 0, 0), wait_ms=500):
    # Alternate colour on inside and outside clusters
    # Setup first run through colour
    # Once looping, this determines current list state
    if strip.getPixelColor(0) == color1: 
        makein = 1
    else:
        makein = 0

    for i in range(strip.numPixels()):
        # Alternate color on off based on whether inout flag for LED is 1 (In) or 0 (Out)
        if l[i][3] == makein:
            strip.setPixelColor(i, color1)
        else:
            strip.setPixelColor(i, color2)
    
    strip.show()
    time.sleep(wait_ms/1000.0)

def fadeinsideout(strip, l, color1, color2=Color(0, 0, 0), fade_ms=2000):
    # Alternate colour on inside and outside clusters
    # Setup first run through colour
    # Once looping, this determines current list state
    starttime = datetime.today()
    endtime = starttime + timedelta(milliseconds=fade_ms)

    while datetime.today() <= endtime:
        # Calculate how far through the fade we should be as a percentage 
        progress = (datetime.today() - starttime) / (endtime - starttime)
        print(progress)
        print(color1)
        print(color2)

        b = round(color1 / 65536)
        g = round((color1 - b) / 256)
        r = color1 - b - g
        print("r ", r, " g ", g, " b ", b)

        for i in range(strip.numPixels()):
            # Alternate color on off based on whether inout flag for LED is 1 (In) or 0 (Out)
            if l[i][3] == 1:
                strip.setPixelColor(i, Color(round(r * progress), round(g * progress), round(b * progress)))
            else:
                r = round(color2 / 65536)
                g = round((color2 - r) / 256)
                b = color2 - r - g
                strip.setPixelColor(i, Color(round(r * progress), round(g * progress), round(b * progress)))
        
        strip.show()
