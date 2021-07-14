# thunderdome
Python scripts for lighting the Thunderdome with WS2812 LEDs

# Hardware
- All designed around a very specific LED geometry for my garden geodesic dome. 
- Each vertex holds 4 LEDs, one on the outside, three on the inside. 
- Due to cable routing, each vertex is wired alternately, with the outside LED first, then inside LED cluster first etc.

# File functionality
## main.py
- Use main.py for development work in Windows (uses devpixel to replicate AdaFruit rpi object model)
- Eventually this will display the output of the animations locally to aid in developing new animations

## rpimain.py
- Run this file to call the same animations, but output to GPIO pins on Raspberry Pi environment. 

## animations.py
- Common list of animation functions. 
- Each animation updates the strip object with RGB values per LED

## data/dome.py
- Contains the three cartesian coordinates of each vertex in the dome, to be used in animations
- Currently shows the top 6 vertices, but depending on how the hardware develops, will contain locations of all 25 vertices
- (Full list of 25 vertex coords are in dome_backup.py)