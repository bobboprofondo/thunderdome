# thunderdome
Python scripts for lighting the Thunderdome with WS2812 LEDs
- All designed around a very specific LED geometry for my garden geodesic dome. 
- Each vertex has 4 LEDs, one on the outside, three on the inside. 

# Entry Points
## main.py
- Use main.py for development work in Windows (uses devpixel to replicate AdaFruit rpi object model)
- Eventually this will display the output of the animations locally to aid in developing new animations

## rpimain.py
- Run this file to call the same animations, but output to GPIO pins on Raspberry Pi environment. 

## animations.py
- Common list of animations expressed as functions. 
- Each animation updates the strip object with RGB values per LED