from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def DDA_Algo(x_start, y_start, x_end, y_end):
    dx = x_end - x_start
    dy = y_end - y_start
    
    if abs(dx) > abs(dy):
        stepSize = abs(dx)
    else:
        stepSize = abs(dy)
    
    try:
        x_inc = dx/stepSize
        y_inc = dy/stepSize
    except ZeroDivisionError:
        print("Division by zero!!")

    x = x_start
    y = y_start
    
    glColor3f(0.0,0.0,1.0) #RGB Color
    glPointSize(4.0) #Point Size
    glBegin(GL_POINTS)

    for _ in range(stepSize+1):
        glVertex2f(round(x), round(y))
        x += x_inc
        y += y_inc

    glEnd()
    glFlush()   

def initialize():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(400, 400)
    glutCreateWindow("Digital Differential Analyzer Algorithm")
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

# driver code
if __name__ ==  "__main__":
    start = input("Enter the start co-ordinates in the form x_start y_start:").split(' ')
    end = input("Enter the end co-ordinates in the form x_end y_end:").split(' ')
    x_start,y_start = int(start[0]), int(start[1])
    x_end,y_end = int(end[0]), int(end[1])
    initialize()
    glutDisplayFunc(lambda: DDA_Algo(x_start, y_start, x_end, y_end))
    glutIdleFunc(lambda: DDA_Algo(x_start, y_start, x_end, y_end))
    glutMainLoop()