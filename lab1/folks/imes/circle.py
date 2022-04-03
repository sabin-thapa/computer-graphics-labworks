from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init(): #Initialisation Function
    glClearColor(0.0,0.0,0.0,1.0) #  This is to clear the screen and set a color
    gluOrtho2D(-100,100,-100,100) #  This will set the origin @ bottom-left corner and 100x100 grid.
    
def translate(x,y,xc, yc):
    glColor3f(0.0,1.0,0.0) #  This will set color RGB(1,0,0) which is red
    glPointSize(5.0) #  this will set the point with a specific radius that we give/    
    glBegin(GL_POINTS)
    glVertex2f(x+xc,y+yc)
    glVertex2f(x+xc,-y+yc)
    glVertex2f(-x+xc,y+yc)
    glVertex2f(-x+xc,-y+yc)
    glVertex2f(y+xc,x+yc)
    glVertex2f(y+xc,-x+yc)
    glVertex2f(-y+xc,x+yc)
    glVertex2f(-y+xc,-x+yc)
    glEnd()


def plotCircle(xc,yc,r):
    pk = 1-r
    x = 0
    y = r
    glClear(GL_COLOR_BUFFER_BIT) #  This is to clear everything we previously drawn, if any    
    # axes
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glVertex2f(0,100)
    glVertex2f(0,-100)
    glEnd()

    glColor3f(0.0,1.0,0.0) #  This will set color RGB(1,0,0) which is red
    glPointSize(5.0) #  this will set the point with a specific radius that we give/

    while x<=y :
        if pk <0:
            x +=1
            pk = pk + 2*x + 1
            translate(x,y,xc,yc)
        else:
            x +=1
            y-=1
            pk = pk + 2*x - 2 * y + 1
            translate(x,y,xc,yc)
    glFlush()

def main():
 
    xc = int(input("Enter xc: "))
    yc = int(input("Enter yc: "))
    r = int(input("Enter r: "))
    print("starting window....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Circle Drawing Using Mid Point algorithm")
    glutDisplayFunc(lambda: plotCircle(xc,yc,r)) # Refer for why the use of lambda
    glutIdleFunc(lambda: plotCircle(xc,yc,r))

    init()
    glutMainLoop()

main()