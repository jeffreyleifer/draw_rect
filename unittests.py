import unittest
from PySide2.QtCore import QPoint
from draw_utils import is_adjacent, is_contained, is_intersect
from rectangle import Rectangle


class TestDrawUtilsMethods(unittest.TestCase):

    def test_isAdjacent(self):
        
        """Upper left, left adjacent to r2, top adjacent to r3"""
        start_r1 = QPoint(0,0)
        end_r1 = QPoint(100,100)
        r1 = Rectangle(start_r1,end_r1)
        """right adjacent to r1"""
        start_r2 = QPoint(100,0)
        end_r2 = QPoint(200,100)
        r2 = Rectangle(start_r2,end_r2)
        """bottom adjacent to r1"""
        start_r3 = QPoint(0,100)
        end_r3 = QPoint(100,200)
        r3 = Rectangle(start_r3,end_r3)
        """Fail case input"""
        start_rf = QPoint(300,300)
        end_rf = QPoint(400,400)
        rf = Rectangle(start_rf,end_rf)

        """Pass case"""
        self.assertTrue(is_adjacent(r1,r2,silent=False))
        self.assertTrue(is_adjacent(r1,r3,silent=False))
        self.assertTrue(is_adjacent(r2,r1,silent=False))
        self.assertTrue(is_adjacent(r3,r1,silent=False))
        """Fail case"""
        self.assertFalse(is_adjacent(r1,rf,silent=False))
        self.assertFalse(is_adjacent(r2,rf,silent=False))
        self.assertFalse(is_adjacent(r3,rf,silent=False))


    def test_isContained(self):
        """Outer of r2"""
        start_r1 = QPoint(0,0)
        end_r1 = QPoint(100,100)
        r1 = Rectangle(start_r1,end_r1)
        """Inner of r1"""
        start_r2 = QPoint(25,25)
        end_r2 = QPoint(75,75)
        r2 = Rectangle(start_r2,end_r2)
        """Fail case input"""
        start_rf = QPoint(300,300)
        end_rf = QPoint(400,400)
        rf = Rectangle(start_rf,end_rf)

        """Pass case"""
        self.assertTrue(is_contained(r1,r2))
        """Fail case"""
        self.assertFalse(is_contained(r1,rf))

    def test_isIntersect(self):
        start_r1 = QPoint(0,0)
        end_r1 = QPoint(100,100)
        r1 = Rectangle(start_r1,end_r1)
        """2 point intersection of r1"""
        start_r2 = QPoint(25,25)
        end_r2 = QPoint(200,100)
        r2 = Rectangle(start_r2,end_r2)
        """4 point intersection of r2"""
        start_r3 = QPoint(100,15)
        end_r3 = QPoint(150,200)
        r3 = Rectangle(start_r3,end_r3)
        """Fail case input"""
        start_rf = QPoint(300,300)
        end_rf = QPoint(400,400)
        rf = Rectangle(start_rf,end_rf)

        """Pass case"""
        self.assertTrue(is_intersect(r1,r2))
        self.assertTrue(is_intersect(r2,r3))
        """Fail case"""
        self.assertFalse(is_intersect(r1,rf))

if __name__ == '__main__':
    unittest.main()
