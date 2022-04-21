from transformation2D import Transformation
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

fan_vertices = [[0,250,250],
                [0,0, 130],
                [1,1,1]]
image = fan_vertices
rotation = 0
speed = 2

def screen_setup():  # initialization and setup
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Wind Mill")
    gluOrtho2D(-500,500,-600,400)
    glClearColor(0.0,0.0,0.0,0.0) 
    glClear(GL_COLOR_BUFFER_BIT) #clears everything previously drawn

def timer(x):
    global rotation
    rotation += speed
    glutPostRedisplay()
    glutTimerFunc(round(1000/60), timer, 0)

def key_input(char, y, z): #to control the rotation speed
    global speed
    if char == b'w':
        speed += 1
    elif char == b's':
        speed -= 1

def windMill():
    global rotation
    glClear(GL_COLOR_BUFFER_BIT);
    glColor3f(1.0, 0.6, 1)
    
    #base
    glBegin(GL_POLYGON)
    glVertex2f(0,5);
    glVertex2f(140,-80);
    glVertex2f(180,-450);
    glVertex2f(-180, -450);
    glVertex2f(-140, -80);
    glEnd()

    #baseDoor
    glColor3f(1, 0.4, 0.4)
    glBegin(GL_POLYGON)
    glVertex2f(-30,-450);
    glVertex2f(30,-450);
    glVertex2f(30,-300);
    glVertex2f(-30,-300);
    glEnd()

    #baseWindow
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_POLYGON)
    glVertex2f(70,-120);
    glVertex2f(70,-160);
    glVertex2f(30,-160);
    glVertex2f(30,-120);
    glEnd()

    windmill = Transformation(fan_vertices, image)
    glColor3f(0.6, 1.0, 0.6)
    windmill.rotate(0+rotation)
    windmill.rotate(120+rotation)
    windmill.rotate(240+rotation)

    glFlush()
    glutSwapBuffers();

if __name__ == "__main__":
    screen_setup()    
    glutDisplayFunc(windMill)
    glutTimerFunc(0,timer,0)
    glutKeyboardFunc(key_input)
    glutMainLoop()





