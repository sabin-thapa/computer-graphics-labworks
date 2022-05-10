from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

''' Window '''
XW_MIN = -200
XW_MAX = 200
YW_MIN = -200
YW_MAX = 200

LEFT = 0
RIGHT = 1
BOTTOM = 2
TOP = 3

IN_TO_IN = 0
IN_TO_OUT = 1
OUT_TO_IN = 2
OUT_TO_OUT = 3

def initialization():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(350, 350)
    glutCreateWindow("Polygon Clipping - Sutherland Hodgeman")
    glClearColor(1.0,1.0,1.0,0.0)  
    gluOrtho2D(-350,350,-350,350)
    glClear(GL_COLOR_BUFFER_BIT) 
    glLineWidth(3)

def draw_window():
    glColor3f(0.0, 0.5, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(XW_MIN,YW_MIN)
    glVertex2f(XW_MAX,YW_MIN)
    glVertex2f(XW_MAX,YW_MAX)
    glVertex2f(XW_MIN,YW_MAX)
    glEnd()

def get_case(boundary, p1, p2):
    (x1,y1) = p1 #tuple unpacking
    (x2,y2) = p2
    if boundary == LEFT: 
        if x1>=XW_MIN and x2>=XW_MIN:
            return IN_TO_IN
        elif x1>=XW_MIN:
            return IN_TO_OUT
        elif x2>=XW_MIN:
            return OUT_TO_IN
        else:
            return OUT_TO_OUT
    elif boundary == RIGHT:
        if x1<=XW_MAX and x2<=XW_MAX:
            return IN_TO_IN
        elif x1<=XW_MAX:
            return IN_TO_OUT
        elif x2<=XW_MAX:
            return OUT_TO_IN
        else:
            return OUT_TO_OUT
    elif boundary == BOTTOM:
        if y1>=YW_MIN and y2>=YW_MIN:
            return IN_TO_IN
        elif y1>=YW_MIN:
            return IN_TO_OUT
        elif y2>=YW_MIN:
            return OUT_TO_IN
        else:
            return OUT_TO_OUT
    elif boundary == TOP:
        if y1<=YW_MAX and y2<=YW_MAX:
            return IN_TO_IN
        elif y1<=YW_MAX:
            return IN_TO_OUT
        elif y2<=YW_MAX:
            return OUT_TO_IN
        else:
            return OUT_TO_OUT

def find_intersection(boundary, p1, p2):
    (x1,y1) = p1
    (x2,y2) = p2
    m=0
    if x1 != x2:
        m = (y2-y1)/(x2-x1)
    if boundary == LEFT:
        return (XW_MIN, y1+m*(XW_MIN-x1))
    elif boundary == RIGHT:
        return (XW_MAX, y1+m*(XW_MAX-x1))
    elif boundary == BOTTOM:
        if x1==x2:
            return (x1,YW_MIN)
        else:
            return (x1+(YW_MIN-y1)/m, YW_MIN)
    elif boundary == TOP:
        if x1==x2:
            return (x1,YW_MAX)
        else:
            return (x1+(YW_MAX-y1)/m, YW_MAX)
    
def polygon_clipper(points):
    for boundary in range(4):
        new_points = []
        for i in range(len(points)):
            p1 = points[i]
            p2 = points[(i+1)%(len(points))]
            
            case = get_case(boundary,p1,p2)
            
            if case == IN_TO_IN:
                new_points.append(p2)
            elif case == IN_TO_OUT:
                p = find_intersection(boundary,p1,p2)
                new_points.append(p)
            elif case == OUT_TO_IN:
                p = find_intersection(boundary,p1,p2)
                new_points.append(p)
                new_points.append(p2)
            
        points = new_points
    return points

def draw_polygon(points):
    for i in range(len(points)):
        (x1,y1) = points[i]
        (x2,y2) = points[(i+1)%len(points)]
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

def SutherlandHodgeman():
    draw_window()
    points = data

    #initial 
    glColor3f(1.0, 0.0, 0.0)
    draw_polygon(points)

    #new 
    new_points = polygon_clipper(points)
    glColor3f(0.0, 1.0, 0.0)
    draw_polygon(new_points)
    glFlush()

if __name__ == "__main__":
    choice = input("Enter the polygon coordinates in the form [(x1, y1), (x2, y2), ...] : \n").strip()[1:-1]
    choice = choice.replace("(", "")
    choice = choice.replace(")", "")
    choice = choice.split(",")
    data = []

    for i in range(0, len(choice), 2):
        data.append((int(choice[i]), int(choice[i+1])))

    initialization()
    glutDisplayFunc(SutherlandHodgeman)
    glutMainLoop()
    
# [(-250, 80),( 50, 250), (170, 80), (100, -250), (-100, -100)]