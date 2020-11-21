## Introduction

The function `map_to_stl(...)` interpolates a set of 3D coordinates using the [Thin-Plate-Spline](https://en.wikipedia.org/wiki/Thin_plate_spline) method to define a 'map' (`z = f(x,y)`). A mesh is created from the map using [Delauny Triangulation](https://en.wikipedia.org/wiki/Delaunay_triangulation) and is saved to a standard 3D-printable .stl (STereo-Lithography) file.

## Example
```python
from map_to_stl import map_to_stl

# Define map axes
x_axis = np.arange(1, 10, 1)
y_axis = np.arange(1, 8, 1)

# Define randomly generated points (x,y,z) within the axes
num_points = 4
x = x_axis[0] + (np.random.random(num_points) * (x_axis[-1] - x_axis[0]))
y = y_axis[0] + (np.random.random(num_points) * (y_axis[-1] - y_axis[0]))
z = np.random.random(num_points) * 3

# Generate a mesh from the points and save to `mesh.stl`
map_to_stl(x_axis, y_axis, x, y, z, 'mesh.stl')
```

### Thin-Plate-Spline interpolated mesh with original points in red
![Mesh](/doc/mesh_interp.PNG)

### Delauny-triangulated mesh in preparation for .stl generation
![Mesh](/doc/mesh_tri.PNG)

### Final .stl mesh
![Mesh](/doc/mesh.PNG)

## Installation

1. Clone this repo add it to your path
2. Install dependencies with `pip install requirements.txt`
3. Run the function `map_to_stl` in `map_to_stl.py`
