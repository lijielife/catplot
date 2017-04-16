#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test case for 2D grid canvas.
"""

import unittest

from matplotlib.collections import PathCollection

from catplot.grid_components.grid_canvas import Grid2DCanvas
from catplot.grid_components.nodes import Node2D


class Grid2DCanvasTest(unittest.TestCase):

    def setUp(self):
        self.maxDiff = True

    def test_construction_and_query(self):
        """ Test the 2D grid canvas can be constructed corretly.
        """
        canvas = Grid2DCanvas()

        self.assertListEqual(canvas.nodes, [])
        self.assertListEqual(canvas.edges, [])
        self.assertTrue(isinstance(canvas.collection, PathCollection))

    def test_add_node(self):
        """ Make sure we can add node to canvas correctly.
        """
        canvas = Grid2DCanvas()

        n1 = Node2D([0.5, 0.5])
        n2 = Node2D([1.0, 1.0])
        canvas.add_node(n1)
        canvas.add_node(n2)

        # Check nodes in canvas.
        self.assertTrue(canvas.nodes)
        for node in canvas.nodes:
            self.assertTrue(isinstance(node, Node2D))

        # Check colors.
        for c in canvas.node_edgecolors:
            self.assertEqual(c, "#000000")

        for c in canvas.node_colors:
            self.assertEqual(c, "#000000")

        # Check cooridnates.
        ref_coordinates = [[0.5, 0.5], [1.0, 1.0]]
        self.assertListEqual(ref_coordinates, canvas.node_coordinates.tolist())

if "__main__" == __name__: 
    suite = unittest.TestLoader().loadTestsFromTestCase(Grid2DCanvasTest)
    unittest.TextTestRunner(verbosity=2).run(suite) 

