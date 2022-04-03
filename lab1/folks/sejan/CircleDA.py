from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def stopping_criteria(x,y): #stopping criteria
    return x>y

def plot_all_symmetric_pixels(x,y,xc,yc): #plots all the 8 symmetric points for a circle's point
    glColor3f(0.0,1.0,1.0)
    glPointSize(4.0)
    glBegin(GL_POINTS)

    glVertex2f(x+xc, y+yc)
    glVertex2f(-x+xc, y+yc)
    glVertex2f(x+xc, -y+yc)
    glVertex2f(-x+xc, -y+yc)
    glVertex2f(y+xc, x+yc)
    glVertex2f(y+xc, -x+yc)
    glVertex2f(-y+xc, x+yc)
    glVertex2f(-y+xc, -x+yc)
    glEnd() 

def CircleDA(xc, yc, r):
    x = 0
    y = r
    pk = 1-r if isinstance(r,int) else 5/4-r  #decision parameter
    
    while not stopping_criteria(x, y):
        x=x+1
        if pk<0:
            pk = pk + 2*x + 1
            plot_all_symmetric_pixels(x,y, xc, yc)
        else:
            y=y-1
            pk = pk + 2*x - 2*y + 1
            plot_all_symmetric_pixels(x,y, xc, yc)
    
    glFlush()

def setup():  # initialization and setup
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(300, 300)
    glutCreateWindow("Midpoint Circle Drawing Algorithm")
    
    glClearColor(0.0,0.0,0.0,0.0) 
    gluOrtho2D(-200,200,-200,200)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clears everything previously drawn

    glColor3f(1.0,1.0,1.0) #sets RGB color
    glPointSize(1.0) #sets point size

    glBegin(GL_LINES)
    glVertex2f(-200,0)
    glVertex2f(200,0)
    glVertex2f(0,200)
    glVertex2f(0,-200)
    glEnd()

if __name__ == "__main__":
    center = input("Enter the center coordinate in the form x,y: ").split(',')
    radius = float(input("Enter the radius: "))
    xc,yc = int(center[0]), int(center[1])

    setup()

    glutDisplayFunc(lambda: CircleDA(xc,yc,radius))
    glutIdleFunc(lambda: CircleDA(xc,yc,radius))
    
    glutMainLoop()
    