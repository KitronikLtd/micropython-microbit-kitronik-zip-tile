# micropython-microbit-kitronik-zip-tile
Example MicroPython (for BBC micro:bit) code for the Kitronik ZIP Tile ( www.kitronik.co.uk/5645 )

## Overview

This repo contains an example of a MicroPython program for the Kitronik ZIP Tile.
No unique functions are required to use the ZIP Tile, just the normal use of the 'microbit' and 'neopixel' libraries.
Some helpful calculations have been provided for setting the (x,y) ZIP LED coordinates on multi-tile displays. 

## Example File

The file 'zip_tile_upython_example.py' is a simple program which just sets a single ZIP LED at position (3,3) to be white.

The 'setup_zip_tile_display' function takes the following parameters:
	(Number of Horizontal Tiles, Number of Vertical Tiles, BBC micro:bit Position)
Note: See the product datasheet at the above web address for an explanation of BBC micro:bit positions.
The function then creates a string of NeoPixels the appropriate length.

The 'zip_tile_plot' function takes the following parameters:
	(x-coordinate, y-coordinate, Red LED brightness, Green LED brightness, Blue LED brightness)
The function then establishes which ZIP LED should be turned on depending on the coordinates, the number of ZIP Tile, 
the arrangement of the ZIP Tiles in te display and the position of the BBC micro:bit - there are different equations for each one.

## License

MIT

## Supported Targets

BBC micro:bit
