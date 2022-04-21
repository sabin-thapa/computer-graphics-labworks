from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(-100,100,-100,100) 


def displayPoint(x,y):    
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def stopping_criteria(x,y,rx,ry):
    return (ry*ry*x > rx*rx*y)

def translatePoint(x,y,xc,yc):
    displayPoint(x+ xc, y+yc)

def symmetricPoints(x,y,xc,yc):
    translatePoint(x,y,xc,yc)
    translatePoint(-x,y,xc,yc)
    translatePoint(x,-y,xc,yc)
    translatePoint(-x,-y,xc,yc)



def plotEllipse(xc, yc, rx, ry):
    glClear(GL_COLOR_BUFFER_BIT) 
    # axes
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glVertex2f(0,100)
    glVertex2f(0,-100)
    glEnd()

    x =0
    y = ry
    pk= ry**2 - rx**2 *ry + (1/4)* rx**2
    glColor3f(0.0,1.0,0.0) 
    glPointSize(5.0) 
    symmetricPoints(x,y,xc,yc)

    while( not stopping_criteria(x,y,rx,ry)):       
        x+=1
        if(pk<=0):
            symmetricPoints(x,y,xc,yc)
            pk=pk + 2* ry**2 *x + ry**2
        else:
            y-=1
            symmetricPoints(x,y,xc,yc)
            pk=pk + 2* ry**2 * x + ry**2 - 2* rx**2*y

    x = 0
    y = rx       
    while(not stopping_criteria(x,y,ry,rx)):
        x +=1
        if(pk<0):
            symmetricPoints(y,x,xc,yc)
            pk=pk + 2*rx**2*x +rx**2
        else:
            y-=1
            symmetricPoints(y,x,xc,yc)
            pk=pk + 2*rx**2*x + rx**2- 2*ry**2*y
    glFlush()
  

def main():     
    xc = int(input("Enter xc: "))
    yc = int(input("Enter yc: "))
    rx = int(input("Enter rx: "))
    ry = int(input("Enter ry: "))
    print("starting window....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Ellipse Drawing Using Mid Point algorithm")
    glutDisplayFunc(lambda: plotEllipse(xc,yc,rx,ry)) # Refer for why the use of lambda
    glutIdleFunc(lambda: plotEllipse(xc,yc,rx,ry))

    init()
    glutMainLoop()

main()