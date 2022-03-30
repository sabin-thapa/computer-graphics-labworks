import sys
import time
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

window = 0
width, height = 800, 600


def DDAalgo(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    slope = dy/float(dx)

    x,y = x1, y1

    if dx > dy:
        stepsize = abs(dx)
    else:
        stepsize = abs(dy)
    

    xinc = dx / stepsize
    yinc = dy / stepsize
    
    for i in range(stepsize):
        x += xinc
        y += yinc    
        time.sleep(0.01)
        glVertex2f(x, y)



def lineDDA():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor(1.0, 1.0, 0.0)
    DDAalgo(200, 300, 300, 150)       
    glEnd()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b'line DDA')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 400.0)
    glutDisplayFunc(lineDDA)
    glutIdleFunc(lineDDA)
    glutMainLoop()

main()
