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

from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
