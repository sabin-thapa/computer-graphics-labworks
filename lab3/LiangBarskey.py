from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

''' Clipping window '''
XW_MIN = -200
XW_MAX = 200
YW_MIN = -200
YW_MAX = 200

def draw_window():
    glColor3f(0.0, 0.5, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(XW_MIN,YW_MIN)
    glVertex2f(XW_MAX,YW_MIN)
    glVertex2f(XW_MAX,YW_MAX)
    glVertex2f(XW_MIN,YW_MAX)
    glEnd()

def initialization(): 
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(300, 300)
    glutCreateWindow("Line Clipping - Liang Barsky")
    glClearColor(1.0,1.0,1.0,0.0)  
    gluOrtho2D(-300,300,-300,300)
    glClear(GL_COLOR_BUFFER_BIT) 
    glPointSize(1.0) 

class LiangBarsky:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.draw_line()
        self.line_clipping()

    #initial line - red color
    def draw_line(self): 
        glLineWidth(3)
        glColor3f(1.0, 0.0, 0.0)
        glBegin(GL_LINES)
        glVertex2f(self.x1, self.y1)
        glVertex2f(self.x2, self.y2)
        glEnd()

    def line_clipping(self):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y1
        pks = [-dx, dx, -dy, dy]
        qks = [self.x1 - XW_MIN, XW_MAX - self.x1, self.y1 - YW_MIN, YW_MAX - self.y1]
        u1, u2 = 0, 1

        for (pk, qk) in zip(pks, qks):
        # For all the boudaries
        #if line is parallel to any axes and lies outside
            if pk == 0 and qk<0: 
                return
            if pk == 0: 
                continue
            u = qk / pk
            if pk < 0:
                u1 = max(u1, u)
            else:
                u2 = min(u2, u)
        #line not completely outside
        if u1 <= u2: 
            x1, y1 = self.x1, self.y1
            self.x1 = x1 + u1 * dx
            self.x2 = x1 + u2 * dx
            self.y1 = y1 + u1 * dy
            self.y2 = y1 + u2 * dy

            #green line
            glColor3f(0.0, 1.0, 0.0)
            glLineWidth(3)
            glBegin(GL_LINES)
            glVertex2f(self.x1, self.y1)
            glVertex2f(self.x2, self.y2)
            glEnd()

def line_clipping():
    draw_window()
    line = LiangBarsky(int(line_inputs[0]), int(line_inputs[1]), int(line_inputs[2]), int(line_inputs[3]))
    glFlush()

if __name__ == "__main__":
    line_inputs = input("Enter the line coordinates in the form x1 y1 x2 y2 : ").split(' ')
    initialization()
    glutDisplayFunc(line_clipping)
    glutMainLoop()
    