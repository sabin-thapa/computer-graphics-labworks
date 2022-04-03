from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

'''Stopping Criteria'''
def stop_criteria(x,y):
    return x>y

#plots all the 8 symmetric points for a circle's point
def plot_symmetric_pixels(x,y,x_center,y_center): 
    glColor3f(0.0,1.0,1.0)
    glPointSize(4.0)
    glBegin(GL_POINTS)

    glVertex2f(x+x_center, y+y_center)
    glVertex2f(-x+x_center, y+y_center)
    glVertex2f(x+x_center, -y+y_center)
    glVertex2f(-x+x_center, -y+y_center)
    glVertex2f(y+x_center, x+y_center)
    glVertex2f(y+x_center, -x+y_center)
    glVertex2f(-y+x_center, x+y_center)
    glVertex2f(-y+x_center, -x+y_center)
    glEnd() 

def Circle_Algo(x_center, y_center, r):
    x = 0
    y = r
    pk = 1-r if isinstance(r,int) else 5/4-r  #decision parameter
    
    while not stop_criteria(x, y):
        x=x+1
        if pk<0:
            pk = pk + 2*x + 1
            plot_symmetric_pixels(x,y, x_center, y_center)
        else:
            y=y-1
            pk = pk + 2*x - 2*y + 1
            plot_symmetric_pixels(x,y, x_center, y_center)
    
    glFlush()

def initialize():  
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(300, 300)
    glutCreateWindow("Midpoint Circle Drawing Algorithm")
    
    glClearColor(1.0,1.0,1.0,0.0) 
    gluOrtho2D(-200,200,-200,200)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clears everything previously drawn

    glColor3f(0.0,0.0,1.0) #sets RGB color
    glPointSize(1.0) #sets point size

    glBegin(GL_LINES)
    glVertex2f(-200,0)
    glVertex2f(200,0)
    glVertex2f(0,200)
    glVertex2f(0,-200)
    glEnd()

if __name__ == "__main__":
    center = input("Enter the center coordinate in the form x y: ").split(' ')
    radius = float(input("Enter the radius of the circle: "))
    x_center,y_center = int(center[0]), int(center[1])

    initialize()

    glutDisplayFunc(lambda: Circle_Algo(x_center,y_center,radius))
    glutIdleFunc(lambda: Circle_Algo(x_center,y_center,radius))
    
    glutMainLoop()
    