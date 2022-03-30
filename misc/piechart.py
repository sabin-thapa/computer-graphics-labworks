from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def init(): #Initialisation Function
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(-100,100,-100,100)
    
def translate(x,y,xc, yc):
    glColor3f(0.0,1.0,0.0) #  RGB(1,0,0)
    glPointSize(5.0) 
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
    # glClear(GL_COLOR_BUFFER_BIT) #  This is to clear everything we previously drawn, if any
    # glColor3f(0.0,1.0,0.0) #  This will set color RGB(1,0,0) which is red
    glPointSize(5.0) # this will set the point with a specific radius that we give/


    glColor3f(1.0,0.0,0.0) # This will set color RGB(1,0,0) which is red
    glBegin(GL_POINTS) # RE1001 sets point mode

    for step in range(1,steps+1):
        glVertex2f(round(x1),round(y1)) 
        x1 = x1 + Xincrement # update x1 to next X cordinate
        y1 = y1 + Yincrement # update y1 to next Y cordinate
    
    glEnd() # 
    # glFlush() #

def plotCircle(theta):
    # for circles
    xc,yc = 0,0
    r =80
    pk = 1-r
    x = 0
    y = r
    # for lines
    x1,y1 = 80,0
    
    plotLine(0,0,80,0)    

    for i in theta:
        radian = math.pi /180 * i
        x2 =round( x1* math.cos(radian) - y1* math.sin(radian))
        y2 = round(x1* math.sin(radian) + y1*math.cos(radian))
        plotLine(0,0,x1,y1)
        # print(f'{x2},{y2}')
        x1 = x2
        y1= y2     

    glColor3f(0.0,1.0,0.0)
    glPointSize(5.0)

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
    a = True
    theta = []
    while(a):
        thetas = []
        userInput = input("Enter the values of theta seperated by space:")
        userInput = userInput.split()

        for i in userInput:
            thetas.append(int(i))
        if sum(thetas )== 360:
            a= False
            theta = thetas 

    print("starting window....")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Pie Chart")
    
    glutDisplayFunc(lambda: plotCircle(theta)) 
    glutIdleFunc(lambda: plotCircle(theta))
    init()
    glutMainLoop()

main()