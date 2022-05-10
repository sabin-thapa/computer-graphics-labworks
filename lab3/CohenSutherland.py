from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
''' Clippping Window '''
XW_MIN = -200
XW_MAX = 200
YW_MIN = -200
YW_MAX = 200

''' Region Codes '''
INSIDE = 0  #0000 
LEFT = 1    #0001 
RIGHT = 2   #0010 
BOTTOM = 4  #0100 
TOP = 8     #1000
def draw_window(): 
    glColor3f(0.0, 0.5, 1.0)
    glLineWidth(3)
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
    glutCreateWindow("Line Clipping - Cohen Sutherland")
    glClearColor(1.0,1.0,1.0,0.0)  
    gluOrtho2D(-300,300,-300,300)
    glClear(GL_COLOR_BUFFER_BIT) 
    glPointSize(1.0) 

class Cohen_Sutherland:
    def __init__(self, x1, y1, x2, y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.draw_line()
        self.line_clipping()

    #initial line - red 
    def draw_line(self): 
        glLineWidth(3)
        glColor3f(1.0, 0.0, 0.0) 
        glBegin(GL_LINES)
        glVertex2f(self.x1, self.y1)
        glVertex2f(self.x2, self.y2)
        glEnd()
    #computes TBRL code for the endpoint
    def compute_code(self, x, y): 
        code = INSIDE 
        if x < XW_MIN:
            code |= LEFT 
        elif x > XW_MAX:
            code |= RIGHT 
        if y < YW_MIN:
            code |= BOTTOM 
        elif y > YW_MAX:
            code |= TOP 
        return code

    def line_clipping(self):
        region_code_1 = self.compute_code(self.x1, self.y1)
        region_code_2 = self.compute_code(self.x2, self.y2)
        partially_inside = False

        while True:
            #Line completely inside
            if region_code_1 == 0 and region_code_2 == 0: 
                partially_inside = True
                break
            #Line completely outside
            elif (region_code_1 & region_code_2)!=0: 
                break
            #Line needs clipping
            else: 
                x = 1.0
                y = 1.0
                if region_code_1 != 0: 
                    code_to_clip = region_code_1 
                else: 
                    code_to_clip = region_code_2 
                
                #finding intersection points
                if code_to_clip & TOP: 
                    x = self.x1 + ((self.x2 - self.x1) / (self.y2 - self.y1)) * (YW_MAX - self.y1) 
                    y = YW_MAX 
                elif code_to_clip & BOTTOM: 
                    x = self.x1 + ((self.x2 - self.x1) / (self.y2 - self.y1)) * (YW_MIN - self.y1) 
                    y = YW_MIN 
                elif code_to_clip & RIGHT: 
                    y = self.y1 + ((self.y2 - self.y1) / (self.x2 - self.x1)) * (XW_MAX - self.x1) 
                    x = XW_MAX 
                elif code_to_clip & LEFT: 
                    y = self.y1 + ((self.y2 - self.y1) / (self.x2 - self.x1)) * (XW_MIN - self.x1)  
                    x = XW_MIN

                # replacing outside points with calculated intersection points
                if code_to_clip == region_code_1: 
                    self.x1 = x 
                    self.y1 = y 
                    region_code_1 = self.compute_code(self.x1, self.y1) 
                else: 
                    self.x2 = x 
                    self.y2 = y 
                    region_code_2 = self.compute_code(self.x2, self.y2) 

        if partially_inside: 
            #draw line in green
            glColor3f(0.0, 1.0, 0.0)
            glLineWidth(3)
            glBegin(GL_LINES)
            glVertex2f(self.x1, self.y1)
            glVertex2f(self.x2, self.y2)
            glEnd()

def LineClipping():
    draw_window()
    line = Cohen_Sutherland(int(line_inputs[0]), int(line_inputs[1]), int(line_inputs[2]), int(line_inputs[3]))
    glFlush()

if __name__ == "__main__":
    line_inputs = input("Enter the line coordinates in the form x1 y1 x2 y2 : ").split(' ')
    initialization()
    glutDisplayFunc(LineClipping)
    glutMainLoop()
