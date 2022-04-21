from _2DTransformation import Transformation
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#fan vertices
vertices = [[0,250,250],
                [0,0, 130],
                [1,1,1]]
image = vertices
rotation = 0
speed = 2

def initialization():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(1000,1000)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Wind Mill Simulation")

    glClearColor(1.0,1.0,1.0,0.0) 
    gluOrtho2D(-500,500,-600,400)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


def timer(x):
    global rotation
    rotation += speed
    glutPostRedisplay()
    glutTimerFunc(round(1000/60), timer, 0)

#keyboard inputs to control rotation
def key_input(char, y, z): 
    global speed
    if char == b'f':
        speed += 1
    elif char == b's':
        speed -= 1

def windmill_simulation():
    global rotation
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(0.5, 0.6, 0.5)
    
    #base
    glBegin(GL_POLYGON)
    glVertex2f(0,5);
    glVertex2f(120,-450);
    # glVertex2f(180,-450);
    # glVertex2f(-180, -450);
    glVertex2f(-120, -450);
    glEnd()

    windmill.Rotate(0+rotation)
    windmill.Rotate(120+rotation)
    windmill.Rotate(240+rotation)

    glFlush()
    glutSwapBuffers();

if __name__ == "__main__":
    initialization()
    windmill = Transformation(vertices, image)
    glutDisplayFunc(windmill_simulation)
    glutTimerFunc(0,timer,0)
    glutKeyboardFunc(key_input)
    glutMainLoop()





