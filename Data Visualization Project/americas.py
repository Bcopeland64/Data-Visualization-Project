#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HO0me
#
# Created:     21/04/2019
# Copyright:   (c) HO0me 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from pygal_maps_world.maps import World

wm = World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
