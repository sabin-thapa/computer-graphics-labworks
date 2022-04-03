from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def init(): #Initialisation Function
    glClearColor(0.0,0.0,0.0,1.0) 
    gluOrtho2D(-100,100,-100,100) 

def swap(x1,y1,x2,y2):
    temp = x1
    x1 = x2
    x2 = temp
    temp = y1
    y1 = y2
    y2 = temp
    return x1,y1,x2,y2

def plotLine(x1, y1,x2, y2):
    deltaX = x2-x1
    deltaY = y2-y1
    if deltaX !=0:
        slope = float(deltaY) / deltaX
    else:
        slope = math.inf

    glClear(GL_COLOR_BUFFER_BIT)     
    # axes
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)
    glVertex2f(-100,0)
    glVertex2f(100,0)
    glVertex2f(0,100)
    glVertex2f(0,-100)
    glEnd()

    glColor3f(0.0,1.0,0.0) # RGB
    glPointSize(5.0) #

    if slope < 1 and slope >0: 
        # print("condition 1")

        if deltaX < 0:
            # swap start and end points
            x1,y1,x2,y2 = swap(x1,y1,x2,y2)
            deltaX = x2-x1
            deltaY = y2-y1

        pk = 2 * deltaY -deltaX
        glBegin(GL_POINTS)
        while (x1 != x2):
            if pk <0:
                pk = pk + 2 * deltaY
                x1 = x1+1
                glVertex2f(x1, y1)
            else:
                pk = pk + 2 * deltaY - 2*deltaX
                x1 = x1+1
                y1 +=1
                glVertex2f(x1, y1) 
        glEnd()

    elif slope >= 1:
        # print("condition 2")
        if deltaX < 0:
            # swap start and end points
            x1,y1,x2,y2 = swap(x1,y1,x2,y2)
            deltaX = x2-x1
            deltaY = y2-y1

        pk = 2 * deltaX - deltaY
        glBegin(GL_POINTS)
        while (y1 != y2):
            if pk <0:
                pk = pk + 2 * deltaX
                y1 = y1+1
                glVertex2f(x1, y1)
            else:
                pk = pk + 2 * deltaX - 2*deltaY
                x1 = x1+1
                y1 += 1
                glVertex2f(x1, y1) 
        glEnd() 

    if slope > -1 and slope < 0:
        # print("condition 3")
        if deltaX < 0:
            # swap start and end points
            x1,y1,x2,y2 = swap(x1,y1,x2,y2)
            deltaX = x2-x1
            deltaY = y2-y1
            # print('here')
        
        deltaX, deltaY = abs(deltaX), abs(deltaY)
        pk = 2 * deltaY -deltaX
        glBegin(GL_POINTS)      
        pk = 2 * deltaY -deltaX

        while(x1 != x2):
            if pk <0:
                pk = pk + 2 * deltaY
                x1 = x1+1
                glVertex2f(x1, y1)
                # print(f'{x1},{y1}')
            else:
                pk = pk + 2 * deltaY - 2*deltaX
                x1 = x1+1
                y1 -=1
                glVertex2f(x1, y1)
                # print(f'{x1},{y1}')  
        glEnd()

    elif slope <= -1:
        # print("condition 4")
        if deltaX < 0:
            # swap start and end points
            x1,y1,x2,y2 = swap(x1,y1,x2,y2)
            deltaX = x2-x1
            deltaY = y2-y1
            
        pk = 2 * deltaX - deltaY
        deltaX, deltaY = abs(deltaX), abs(deltaY)
        
        glBegin(GL_POINTS)
        while (y1 != y2):
            if pk <0:
                pk = pk + 2 * deltaX
                y1 = y1-1
                glVertex2f(x1, y1)
            else:
                pk = pk + 2 * deltaX - 2*deltaY
                x1 = x1+1
                y1 -= 1
                glVertex2f(x1, y1) 
        glEnd() 

    elif slope == 0:
        if deltaX < 0:
            # swap start and end points
            x1,y1,x2,y2 = swap(x1,y1,x2,y2)                   
        
        glBegin(GL_POINTS)
        while (x1 != x2):
                x1 += 1 
                glVertex2f(x1, y1)            
        glEnd() 
    
    elif slope ==  math.inf:
        if deltaX < 0:
            # swap start and end points
            x1,y1,x2,y2 = swap(x1,y1,x2,y2)                  
        
        glBegin(GL_POINTS)
        while (y1 != y2):
                y1 += 1 
                glVertex2f(x1, y1)            
        glEnd() 

    glFlush() #   

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
    glutCreateWindow("Plot Line using Bresenhams Algorithm")
    glutDisplayFunc(lambda: plotLine(x1,y1,x2,y2)) 
    glutIdleFunc(lambda: plotLine(x1,y1,x2,y2))
    init()
    glutMainLoop()
        
main()



        

    

    





