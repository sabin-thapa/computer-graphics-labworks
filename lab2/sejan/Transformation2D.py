from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

vertices = [[20,20,120, 120], 
            [20,120,120,20], 
            [1,1,1,1]]

image = vertices

class Transformation:
    def __init__(self, vertices, image):
        self.vertices = vertices
        self.image = image

    # draws/ renders the images
    def draw_shape(self):
        glBegin(GL_POLYGON)
        for i in range(len(self.image[0])):
            glVertex2f(self.image[0][i], self.image[1][i])
        glEnd() 

    #for matrix multiplication
    def matrix_multiply(self, transformer):
        result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*self.vertices)] for X_row in transformer]
        self.image = result
        return

    #rotation
    def Rotate(self,angle):
        theta = angle*math.pi/180
        transformer= [[math.cos(theta), -math.sin(theta), 0],
                    [math.sin(theta), math.cos(theta), 0],
                    [0,0,1]]
        self.matrix_multiply(transformer)
        self.draw_shape()

    #translation
    def Translate(self,tx,ty):
        transformer= [[1,0,tx],
                    [0,1,ty],
                    [0,0,1]]
        self.matrix_multiply(transformer)
        self.draw_shape()
        
    #scaling
    def Scale(self,sx,sy):
        transformer= [[sx,0,0],
                    [0,sy,0],
                    [0,0,1]]
        self.matrix_multiply(transformer)
        self.draw_shape()

    #reflection across x-axis
    def ReflectX(self):
        transformer= [[1,0,0],
                    [0,-1,0],
                    [0,0,1]]
        self.matrix_multiply(transformer)
        self.draw_shape()

    #reflection across y-axis
    def ReflectY(self):
        transformer= [[-1,0,0],
                    [0,1,0],
                    [0,0,1]]
        self.matrix_multiply(transformer)
        self.draw_shape()

    #shearing
    def Shear(self,shx, shy):
        transformer= [[1,shx,0],
                    [shy,1,0],
                    [0,0,1]]
        self.matrix_multiply(transformer)
        self.draw_shape()
        
def Transformations():
    glColor3f(1.0, 1.0, 1.0)
    t.draw_shape() #draws original square

    glColor3f(0.4, 0.4, 0.4)
    # t.ReflectY() #reflection on y axis
    # t.ReflectX() #reflection on x axis
    # t.Translate(-200, 0) #Translation by -200 units on x-axis
    # t.Translate(-150, -150) #Translation by 50 units on x-axis and 100 units on y-axis
    # t.Shear(0.7,0) #Shearing by 0.7 on x-axis
    # t.Shear(0,1.4) #Shearing by 0.7 on x-axis
    t.Rotate(30) #Rotation by 30 degrees antoclockwise
    # t.Scale(2,2) #Scaling by 2 units
    # t.Scale(0.5,2) #Scaling by 0.5 units on x-axis and 2 units on y-axis

    glFlush()
    glutSwapBuffers();

def screen_setup():  # initialization and setup
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(300, 300)
    glutCreateWindow("2D Transformations")
    glClearColor(0.0,0.0,0.0,0.0) 
    gluOrtho2D(-300,300,-300,300)
    glClear(GL_COLOR_BUFFER_BIT) #clears everything previously drawn
    glColor3f(1.0,1.0,1.0) #sets RGB color
    glPointSize(1.0) #sets point size

    #axes
    glBegin(GL_LINES)
    glVertex2f(-300,0)
    glVertex2f(300,0)
    glVertex2f(0,300)
    glVertex2f(0,-300)
    glEnd()

if __name__ == "__main__":
    t = Transformation(vertices, image)
    screen_setup()
    glutDisplayFunc(Transformations)
    glutMainLoop()