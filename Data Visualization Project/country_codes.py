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

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code

    #If the country wasn't found.
    return None

print(get_country_code('Andorra'))
print(get_country_code('Afghanistan'))
print(get_country_code('United Arab Emirates'))
