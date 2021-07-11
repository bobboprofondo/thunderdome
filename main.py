# import board
# import neopixel



def main():
    print('Setup Vertices')
    # vertices 
    #   x - coordinate
    #   y - coordinate
    #   z - coordinate
    #   in first
    #       0 - Outside single LED wired first
    #       1 - Inside three LEDs wired first
    v =  {
        1 : [0.282952, 0.38945, 0.876508, 0],
        2 : [0.457826, -0.148757, 0.876508, 1],
        3 : [0, -0.481387, 0.876508, 0],
        4 : [-0.457826, -0.148757, 0.876508, 1],
        5 : [-0.282952, 0.38945, 0.876508, 0],
        6 : [0, 0, 1, 1]
    }
    print("%2d vertices loaded." % (len(v)))
    
    # iterate through v and set up list of LEDs, 4 per vertex
    d = []
    # d contains LED refs
    #   LED number
    #   Vertex number
    #   Vertex coords
    #   In or Out

    for x in v:
        i = v.get(x)[3]
        d.append([(4 * x) - 3, x, v.get(x), i])
        d.append([(4 * x) - 2, x, v.get(x), 1])
        d.append([(4 * x) - 1, x, v.get(x), 1])
        d.append([(4 * x) - 0, x, v.get(x), int(not(i))])

    print("%2d LEDs loaded." % (len(d)))
    
main()