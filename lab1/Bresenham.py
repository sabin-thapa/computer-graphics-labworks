from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def Bresenham_Algo(x_start, y_start, x_end, y_end):
    dx = x_end - x_start
    dy = y_end - y_start    
    x = x_start
    y = y_start

    if abs(dx) > abs(dy) and x_end < x_start:
        dx, dy = -dx, -dy
        x_end, x_start  = x_start, x_end
        y_end, y_start = y_start, y_end 

    elif abs(dx) <= abs(dy) and y_end <  y_start:
        dy, dx = -dy, -dx
        y_end, y_start = y_start, y_end
        x_end, x_start = x_start, x_end

    glPointSize(4.0) #Point Size
    glBegin(GL_POINTS)
    '''RGB COLOR'''
    glColor3f(0.0,0.0,1.0)
    '''Starting Point'''
    glVertex2f(x, y)

    ''' Case: |slope| < 1'''
    if abs(dx) > abs(dy):
        #decision parameter
        p = 2*dy-dx
        for i in range(0, abs(dx)+1):
            x+=1
            if(p >= 0):
                y = y+1 if y_start < y_end else y-1
                glVertex2f(x, y)
                p = p+2*dy-2*dx if y_start < y_end else p-2*dy-2*dx
            else:
                glVertex2f(x,y)
                p = p+2*dy if y_start < y_end else p-2*dy
        glEnd()

    #Case: |slope| > 1
    else:
        p=2*dx-dy
        for i in range(0, abs(dy)+1):
            y+=1
            if (p>=0):
                x = x+1 if x_start < x_end else x-1
                glVertex2f(x, y)
                p = p+2*dx-2*dy if x_start < x_end else p-2*dx-2*dy
            else:
                glVertex2f(x, y)
                p = p+2*dx if x_start < x_end else p-2*dx
        glEnd()
    
    glFlush()

def initialize():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(300, 300)
    glutCreateWindow("Bresenham Line Drawing Algorithm")
    glClearColor(1.0,1.0,1.0,0.0) 
    gluOrtho2D(-100,100,-100,100)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #to clear everything drawn previously

    #Axes
    glColor3f(0.0,0.0,1.0)
    glPointSize(1.0)
    glBegin(GL_LINES)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glVertex2f(0,100)
    glVertex2f(0,-100)
    glEnd()


if __name__ ==  "__main__":
    start = input("Enter the start co-ordinates in the form x1 y1:").split(' ')
    end = input("Enter the end co-ordinates in the form x2 y2:").split(' ')
    x1,y1 = int(start[0]), int(start[1])
    x2,y2 = int(end[0]), int(end[1])
    initialize()
    glutDisplayFunc(lambda: Bresenham_Algo(x1, y1, x2, y2))
    glutIdleFunc(lambda: Bresenham_Algo(x1, y1, x2, y2))
    glutMainLoop()