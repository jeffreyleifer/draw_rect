from PySide2.QtCore import QPoint
from PySide2.QtCore import QLineF
from rectangle import Rectangle
import constants

"""
is_adjacent
* Checks for adjacency of two rectangles within
* a certain tolerance
* Silence parameter for use as a helper function
* Adjacency defined as exterior adjacency only
* Interior adjacency viewed not adjacent
* Algorithm: 
** Get topLeft and BottomRight points of Rectangle A
** Get reflection of topLeft and BottomRight points of Rectangle B
** Compare differences of points against the tolerance
"""
def is_adjacent(rect1,rect2,silent):
    
    r1_tl = rect1.topLeft()
    r1_br = rect1.bottomRight()

    rect2.refl()        
    r2_tl = rect2.topLeft()
    r2_br = rect2.bottomRight()
    rect2.refl()       

    diffleft = r1_tl.x() - r2_tl.x()
    diffright = r1_br.x() - r2_br.x()
    difftop = r1_tl.y() - r2_tl.y()
    diffbot = r1_br.y() - r2_br.y()

    adj_list = []     
    if difftop > - TOLERANCE and  difftop < TOLERANCE:
        adj_list.append('top adjacent')
    if diffbot > - TOLERANCE and diffbot < TOLERANCE:
        adj_list.append('bottom adjacent')
    if diffright > - TOLERANCE  and diffright < TOLERANCE:
        adj_list.append('right adjacent')
    if diffleft > - TOLERANCE and diffleft < TOLERANCE:
        adj_list.append('left adjacent')
    
    if len(adj_list) == 0:
        return False
    else:
        if not silent:
           print(adj_list)
        return True

"""
is_contained
* Calls is_intersect and is_adjacent as helper functions to determain if rect2 is fully within rect1
* Contained is defined as within not touching any boundaries 
* Algorithm:
** Try to generate intersection area rectangle
** If intersection area rectangle exits, check if it has any adjacent sides
** If intersection area rectangle exists and it has no adjacent sides it is contained 
"""
def is_contained(rect1,rect2):
    #intersect_rect = is_intersect(rect1,rect2,silent=True)
    intersect_rect = get_intersection_rectangle
    if intersect_rect == None:
        return False
    intersect_rect.refl()
    if is_adjacent(rect1,intersect_rect,silent=True):
        return False
    else:
        print('Is contained!')
        return True 

"""
is_intersect
* Prints intersection points of rect1 and rect2
* Uses QLineF containers to determine intersection points
* Intersection is defined as a line fully crossing boundaries of the other
* Algorithm:
** Get 4 corners of each rectangle
** Create QLineF object for each side
** Get intersection points 
"""

def is_intersection_points(rect1,rect2):
    r1_tl = rect1.topLeft()
    r1_tr = rect1.topRight()
    r1_br = rect1.bottomRight()
    r1_bl = rect1.bottomLeft()

    r2_tl = rect2.topLeft()
    r2_tr = rect2.topRight()
    r2_br = rect2.bottomRight()
    r2_bl = rect2.bottomLeft()

    sec_list1 = []
    sec_list2 = []

    sec_list1.append(QLineF(r1_tl,r1_bl))
    sec_list1.append(QLineF(r1_tl,r1_tr))
    sec_list1.append(QLineF(r1_tr,r1_br))
    sec_list1.append(QLineF(r1_br,r1_bl))

    sec_list2.append(QLineF(r2_tl,r2_bl))
    sec_list2.append(QLineF(r2_tl,r2_tr))
    sec_list2.append(QLineF(r2_tr,r2_br))
    sec_list2.append(QLineF(r2_br,r2_bl))
    
    for i in range(len(sec_list1)):
       for r in range(len(sec_list2)):
          if sec_list1[i].intersect(sec_list2[r])[0] == QLineF.IntersectType.BoundedIntersection:
             print('intersects')
             print(sec_list1[i].intersect(sec_list2[r])[1].x(),sec_list1[i].intersect(sec_list2[r])[1].y())    


"""
get_intersection_rectangle
* Returns intersection area rectangle of rect1 and rect2 if it exists
* Otherwise returns NoneType
* Algorithm:
** Get TopLeft & bottomRight of both rectangles
** Get max of topLeft's and min of bottomRight's
** Max's produce topLeft of intersection area rectangle
** Min's produce bottomRight of intersection area rectangle
"""
def get_intersection_rectangle(rect1,rect2)
    
    r1_tl = rect1.topLeft()
    r1_br = rect1.bottomRight()

    r2_tl = rect2.topLeft()
    r2_br = rect2.bottomRight()

    x1 = max(r1_tl.x(),r2_tl.x())
    y1 = max(r1_tl.y(),r2_tl.y())

    x2 = min(r1_br.x(),r2_br.x())
    y2 = min(r1_br.y(),r2_br.y())
    
    if(x1 < x2 and y1 <  y2):      
       return Rectangle(QPoint(x1,y1),QPoint(x2,y2))
    return None