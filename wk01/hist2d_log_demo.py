from matplotlib.colors import LogNorm
from pylab import *

#normal distribution center at x=0 and y=5
x = randn(100000)
y = randn(100000)+5

H, xedges, yedges = histogram2d(x, y, bins=40)

extent = [yedges[0], yedges[-1], xedges[-1], xedges[0]]
plt.imshow(H, extent=extent, interpolation='nearest')
colorbar()
show()
