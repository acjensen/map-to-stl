import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from stl import mesh
from scipy import interpolate
from scipy.spatial import Delaunay
np.random.seed(23452)

#%matplotlib inline

# define map axes
xMax = 400
xMin = 10
xInt = 10
yMax = 3000
yMin = 600
yInt = 100
xRange = range(xMin,xMax,xInt)
yRange = range(yMin,yMax,yInt)
xAxis = np.arange(xMin,xMax,xInt)
yAxis = np.arange(yMin,yMax,yInt)

# generate random points
numPoints = 15
x = xMin + ( np.random.random(numPoints) * (xMax - xMin) )
y = yMin + ( np.random.random(numPoints) * (yMax - yMin) )
z = np.random.random(numPoints) * 21 - 5

# interpolate between points
interp = interpolate.Rbf(x, y, z, function='thin_plate')
xi, yi = np.mgrid[xRange,yRange]
zi = interp(xi,yi)

# plot
fig = plt.figure()
ax = axes3d.Axes3D(fig)
ax.plot_surface(xi,yi,zi)
ax.scatter3D(x,y,z)
plt.show()

# trangulate parameter space
tri = Delaunay(np.array([xi,yi]).T[0])

fig = plt.figure()
ax = axes3d.Axes3D(fig)
ax.plot_trisurf(x, y, z, triangles=tri.simplices, cmap=plt.cm.Spectral)
plt.show()



myMesh = mesh.Mesh(z, remove_empty_areas=False)
myMesh.save('myMesh.stl')