from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

def initialization():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600,600)
    glutInitWindowPosition(300,300)
    glutCreateWindow("Transformations - 2D Square")

    glClearColor(1.0,1.0,1.0,0.0) 
    gluOrtho2D(-300,300,-300,300)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # axes
    glColor3f(0.0,0.0,1.0)
    glBegin(GL_LINES)
    glVertex2f(-300,0)
    glVertex2f(300,0)
    glVertex2f(0,300)
    glVertex2f(0,-300)
    glEnd()

vertices = [[20,20,120, 120], 
            [20,120,120,20], 
            [1,1,1,1]]

image = vertices

class Transformation:
    def __init__(self, vertices, image):
        self.vertices = vertices
        self.image = image

    ''' Draw square'''
    def draw_shape(self):
        glBegin(GL_POLYGON)
        for i in range(len(self.image[0])):
            glVertex2f(self.image[0][i], self.image[1][i])
        glEnd() 

    ''' Matrix multiplication '''
    def matrix_multiply(self, transformer):
        mult = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*self.vertices)] for X_row in transformer]
        self.image = mult
        return

    '''Rotation'''
    def Rotate(self,angle):
        theta = angle*math.pi/180
        transformer= [[math.cos(theta), -math.sin(theta), 0],
                    [math.sin(theta), math.cos(theta), 0],
                    [0,0,1]]
        self.matrix_multiply(transformer)
        self.draw_shape()

    '''Translation'''
    def Translate(self,tx,ty):
        transformer= [[1,0,tx],
                    [0,1,ty],
                    [0,0,1]]
        self.matrix_multiply(transformer)
        self.draw_shape()
        
    '''Scaling'''
    def Scale(self,sx,sy):
        transformer= [[sx,0,0],
                    [0,sy,0],
                    [0,0,1]]
        self.matrix_multiply(transformer)
        self.draw_shape()

    '''Reflection X-axis'''
    def ReflectX(self):
        transformer= [[1,0,0],
                    [0,-1,0],
                    [0,0,1]]
        self.matrix_multiply(transformer)
        self.draw_shape()

    '''Reflection Y-axis'''
    def ReflectY(self):
        transformer= [[-1,0,0],
                    [0,1,0],
                    [0,0,1]]
        self.matrix_multiply(transformer)
        self.draw_shape()

    
    '''Shearing'''
    def Shear(self,shx, shy):
        transformer= [[1,shx,0],
                    [shy,1,0],
                    [0,0,1]]
        self.matrix_multiply(transformer)
        self.draw_shape()
        
def Transformations():
    glColor3f(0, 0, 1)
    t.draw_shape() #draws original square

    glColor3f(0.5, 0.5 , 1)

    if userInput == 1:
        #Translation by -200 units on x-axis
        t.Translate(-200, 0) 
    
    elif userInput == 2:
        #Rotation by 30 degrees anticlockwise
        t.Rotate(30) 

    elif userInput == 3:
        #Scaling by 2 units
        t.Scale(2,2) 
    
    elif userInput == 4:
        t.ReflectY()
    
    elif userInput == 5:
        # x axis shear by 0,7
        t.Shear(0.7,0) 

    glFlush()
    glutSwapBuffers();

if __name__ == "__main__":
    t = Transformation(vertices, image)
    global userInput
    userInput = int(input("Enter 1 for Translation, 2 for Rotation, 3 for Scaling, 4 for reflection, 5 for Shearing: "))
    initialization()
    glutDisplayFunc(Transformations)
    glutMainLoop()