#!/usr/bin/env python3
# Author: Bob Forbes (github@bobboprofondo.co.uk)
#
# various animations on a strip of NeoPixels.

import time
from datetime import datetime, timedelta
import argparse
from rpi_ws281x import Color
# from numpy import *
from math import sqrt

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
    starttime = datetime.today()
    endtime = starttime + timedelta(milliseconds=fade_ms)

    for i in range(strip.numPixels()):
        # Alternate color on off based on whether inout flag for LED is 1 (In) or 0 (Out)
        if l[i][3] == 1:
            strip.setPixelColor(i, color1)
        else:
            strip.setPixelColor(i, color2)

    while datetime.today() <= endtime:
        # Calculate how far through the fade we should be as a percentage 
        progress = (datetime.today() - starttime) / (endtime - starttime)
        strip.setBrightness(round((progress ** 2) * 255)) # Straightline (?) brightness from 0 to full        
        strip.show()

def rainbowloop(strip, l, loop_ms = 10000):
    pixelcount = range(strip.numPixels())
    for i in pixelcount:
        strip.setPixelColor(i, hsv_to_rgb(round(i / pixelcount), 1., 1.))

    strip.show()
    time.sleep(loop_ms/1000.0)


# HSV Conversion function
def hsv_to_rgb(h, s, v):
    shape = h.shape
    i = int_(h*6.)
    f = h*6.-i

    q = f
    t = 1.-f
    i = ravel(i)
    f = ravel(f)
    i%=6

    t = ravel(t)
    q = ravel(q)

    clist = (1-s*vstack([zeros_like(f),ones_like(f),q,t]))*v

    #0:v 1:p 2:q 3:t
    order = array([[0,3,1],[2,0,1],[1,0,3],[1,2,0],[3,1,0],[0,1,2]])
    rgb = clist[order[i], arange(prod(shape))[:,None]]

    return rgb.reshape(shape+(3,))
