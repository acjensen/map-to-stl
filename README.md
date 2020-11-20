## Introduction

The single function `map_to_stl` interpolates a mesh from a set of 3D coordinates that define a 'map' (a function of two inputs `z = f(x,y)` ) using the Thin-Plate Spline method. The mesh is saved to a standard 3D-printable .stl (STereo-Lithography) file.

## Example
```python

# Define map axes
x_axis = np.arange(1, 10, 1)
y_axis = np.arange(1, 8, 1)

# Define randomly generated points (x,y,z) within the axes
num_points = 4
x = x_axis[0] + (np.random.random(num_points) * (x_axis[-1] - x_axis[0]))
y = y_axis[0] + (np.random.random(num_points) * (y_axis[-1] - y_axis[0]))
z = np.random.random(num_points) * 3

# Generate a mesh from the points and save to `mesh.stl`
ax_interp, ax_trisurf = map_to_stl(x_axis, y_axis, x, y, z, 'mesh.stl')
ax_interp.show()
ax_trisurf.show()
```

### Thin-Plate-Spline interpolated mesh with original points in red
![Mesh](mesh_interp.PNG)

### Delauny-triangulated mesh in preparation for .stl generation
![Mesh](mesh_tri.PNG)

### Final .stl mesh
![Mesh](mesh.PNG)

## Installation

1. Clone this repo add it to your path
2. Install dependencies with `pip install requirements.txt`
3. Run the function `map_to_stl` in `map_to_stl.py`
