import data.dome as dome

v = dome.vertices
print("%3d vertices loaded." % (len(v)))

# leds contains LED refs
#   LED number
#   Vertex number
#   Vertex coords
#   In or Out
# iterate through v and set up list of LEDs, 4 per vertex

leds = []

for x in v:
    i = v.get(x)[3]
    leds.append([(4 * x) - 3, x, v.get(x), i])
    leds.append([(4 * x) - 2, x, v.get(x), 1])
    leds.append([(4 * x) - 1, x, v.get(x), 1])
    leds.append([(4 * x) - 0, x, v.get(x), int(not(i))])

print("%3d LEDs loaded." % (len(leds)))