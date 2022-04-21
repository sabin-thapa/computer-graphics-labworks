from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def initialize():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Mid-point Ellipse Drawing Algorithm")

    glClearColor(1.0,1.0,1.0,0.0) 
    gluOrtho2D(-200,200,-200,200)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clears everything previously drawn

    # axes
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(-200,0)
    glVertex2f(200,0)
    glVertex2f(0,200)
    glVertex2f(0,-200)
    glEnd()

'''Display each point '''
def display_point(x,y):    
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

'''Stopping Criteria'''
def stopping_criteria(x,y,rx,ry):
    return (ry*ry*x > rx*rx*y)

def translate_point(x,y,xc,yc):
    display_point(x+ xc, y+yc)

def calc_symmetric_points(x,y,xc,yc):
    translate_point(x,y,xc,yc)
    translate_point(-x,y,xc,yc)
    translate_point(x,-y,xc,yc)
    translate_point(-x,-y,xc,yc)

def ellipse_algo(xc, yc, rx, ry):
    x =0
    y = ry
    pk= ry**2 - rx**2 *ry + (1/4)* rx**2 #decision param
    glColor3f(0.0,1.0,1.0) 
    glPointSize(5.0) 
    calc_symmetric_points(x,y,xc,yc)

    while( not stopping_criteria(x,y,rx,ry)):       
        x+=1
        if(pk<=0):
            calc_symmetric_points(x,y,xc,yc)
            pk=pk + 2* ry**2 *x + ry**2
        else:
            y-=1
            calc_symmetric_points(x,y,xc,yc)
            pk=pk + 2* ry**2 * x + ry**2 - 2* rx**2*y
    x = 0
    y = rx       
    while(not stopping_criteria(x,y,ry,rx)):
        x +=1
        if(pk<0):
            calc_symmetric_points(y,x,xc,yc)
            pk=pk + 2*rx**2*x +rx**2
        else:
            y-=1
            calc_symmetric_points(y,x,xc,yc)
            pk=pk + 2*rx**2*x + rx**2- 2*ry**2*y
    glFlush()

if __name__ == '__main__':   
    center = input("Enter the center of the ellipse as xc,yc: ").split(',')
    xc, yc = int(center[0]), int(center[1])
    radius= input("Enter rx,ry: ").split(',')
    rx, ry = int(radius[0]), int(radius[1])

    initialize()
    glutDisplayFunc(lambda: ellipse_algo(xc,yc,rx,ry)) 
    glutIdleFunc(lambda: ellipse_algo(xc,yc,rx,ry))

    glutMainLoop()
