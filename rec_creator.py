from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from PySide2.QtCore import QPoint
from PySide2.QtWidgets import QWidget, QLabel
from PySide2.QtGui import QPainter
from PySide2.QtGui import QPixmap
from PySide2.QtGui import QPen
from draw_utils import is_adjacent, is_contained, is_intersect
from rectangle import Rectangle


"""
Rectangle Creator:
GUI to create rectangles
Extended from  QWidget
"""

class RectangleCreator(QWidget):                    
    def __init__(self):
        super().__init__()           
        """ Setuup """
        self.setMouseTracking(True)
        self.begin = QPoint()
        self.end = QPoint()
        self.coord_list = []
        self.rect_list = []
        self.clicked = False

    """
    Paint Event
        Paints Rectangles onto a Pixmap
        from a list of coordinates
        stores crated rectangles in a list
        rectangle store is cleared before adding new
        rectangles
    """ 
    def paintEvent(self, event):
        pixmap = QPixmap()
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), pixmap)
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(Qt.black)
        painter.setPen(pen)
        self.rect_list.clear() 
        for rect in self.coord_list:
           rec = Rectangle(rect[0], rect[1])
           self.rect_list.append(rec)
           painter.drawRect(rec)
        if not self.clicked:
           return
        rec = Rectangle(self.begin, self.end)
        self.rect_list.append(rec)
        painter.drawRect(rec)
        #self.update()

    """
      mousePressEvent
         Deletes oldest rectangle from the coordinate list
         Updates begin and end values
         Tracks click for use in display of rectangles
    """
    def mousePressEvent(self, event):
        if(len(self.coord_list) > 1):
           self.coord_list.pop(0)
        self.begin = event.pos()
        self.end = event.pos()
        self.clicked = True
        self.update()

    """
      mouseMoveEvent
        Updates endpoint
        Updates Coordinates on display
    """
    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.setWindowTitle('Coordinates: ( x = %d : y = %d )' % (event.x(), event.y()))
        self.update()

    """
      mouseReleaseEvent
        Checks for position of start and end points of triangle
        Transforms trangle so start is topleft and end is bottom right
        Adds triangle coordinates to the coordinates list
        If two triangles exist:
        Runs test for Adjacent, contained and intersection #TODO move/cleanup tests
    """
    def mouseReleaseEvent(self, event):
  
        if self.begin.x() > self.end.x() and self.begin.y() < self.end.y():
           if len(self.rect_list) == 1:
              self.rect_list[0] = self.flip_hor(self.rect_list[0])
           else:
              self.rect_list[1] = self.flip_hor(self.rect_list[1])

        if self.begin.x() < self.end.x() and self.begin.y() > self.end.y():
           if len(self.rect_list) == 1:
              self.rect_list[0] = self.flip_ver(self.rect_list[0])
           else:
              self.rect_list[1] = self.flip_ver(self.rect_list[1])

        if self.begin.x() > self.end.x() and self.begin.y() > self.end.y():
           if len(self.rect_list) == 1:
              self.rect_list[0] = self.reflect(self.rect_list[0])
           else:
              self.rect_list[1] = self.reflect(self.rect_list[1])

        self.clicked = False
        self.update()
        self.coord_list.append([self.begin,self.end])
        if(len(self.coord_list) == 2):
           is_adjacent(self.rect_list[0],self.rect_list[1],silent=False)
           contained = is_contained(self.rect_list[0],self.rect_list[1])
           if not contained:
              contained = is_contained(self.rect_list[1],self.rect_list[0])
           if not contained:
              is_intersect(self.rect_list[0],self.rect_list[1],silent=False)
  
     
    """
    flip_hor
     Call rectangle flip_h function 
     Flip start and end points horizontal
    """
    def flip_hor(self,rect):
        rect.flip_h()
        self.begin = rect.topLeft()
        self.end = rect.bottomRight()
        return rect
    """
    flip_ver
     Calls rectagle flip_v function and
     Flip start and end points vertical
    """
    def flip_ver(self,rect):
        rect.flip_v()
        self.begin = rect.topLeft()
        self.end = rect.bottomRight()
        return rect

    """
    reflect
       Calls flip_hor then flip_ver to produce a 
       reflection of the start and end points as
       well as the input rectangle coordinates
    """

    def reflect(self,rect):
        rect = self.flip_hor(rect)
        rect = self.flip_ver(rect)
        return rect

