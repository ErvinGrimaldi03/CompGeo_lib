import unittest
from Point import Point
from convHull_2D import *

class TestMin_i(unittest.TestCase):
    def test_empty_list(self):
        points = []
        with self.assertRaises(ValueError):
            min_i(points)

    def test_one_entry_list(self):
        p = (1,0)
        point = Point(p)
        points = [point]
        self.assertEquals(min_i(points), point)

    def test_two_same_entry_list(self):
        ps = [(1,0), (1,0)]
        p = Point((1,0))
        points = [Point(i) for i in ps]
        self.assertEquals(min_i(points), p)


    def test_multiple_entry_list(self):
        ps = [(1,0), (4,8), (12,5), (2,64), (43,3), (1,3), (5,4), (98,23), (4, 23), (23,12)]
        p = Point((1,0))
        points = [Point(i) for i in ps]
        self.assertEquals(min_i(points), p)

    def test_multiple_entry_with_two_same_y_coordinate_list(self):
        ps = [(4,8), (12,5), (2,64), (43,3), (1,3), (5,4), (98,23), (4, 23), (23,12)]
        p = Point((1, 3))
        points = [Point(i) for i in ps]
        self.assertEquals(min_i(points), p)