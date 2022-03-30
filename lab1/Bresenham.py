from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time

window = 0
width, height = 800,600

def Bresenham_Algo(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    i1 = 2*dy
    i2 = 2*(dy-dx)
    d = i1 - dx

    if (dx < 0):
        x = x2
        y = y2
        x_end = x1

    if (dx > 0):
        x = x1
        y = y1
        x_end = x2
        

    if abs(dx) > abs(dy):
        stepSize = abs(dx)
    else:
        stepSize = abs(dy)
    
    xinc = dx/stepSize
    yinc = dy/stepSize

    x = x1
    y = y1
    # print(x, y)

    for _ in range(stepSize):
        x += xinc
        y += yinc
        time.sleep(0.01)

        glVertex2f(round(x), round(y))


def lineBresenham():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glBegin(GL_POINTS)
    glColor(1.0, 1.0, 0.0)

    Bresenham_Algo(50, 50, 350, 350)
        
    glEnd()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE|GLUT_ALPHA|GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0,0)
    glutCreateWindow(b'DDA Line')
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(0.0, 500.0, 0.0, 400.0)
    glutDisplayFunc(lineBresenham)
    glutIdleFunc(lineBresenham)
    glutMainLoop()

main()