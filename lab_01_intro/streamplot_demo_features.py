"""
Demo of the `streamplot` function.

A streamplot, or streamline plot, is used to display 2D vector fields. This
example shows a few features of the stream plot function:

    * Varying the color along a streamline.
    * Varying the density of streamlines.
    * Varying the line width along a stream line.
"""

# "images_contours_and_fields example code: streamplot_demo_features.py" images_contours_and_fields example code:
# streamplot_demo_features.py — Matplotlib 1.5.1 documentation. [Online]. Available:
# http://matplotlib.org/examples/images_contours_and_fields/streamplot_demo_features.html. [Accessed: 21-Aug-2016].


import matplotlib.pyplot as plt
import numpy as np

Y, X = np.mgrid[-3:3:100j, -3:3:100j]
U = -1 - X ** 2 + Y
V = 1 + X - Y ** 2
speed = np.sqrt(U * U + V * V)

plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap=plt.cm.autumn)
plt.colorbar()

f, (ax1, ax2) = plt.subplots(ncols=2)
ax1.streamplot(X, Y, U, V, density=[0.5, 1])

lw = 5 * speed / speed.max()
ax2.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)

plt.show()
