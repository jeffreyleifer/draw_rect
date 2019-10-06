from PySide2.QtCore import QPoint
from PySide2.QtCore import QLineF
from rectangle import Rectangle

"""
is_adjacent
* Checks for adjacency of two rectangles within
* a certain tolerance
* Silence parameter for use as a helper function
* Adjacency defined as exterior adjacency only
* Interior adjacency viewed not adjacent
.. TODO:: Algorithm explanation
"""
def is_adjacent(rect1,rect2,silent):
    #rect2.refl()        
    r1_tl = rect1.topLeft()
    r1_br = rect1.bottomRight()
    r2_tl = rect2.topLeft()
    r2_br = rect2.bottomRight()
    #rect2.refl()       

    diffleft = r1_tl.x() - r2_tr.x()
    diffright = r1_br.x() - r2_bl.x()
    difftop = r1_tl.y() - r2_tr.y()
    diffbot = r1_br.y() - r2_bl.y()

    adj_list = []     
    if difftop > - 7 and  difftop < 7:
        adj_list.append('top adjacent')
    if diffbot > - 7 and diffbot < 7:
        adj_list.append('bottom adjacent')
    if diffright > - 7  and diffright < 7:
        adj_list.append('right adjacent')
    if diffleft > - 7 and diffleft < 7:
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
.. TODO:: break intersect method and use interect rectangle only
"""
def is_contained(rect1,rect2):
    intersect_rect = is_intersect(rect1,rect2,silent=True)
    if intersect_rect == None:
        return 
    intersect_rect.refl()
    if is_adjacent(rect1,intersect_rect,silent=True):
        return False
    else:
        print('Is contained!')
        return True 

"""
is_intersect
* Checks if rect1 and rect2 intersect 
* If they intersect, uses QLineF containers to determine intersection points
* intersection is defined as filly crossing boundaries of the other
.. TODO:: explain algorithm cleanup and use helpers
.. TODO:: Split up into intersection points and intersection rectangle 
"""

def is_intersect(rect1,rect2,silent):
    r1_tl = rect1.topLeft()
    r1_tr = rect1.topRight()
    r1_br = rect1.bottomRight()
    r1_bl = rect1.bottomLeft()

    r2_tl = rect2.topLeft()
    r2_tr = rect2.topRight()
    r2_br = rect2.bottomRight()
    r2_bl = rect2.bottomLeft()
    
    #TODO Move to external function
    #creates intersection rectangle
    x1 = max(r1_tl.x(),r2_tl.x())
    x2 = min(r1_br.x(),r2_br.x())
    y1 = max(r1_tl.y(),r2_tl.y())
    y2 = min(r1_br.y(),r2_br.y())
     
    found = False
    #if x1 < x2 and y1 <  y2:
    #   if not silent:
    #      print('intersects')
    #   found = True
    #   
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
          if sec_list1[i].intersect(sec_list2[r])[0] == QLineF.IntersectType.BoundedIntersection and not silent:
             print('intersects')
             print(sec_list1[i].intersect(sec_list2[r])[1].x(),sec_list1[i].intersect(sec_list2[r])[1].y())    

    
    if(x1 < x2 and y1 <  y2):      
       return Rectangle(QPoint(x1,y1),QPoint(x2,y2))
    return None
