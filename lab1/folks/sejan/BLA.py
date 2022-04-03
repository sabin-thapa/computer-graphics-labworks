from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def BLA(x_s, y_s, x_e, y_e):
    dx = x_e - x_s
    dy = y_e - y_s
    x=x_s
    y=y_s

    #swap lesser and greater points 
    if abs(dx)>abs(dy) and x_e < x_s:
        dx = - dx
        dy = - dy
        x = x_e
        x_e = x_s
        x_s = x
        y = y_e
        y_e = y_s
        y_s = y
    elif abs(dy)>=abs(dx) and y_e < y_s:
        dy = - dy
        dx = - dx
        y = y_e
        y_e = y_s
        y_s = y
        x = x_e
        x_e = x_s
        x_s = x

    glPointSize(4.0) #sets point size
    glBegin(GL_POINTS) 
    glColor3f(0.0,1.0,1.0) #sets RGB colour

    glVertex2f(x, y) #starting point

    if abs(dx)>abs(dy): #for |slope| < 1 
        p=2*dy-dx #decision parameter
        for i in range(0, abs(dx)+1):
            x+=1
            if (p>=0):
                y = y+1 if y_s < y_e else y-1
                glVertex2f(x, y)
                p = p+2*dy-2*dx if y_s < y_e else p-2*dy-2*dx
            else:
                glVertex2f(x, y)
                p = p+2*dy if y_s < y_e else p-2*dy
        glEnd()

    else: #for |slope|>1
        p=2*dx-dy
        for i in range(0, abs(dy)+1):
            y+=1
            if (p>=0):
                x = x+1 if x_s < x_e else x-1
                glVertex2f(x, y)
                p = p+2*dx-2*dy if x_s < x_e else p-2*dx-2*dy
            else:
                glVertex2f(x, y)
                p = p+2*dx if x_s < x_e else p-2*dx
        glEnd()

    glFlush()

def setup(): #initialization and setup
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(300, 300)
    glutCreateWindow("Bresenham Line Drawing Algorithm")
    glClearColor(0.0,0.0,0.0,0.0) 
    gluOrtho2D(-100,100,-100,100)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clears everything previously drawn

    #for axes
    glColor3f(1.0,1.0,1.0)
    glPointSize(1.0)
    glBegin(GL_LINES)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glVertex2f(0,100)
    glVertex2f(0,-100)
    glEnd()

if __name__ == "__main__":
    first_coord = input("Enter the start coordinate in the form x1,y1: ").split(',')
    second_coord = input("Enter the end coordinate in the form x2,y2: ").split(',')
    x1,y1 = int(first_coord[0]), int(first_coord[1])
    x2,y2 = int(second_coord[0]), int(second_coord[1])
    setup()
    glutDisplayFunc(lambda: BLA(x1, y1, x2, y2))
    glutIdleFunc(lambda: BLA(x1, y1, x2, y2))
    glutMainLoop()
    