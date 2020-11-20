import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from stl import mesh
from scipy import interpolate
from scipy.spatial import Delaunay


def map_to_stl(x_axis, y_axis, x, y, z, output_filename=None, show_plots=True):
    '''
    This function interpolates a mesh from a set of 3D coordinates that define a 'map' (a function of two inputs `z = f(x,y)` ) using the Thin-Plate Spline method.

    A standard 3D-printable .stl (STereo-Lithography) file is saved to `output_filename` if provided.

    Args:
        x_axis, y_axis (np.array): 3D map axis
        x, y, z (np.array): Coordinates of points in 3-dimensional space. Coordinates can fall anywhere within the min/max of the provided axes.
        output_filename (str): Name of .stl file
        show_plots (bool): Turn on/off plotting

    '''

    assert np.logical_and(x > min(x_axis), x < max(
        x_axis)).all(), " Coordinates must lie within the axes bounds"
    assert np.logical_and(y > min(y_axis), y < max(
        y_axis)).all(), " Coordinates must lie within the axes bounds"

    # Interpolate between points using the thin plate spline algorithm
    interp = interpolate.Rbf(x, y, z, function='thin_plate')
    xi, yi = np.meshgrid(x_axis, y_axis)
    zi = interp(xi, yi)

    # Plot the initial interpolated surface
    fig = plt.figure()
    ax_interp = axes3d.Axes3D(fig)
    ax_interp.plot_surface(xi, yi, zi, alpha=0.5)
    ax_interp.scatter3D(x, y, z, c="red")
    if show_plots:
        plt.show()

    # Create the mesh

    # Triangulate the parameter space
    points = np.array([xi.flatten(), yi.flatten()]).T
    tri = Delaunay(points)

    # Plot the triangulated surface
    fig = plt.figure()
    ax_trisurf = axes3d.Axes3D(fig)
    ax_trisurf.plot_trisurf(xi.flatten(), yi.flatten(), zi.flatten(),
                            triangles=tri.simplices, cmap=plt.cm.Spectral)
    if show_plots:
        plt.show()

    # Save result to a .stl file
    if output_filename:

        vertices = points = np.array(
            [xi.flatten(), yi.flatten(), zi.flatten()]).T
        faces = tri.simplices

        map_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype), )
        for i, f in enumerate(faces):
            for j in range(3):
                map_mesh.vectors[i][j] = vertices[f[j], :]

        map_mesh.save(output_filename)

    return ax_interp, ax_trisurf,
