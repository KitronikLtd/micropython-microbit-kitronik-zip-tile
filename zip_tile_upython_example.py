from microbit import *
import neopixel
import math

# Declare constants
LEDS_ON_PANEL = 64

# Define a display with a number of ZIP Tiles
# Function parameters: (Num Horizontal Tiles, Num Vertical Tiles, uBit "Hidden"/"Visible")
def setup_zip_tile_display(h_tiles, v_tiles, ubit_pos):
    global zip_tile_length
    global zip_tile_grid_width
    global zip_tile_grid_height
    global location
    global zip_tile_display
    
    zip_tile_length = (h_tiles * v_tiles * 64)
    zip_tile_grid_width = (h_tiles * 8)
    zip_tile_grid_height = (v_tiles * 8) 
    if ubit_pos is "Hidden":
        location = "H"
    elif ubit_pos is "Visible":
        location = "V"
    
    zip_tile_display = neopixel.NeoPixel(pin0, zip_tile_length)

# Enable ZIP Tile display to use x,y coordinates
def zip_tile_plot(x, y, r, g, b):
    x_div = x / 8
    y_div = y / 8
    floor_x = math.floor(x_div)
    floor_y = math.floor(y_div)
    total_tiles = zip_tile_length/LEDS_ON_PANEL
    if zip_tile_grid_height == 8:
        if location == "H":
            zip_led = (x+(y*8))+(floor_x*(LEDS_ON_PANEL-8))
        elif location == "V":
            zip_led = math.trunc((((zip_tile_grid_width/8)*LEDS_ON_PANEL)-1)-(x+(y*8))-(floor_x*(LEDS_ON_PANEL-8)))
    elif zip_tile_grid_width == 8:
        if location == "H":
            if y < 8:
                current_tile = 1
            else:
                current_tile = 2
        elif location == "V":
            if y < 8:
                current_tile = 2
            else:
                current_tile = 1        
        zip_led = math.trunc(((2*floor_y)-1)*(x+(y*8))+(current_tile*LEDS_ON_PANEL)-1-(floor_y*((total_tiles*LEDS_ON_PANEL)-1)))
    elif zip_tile_grid_height == 16 and zip_tile_grid_width == 16:
        if location == "H":
            zip_led = math.trunc((-255*(floor_y-1))+(2*floor_y-1)*(x+8*(y-floor_y*8))+(floor_y*floor_x*(LEDS_ON_PANEL-8))+(floor_y-1)*(floor_x*(LEDS_ON_PANEL-8)))
        elif location == "V":
            zip_led = math.trunc((-255*(floor_y-1))+(2*floor_y-1)*(x+8*(y-floor_y*8))+(floor_y*floor_x*(LEDS_ON_PANEL-8))+(floor_y-1)*(floor_x*(LEDS_ON_PANEL-8))-128+(floor_y*256))
        
    zip_tile_display[zip_led] = (r, g, b)
    
# ZIP Tile Display setup
setup_zip_tile_display(1, 1, "Hidden")

# Example display of ZIP LED at (3, 3)
x_value = 3
y_value = 3
zip_tile_plot(x_value, y_value, 64, 64, 64)
zip_tile_display.show()