# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 17:47:04 2019

@author: HO0me
"""

import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x % 3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

#Set the chart title and label axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

#Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show()