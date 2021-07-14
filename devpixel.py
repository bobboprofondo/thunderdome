import data.leds as leds

l = leds.leds

class ProxyAdafruitNeopixel:
    # Put in place to handle calls in animations definitions for 
    # programming animations / debugging
    def __init__(self):
        self.__pixels = l

    @property
    def pixels(self):
        return self.__pixels
    
    def numPixels(self):
        return len(self.__pixels)
    
    def setPixelColor(self, i, color):
        self.pixels[i][5] = color
    
    def show():
        print("Brap!")