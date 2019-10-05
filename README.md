# Draw Rect Exercise
Jeffrey Leifer 2019-10-05 v1  [License](LICENSE.md)

TODO Cleanup rect_creator, make some more helpers in rectangle class
     make unit tests
     Better document inline functions

### Table of Contents:
##### [-Overview-](#overview)
##### [-Build-](#build)
##### [-Usage-](#usage)
##### [-Files-](#files)


## Overview
---
- [Qt for Python](https://www.qt.io/qt-for-python) based GUI draw two rectangles. Includes supporting code to determine the following
   -  Is Adjacent
       - Does the two rectangles share a common side
      - Is conditional that one rectangle is not inside the other
   -  Is Contained
      - One Rectangle is fully within the other
  -  Intersection
      - Do any of the sides for the two rectangles intersect.
      - What are the intersection points
     
  - Mouse tracking displays the xy position of the mouse on the wider header 

## Build 
---
### python3 and install PySide2
- Running of the software requires Python3 and the PySide2 module 
- Below is the install process using Anaconda3 on a CentOS Linux operating system
```
#Download anaconda3
   wget https://repo.anaconda.com/archive/Anaconda3-2019.07-Linux-x86_64.sh
#Make install script executable 
   chmod a+x Anaconda3-2019.03-Linux-x86_64.sh
#Run install script using defaults
   ./Anaconda3-2019.03-Linux-x86_64.sh
#Add conda-forge channels
   conda config --add channels conda-forge
#Create enviorment (optional)
   conda create --name draw_rect
   conda activate draw_rect
#Install PySide2
   conda install pyside2 
````

## Usage
---
 To run the GUI 
 ```
 cd draw_rect/
 python main.py
 ```
 - Draw rectangles using the mouse and holding the left mouse button
 - Only two rectangles can be drawn at one time.
    - Once a new rectangle is created, the oldest rectangle is destroyed
 TODO Screenshots here for:
-Adjacent
-Contained
-Intersection

## Files
---
##### main.py
  - Driver for GUI
  - Create RectangleCreator object
##### rect_creator.py
  - Qt based GUI to draw rectangles
  - Creates Rectangle objects
  - Runs isAdjacent, isContained and isIntersect draw_utils routines
##### draw_utils.py
  - Routines to check if two rectangles are:
    - Adjacent
    - Contained
    - Intersect
##### rectangle.py
 - Rectangle object extend from the QRect object
 - Helper functions to change rectangle orientation and get rectangle characteristics

