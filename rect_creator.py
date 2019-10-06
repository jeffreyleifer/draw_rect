from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import QWidget, QLabel
from PySide2.QtGui import QPainter
from PySide2.QtGui import QPixmap
from PySide2.QtGui import QPen
from draw_utils import is_adjacent, is_contained,is_intersect
                        
from rectangle import Rectangle
from constants import RECT_A,RECT_B,PEN_WIDTH

"""
Rectangle Creator:
* GUI to create rectangles
* Extended from QWidget
"""
class RectangleCreator(QWidget):                    
    def __init__(self):
        super().__init__()           
        """ Setup """
        self.setMouseTracking(True)
        self.begin = QPoint()
        self.end = QPoint()
        self.coord_list = []
        self.rect_list = []
        self.clicked = False

    """
    Paint Event
    * Paints Rectangles onto a Pixmap from a list of coordinates
    * Stores created rectangles in a list
    * Rectangle store is cleared and rebuild each iteration
    """ 
    def paintEvent(self, event):
        """Create Pallet"""
        pixmap = QPixmap()
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), pixmap)
        pen = QPen()
        pen.setWidth(PEN_WIDTH)
        pen.setColor(Qt.black)
        painter.setPen(pen)

        """Rebuild rectangle store"""
        self.rect_list.clear() 
        for coord in self.coord_list:
           rec = Rectangle(coord[RECT_A], coord[RECT_B])
           self.rect_list.append(rec)
           painter.drawRect(rec)
        if not self.clicked:
           return
        """Create new rectangle"""   
        rec = Rectangle(self.begin, self.end)
        self.rect_list.append(rec)
        painter.drawRect(rec)

    """
    mousePressEvent
    * Deletes oldest rectangle from the coordinate list
    * Updates begin and end values
    * Tracks click for use in display of rectangles
    """
    def mousePressEvent(self, event):
        """Remove oldest"""
        if len(self.coord_list) > 1:
           self.coord_list.pop(0)
        """Update tracking variables"""   
        self.begin = event.pos()
        self.end = event.pos()
        self.clicked = True
        self.update()

    """
    mouseMoveEvent
    * Updates endpoint
    * Updates Coordinates on display
    """
    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.setWindowTitle('Coordinates: ( x = %d : y = %d )' % (event.x(), event.y()))
        self.update()

    """
    mouseReleaseEvent
    * Checks for position of start and end points of triangle
    * Transforms triangle so start is topleft and end is bottom right
    * Adds triangle coordinates to the coordinates list
    * If two triangles exist:
       *  Runs test for Adjacent, contained and intersection 
    .. TODO:: check that arg2 is non zero. move/cleanup tests
    """
    def mouseReleaseEvent(self, event):
        """Needs horizontal flip?""" 
        if self.begin.x() > self.end.x() and self.begin.y() < self.end.y():
           if len(self.rect_list) == 1:
              self.rect_list[RECT_A] = self.flip_hor(self.rect_list[RECT_A])
           else:
              self.rect_list[RECT_B] = self.flip_hor(self.rect_list[RECT_B])
        """Needs vertical flip?"""
        if self.begin.x() < self.end.x() and self.begin.y() > self.end.y():
           if len(self.rect_list) == 1:
              self.rect_list[RECT_A] = self.flip_ver(self.rect_list[RECT_A])
           else:
              self.rect_list[RECT_B] = self.flip_ver(self.rect_list[RECT_B])
        """Needs refection?"""
        if self.begin.x() > self.end.x() and self.begin.y() > self.end.y():
           if len(self.rect_list) == 1:
              self.rect_list[RECT_A] = self.reflect(self.rect_list[RECT_A])
           else:
              self.rect_list[RECT_B] = self.reflect(self.rect_list[RECT_B])

        self.clicked = False
        self.update()
        """Add new coordinates to the coordinates list"""
        self.coord_list.append([self.begin,self.end])
        
        """Run Tests"""
        if len(self.coord_list) == 2:
           is_adjacent(self.rect_list[RECT_A],self.rect_list[RECT_B],silent=False)
           contained = is_contained(self.rect_list[RECT_A],self.rect_list[RECT_B])
           if not contained:
              contained = is_contained(self.rect_list[RECT_B],self.rect_list[RECT_A])
           if not contained:
              is_intersect(self.rect_list[RECT_A],self.rect_list[RECT_B]) 
        print('------')
  
     
    """
    flip_hor
    * Call rectangle flip_h function 
    * Flip start and end points horizontal
    """
    def flip_hor(self,rect):
        rect.flip_h()
        self.begin = rect.topLeft()
        self.end = rect.bottomRight()
        return rect
    """
    flip_ver
    * Calls rectangle flip_v function and
    * Flip start and end points vertical
    """
    def flip_ver(self,rect):
        rect.flip_v()
        self.begin = rect.topLeft()
        self.end = rect.bottomRight()
        return rect

    """
    reflect
    * Calls flip_hor then flip_ver to produce a reflection of the start and end points
    * Same as above for the input rectangle coordinates
    """
    def reflect(self,rect):
        rect = self.flip_hor(rect)
        rect = self.flip_ver(rect)
        return rect

