import board
import neopixel

from adafruit_circuitplayground.express import cpx
import adafruit_fancyled.adafruit_fancyled as fancy

cpx.pixels.auto_write = False  # Update only when we say
cpx.pixels.brightness = 1   # make less blinding

NUM_STRIP_PIXELS = 60
strip = neopixel.NeoPixel(board.A1, NUM_STRIP_PIXELS, brightness=1.0, auto_write=False)

# palette = [fancy.CRGB(255, 0, 0),  # Red
#           fancy.CRGB(255, 192, 203),  # Pink
#           fancy.CRGB(255, 192, 203),  # Pink
#           fancy.CRGB(255, 0, 0)]      # Red

# palette = [fancy.CRGB(255, 0, 0),
#           fancy.CRGB(255, 50, 50)]

palette = [fancy.CRGB(255, 0, 0)]

offset = 0  # Position offset into palette to make it "spin"


while True:
    for i in range(10):
        color = fancy.palette_lookup(palette, offset + i / 9)
        cpx.pixels[i] = color.pack()
    cpx.pixels.show()

    for i in range(NUM_STRIP_PIXELS):
        color = fancy.palette_lookup(palette, offset + i / 9)
        strip[i] = color.pack()
    strip.show()


    offset += 0.033  # Bigger number = faster spin
