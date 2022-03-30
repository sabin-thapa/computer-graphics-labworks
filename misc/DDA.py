# First Import necessary dependencies
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init(): #Initialisation Function
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(-100,100,-100,100) # This will set the origin @ bottom-left corner and 100x100 grid.
    
def plotLine(x1,y1,x2,y2):    
    deltaX = x2-x1
    deltaY = y2-y1
    # 2. Calculate Steps. 
    steps = 0
    if(abs(deltaX)>abs(deltaY)):
        steps = abs(deltaX)
    else:
        steps = abs(deltaY)
    # 3. Calculate X & Y increment.
    Xincrement = deltaX/steps
    Yincrement = deltaY/steps
    glClear(GL_COLOR_BUFFER_BIT) #  This is to clear everything we previously drawn, if any
    glColor3f(0.0,1.0,0.0) #  This will set color RGB(1,0,0) which is red
    glPointSize(5.0) # this will set the point with a specific radius that we give/
# axes
    glBegin(GL_LINES)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glVertex2f(0,100)
    glVertex2f(0,-100)
    glEnd()

    glColor3f(1.0,0.0,0.0) # This will set color RGB(1,0,0) which is red
    glBegin(GL_POINTS) # RE1001 sets point mode

    for step in range(1,steps+1):
        glVertex2f(round(x1),round(y1)) 
        x1 = x1 + Xincrement # update x1 to next X cordinate
        y1 = y1 + Yincrement # update y1 to next Y cordinate
    
    glEnd() # 
    glFlush() #
        
# driver function
def main():
    
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    x2 = int(input("Enter x2: "))
    y2 = int(input("Enter y2: "))
    print("starting window....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Line Drawing Using DDA")
    glutDisplayFunc(lambda: plotLine(x1,y1,x2,y2)) 
    glutIdleFunc(lambda: plotLine(x1,y1,x2,y2))

    init()
    glutMainLoop()
        
main()

