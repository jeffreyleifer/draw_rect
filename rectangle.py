from PySide2.QtCore import QRect
from PySide2.QtCore import QPoint

"""
Rectangle
* Rectangle class derived from QRect
* Includes rotation functions and helper function for points
"""

class Rectangle(QRect):
    def __init__(self,begin,end):
        super().__init__(begin_point,end_point)
    
    """
     flip_h
     * Flip Coordinates of the rectangle horizontally
    """
    def flip_h(self):
        tl = self.topLeft()
        tr = self.topRight()
        bl = self.bottomLeft()
        br = self.bottomRight()
        self.setTopLeft(tr)
        self.setTopRight(tl)
        self.setBottomRight(bl)
        self.setBottomLeft(br)

    """
     flip_v
    * Flip Coordinates of the rectangle vertically
    """
    def flip_v(self):
        tl = self.topLeft()
        tr = self.topRight()
        bl = self.bottomLeft()
        br = self.bottomRight()
        self.setTopLeft(bl)
        self.setTopRight(br)
        self.setBottomRight(tr)
        self.setBottomLeft(tl)

    """
     refl
     * Calls flip_h and flip_v to create a reflextion of original rectangle
    """
    def refl(self):
        rect = self.flip_h()
        rect = self.flip_v()
