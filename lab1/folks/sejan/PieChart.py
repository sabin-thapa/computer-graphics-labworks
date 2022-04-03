from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
from CircleDA import CircleDA
import random

def radian(angle_in_degrees): #caclulates radian for degrees
    return - math.pi /180 * angle_in_degrees

def plot_lines(x1, y1, x2, y2): #plots line with openGL function
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()

def draw(thetas):
    CircleDA(0, 0, 120) #midpoint circle drawing
    x1 = 0
    y1 = 120
    angle = 0
    for i, theta in enumerate(thetas): # for each theta in input, plots lines
        for j in range(angle, angle+theta): #plots lines from previous angle to the next angle
            k=0
            while k<1: #plots line at interval of 0.1
                radian_val = radian(j+k)
                #finding point on circle from the degree
                x = round(x1* math.cos(radian_val) - y1* math.sin(radian_val)) 
                y = round(x1* math.sin(radian_val) + y1* math.cos(radian_val))
                #random RGB value generation
                r = (i+1)%2
                g = (i/2)%2
                b = (i/4)%2
                glColor3f(r,g,b)
                plot_lines(0,0,x,y)
                k+=0.1

        angle += theta

def setup(): # initialization and setup
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(300, 300)
    glutCreateWindow("PieChart")
    glClearColor(0.0,0.0,0.0,0.0) 
    gluOrtho2D(-200,200,-200,200)
    glPointSize(4.0) #sets point size
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #clears everything previously drawn

if __name__ == "__main__":
    input_theta = True
    thetas = []
    while(input_theta): #take angle inputs from the user
        userInput = input("Enter the values of theta degrees in pie charts separated by space: ")
        userInput = userInput.split()

        for i in userInput:
            thetas.append(int(i))
        
        if sum(thetas) > 360:
            input_theta = False
            print("Sum of angles exceeded 360 degrees. So, the input is wrong.")
        else:
            setup()
            glutDisplayFunc(lambda: draw(thetas))
            glutIdleFunc(lambda: draw(thetas))
            glutMainLoop()

