from unittest import TestCase
import unittest.main
import numpy as np
from map_to_stl import map_to_stl


class MapToStlTest(TestCase):

    def test_simple(self):

        # Define map axes
        x_axis = np.arange(1, 10, 1)
        y_axis = np.arange(1, 8, 1)

        # Define a rough surface using randomly generated points
        num_points = 10
        x = x_axis[0] + (np.random.random(num_points)
                         * (x_axis[-1] - x_axis[0]))
        y = y_axis[0] + (np.random.random(num_points)
                         * (y_axis[-1] - y_axis[0]))
        z = np.random.random(num_points) * (3 - (-2)) - 2

        # Generate a mesh from the points and save to the .stl file
        map_to_stl(x_axis, y_axis, x, y, z, 'mesh_simple.stl')

        # TBD: real tests
        self.assertTrue(True)

    def test_complex(self):

        # Define map axes
        x_axis = np.arange(10, 400, 10)
        y_axis = np.arange(600, 3000, 100)

        # Define a rough surface using randomly generated points
        num_points = 15
        x = x_axis[0] + (np.random.random(num_points)
                         * (x_axis[-1] - x_axis[0]))
        y = y_axis[0] + (np.random.random(num_points)
                         * (y_axis[-1] - y_axis[0]))
        z = np.random.random(num_points) * 100 - 50

        # Generate a mesh from the points and save to the .stl file
        map_to_stl(x_axis, y_axis, x, y, z, 'mesh_complex.stl')

        # TBD: real tests
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
