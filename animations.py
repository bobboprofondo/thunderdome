#!/usr/bin/env python3
# Author: Bob Forbes (github@bobboprofondo.co.uk)
#
# various animations on a strip of NeoPixels.

import time
from datetime import datetime, timedelta
import argparse
from rpi_ws281x import Color
import colorsys 
from math import sqrt

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    print("colorWipe: ", color, " wait_ms: ", wait_ms)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def simpleTest(strip, color, l, wait_ms=50):

    print(strip.numPixels())

    for i in range(strip.numPixels()):
        print(strip.pixels[i])
        time.sleep(wait_ms/1000.0)

def insideout(strip, l, color1, color2=Color(0, 0, 0), brightness=1., wait_ms=500):
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

def fadein(strip, l, colorin, colorout=Color(0, 0, 0), brightness=1., fade_ms=2000, hold_ms=0):
    print("fadein: ", colorin, ", ", colorout, " fade_ms: ", fade_ms, " hold_ms: ", hold_ms)
    # Alternate colour on inside and outside clusters
    starttime = datetime.today()
    fadeuptime = starttime + timedelta(milliseconds=fade_ms)
    endtime = starttime + timedelta(milliseconds=fade_ms + hold_ms)

    for i in range(strip.numPixels()):
        # Alternate color on off based on whether inout flag for LED is 1 (In) or 0 (Out)
        if l[i][3] == 1:
            strip.setPixelColor(i, colorin)
        else:
            strip.setPixelColor(i, colorout)

    while datetime.today() <= fadeuptime:
        # Calculate how far through the fade we should be as a percentage 
        progress = (datetime.today() - starttime) / (endtime - starttime)
        strip.setBrightness(round((progress ** 2) * 255)) # Straightline (?) brightness from 0 to full        
        strip.show()
    
    time.sleep(hold_ms/1000)

def fadeinandout(strip, l, colorin, colorout=Color(0, 0, 0), brightness=1., fade_ms=2000, hold_ms=0):
    print("fadeinandout: ", colorin, ", ", colorout, " fade_ms: ", fade_ms, " hold_ms: ", hold_ms)
    # Alternate colour on inside and outside clusters
    starttime = datetime.today()
    fadeuptime = starttime + timedelta(milliseconds=fade_ms)
    fadedowntime = starttime + timedelta(milliseconds=fade_ms + hold_ms)
    endtime = starttime + timedelta(milliseconds=(fade_ms * 2) + hold_ms)

    for i in range(strip.numPixels()):
        # Alternate color on off based on whether inout flag for LED is 1 (In) or 0 (Out)
        if l[i][3] == 1:
            strip.setPixelColor(i, colorin)
        else:
            strip.setPixelColor(i, colorout)

    while datetime.today() <= fadeuptime:
        # Calculate how far through the fade we should be as a percentage 
        progress = (datetime.today() - starttime) / (fadeuptime - starttime)
        #print("Progress ", progress)
        strip.setBrightness(round(brightness * (progress ** 2) * 255)) # Straightline (?) brightness from 0 to full        
        strip.show()

    time.sleep(hold_ms/1000)

    while datetime.today() <= endtime:
        # Calculate how far through the fade we should be as a percentage 
        progress = 1 - (datetime.today() - fadedowntime) / (endtime - fadedowntime)
        #print("Progress ", progress)
        strip.setBrightness(round(brightness * (progress ** 2) * 255)) # Straightline (?) brightness from 0 to full        
        strip.show()

def rainbowfade(strip, l, brightness=1., fade_ms=2000, hold_ms=0):
    strip.setBrightness(255)
    print("rainbowfade: fade_ms: ", fade_ms, " hold_ms: ", hold_ms)
    # Alternate colour on inside and outside clusters
    starttime = datetime.today()
    fadeuptime = starttime + timedelta(milliseconds=fade_ms)
    fadedowntime = starttime + timedelta(milliseconds=fade_ms + hold_ms)
    endtime = starttime + timedelta(milliseconds=(fade_ms * 2) + hold_ms)

    pixelcount = strip.numPixels()
    
    while datetime.today() <= fadeuptime:
        # Calculate how far through the fade we should be as a percentage 
        progress = (datetime.today() - starttime) / (fadeuptime - starttime)
        #print("Progress ", progress)

        for i in range(pixelcount):
            # Get pixel z value to determine colour on Hue cycle
            zval = l[i][2][2]
            # zval = (l[i][2][1] + 0.5) / 2
            pc = hsv2rgb((zval + progress) % 1, 1., (brightness) * (progress ** 2))
            strip.setPixelColor(i, Color(pc[0],pc[1],pc[2]))
           

        strip.show()

    time.sleep(hold_ms/1000)

    while datetime.today() <= endtime:
        # Calculate how far through the fade we should be as a percentage 
        progress = 1 - (datetime.today() - fadedowntime) / (endtime - fadedowntime)
        #print("Progress ", progress)
        for i in range(pixelcount):
            # Get pixel z value to determine colour on Hue cycle
            zval = l[i][2][2]
            # zval = (l[i][2][1] + 0.5) / 2
            pc = hsv2rgb((zval + progress) % 1, 1., brightness * (progress ** 2))
            strip.setPixelColor(i, Color(pc[0],pc[1],pc[2]))

        strip.show()

def rainbowloop(strip, l, brightness=1., loop_ms = 10000):
    print("rainbowloop: loops_ms ", loop_ms)
    pixelcount = strip.numPixels()
    for i in range(strip.numPixels()):
        
        pc = hsv2rgb((i / pixelcount), 1., 0.1)
        strip.setPixelColor(i, Color(pc[0],pc[1],pc[2]))

    strip.show()
    time.sleep(loop_ms/1000.0)



# HSV Conversion function
def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))