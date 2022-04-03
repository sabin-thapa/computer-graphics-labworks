from Circle import Circle_Algo
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

def plot_lines(x1, y1, x2, y2):
    glLineWidth(3.0)
    glBegin(GL_LINES)
    glVertex2f(x1,y1)
    glVertex2f(x2,y2)
    glEnd()

def convert_to_radian(angle_in_degrees): 
    return - math.pi /180 * angle_in_degrees

def draw_pie_chart(theta_values):
    '''Using Midpoint Circle Algo to draw the Circle'''
    Circle_Algo(0, 0, 150) 
    x1 = 0
    y1 = 150
    angle = 0
    # Plot lines for each theta in the input
    for i, theta in enumerate(theta_values):
        #Plot lines from previous angle to the next angle
        for j in range(angle, angle+theta): 
            k=0
            # Plot lines at every 0.1 interval
            while k<1: 
                radian_val = convert_to_radian(j+k)
                # Use the degree to find the coordinates on the circle
                x = round(x1* math.cos(radian_val) - y1* math.sin(radian_val)) 
                y = round(x1* math.sin(radian_val) + y1* math.cos(radian_val))
                # Generate random RGB color to fill the pie chart sections
                r = ((i+1)/4)%2
                g = ((i+1)/2)%2
                b = (i+1)%2
                glColor3f(r,g,b)
                plot_lines(0,0,x,y)
                k+=0.1

        angle += theta

def initialize():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(300, 300)
    glutCreateWindow("PieChart")
    glClearColor(1.0,1.0,1.0,0.0) 
    gluOrtho2D(-200,200,-200,200)
    glPointSize(4.0) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 

if __name__ == "__main__":
    accept_input = True
    theta_values = []

    '''Take theta angles as inputs from the user to create a pie chart'''
    while(accept_input):
        inputs = input("Enter the values of theta degrees in pie charts separated by space: ").split(' ')

        for inp in inputs:
            theta_values.append(int(inp))
        
        #Stop if the theta values exceed 360
        if sum(theta_values) > 360:
            accept_input = False
            print("Sum of angles exceeded 360 degrees.")
        else:
            initialize()
            glutDisplayFunc(lambda: draw_pie_chart(theta_values))
            glutIdleFunc(lambda: draw_pie_chart(theta_values))
            glutMainLoop()

