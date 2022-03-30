#include<GL/glut.h>
#include<iostream>
#include<math.h>

using namespace std;

#define windowSize 500
#define pie 3.141592

int r = windowSize/3;
int p1x = 0;                // line (0,0) to (r,0)
int p1y = 0;
int p2x = r;
int p2y = 0;
float lx,ly;
int cx = 0;                 // circle center(0,0) radius = windowsize/3
int cy = 0;
int x,y;
int no_section;
int *percentages;

void Setup(void){
	glClearColor(0,0,0,1);
	glColor3f(0,1,1);
}

void showPoint(int x, int y){           //the points are plotted in the range (1,1) to (-1,-1) 
	int scale = windowSize/2;           //so converting it to the scale of the windowSize
	glBegin(GL_POINTS);
		glVertex2f(float(x)/scale,float(y)/scale);
	glEnd();
}

void inputPoints(){
    cout<<"Enter the number of sections in the Pie: "<<endl;
    cin>>no_section;
    percentages = new int(no_section);
	cout<<"Enter the percentages in the Piechart: "<<endl;
    for (x = 0; x < no_section; x++) {
		cin >> percentages[x];
	}
    cout<<"Pieeee!!!"<<endl;
}

float theta(float angle){
    return float(angle)*pie/180;
} 

void Rotate(int xx, int yy){
	int count = 0;
	int p = percentages[count];
    for(float i = 0; i <= 360; i+=.1){
        float xxx = float(xx)*cos(theta(i)) - float(yy)*sin(theta(i));
        float yyy = float(xx)*sin(theta(i)) + float(yy)*cos(theta(i));
		if(float(i)/360*100<p){
			int r = ((count+1)/4)%2;
			int g = ((count+1)/2)%2;
			int b = (count+1)%2;
			glColor3f(r,g,b);
			showPoint(int(xxx),int(yyy));
		} else {
			count++;
			p+=percentages[count];
			showPoint(xxx,yyy);
		}
    }
}

void translate(int x, int y, int tx, int ty){   //translates the points to the given center
	showPoint(x+tx,y+ty);
}

void symmetricPoints(int x, int y){             //Eight point symmetry of the circle
    translate(x,y,cx,cy);
    translate(-x,y,cx,cy);
    translate(x,-y,cx,cy);
    translate(-x,-y,cx,cy);
    translate(y,x,cx,cy);
    translate(-y,x,cx,cy);
    translate(y,-x,cx,cy);
    translate(-y,-x,cx,cy);
}

void Circle(){          // midpoint circle drawing algorithm
    x = 0;
    y = r;
    int pk = 1 - r; 
    symmetricPoints(x,y);
    while(x<y){
        x++;
        if(pk<0){
            symmetricPoints(x,y);
            pk=pk + 2*x + 1;
        } else {
            y--;
            symmetricPoints(x,y);
            pk = pk + 2*(x-y) + 1;
        }
    }

}

void DDA(){					// Digital Differential Analyzer
	int dy = p2y - p1y;
	int dx = p2x - p1x;
	lx=p1x;
	ly=p1y;
	int stepsize;
	
	if (abs(dx)>abs(dy)){
		stepsize = abs(dx);
	}else{
		stepsize = abs(dy);
	}
	float x_inc = float(dx)/stepsize;
	float y_inc = float(dy)/stepsize;
	for(int i=0;i<=stepsize;i++){
		lx+=x_inc;
		ly+=y_inc;
		Rotate(lx,ly);
	}
}

void Draw(void){
	glClear(GL_COLOR_BUFFER_BIT);

	glColor3f(0,1,0);       // circle
    Circle();
    DDA();
    glFlush();
}

int main(int argc, char** argv){
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE);
	glutInitWindowSize(500,500);
	glutInitWindowPosition(100,100);
	glutCreateWindow("Circle Drawing!");
	Setup();
    inputPoints();
	glutDisplayFunc(Draw);
	glutMainLoop();
	return 0;
}




// void Rotate(int *percent, int xx, int yy){
//     for(int i = 0; i <= 10; i++){
//         xx = xx*cos(theta(10)) - yy*sin(theta(10));
//         yy = xx*sin(theta(10)) + yy*cos(theta(10));
//         showPoint(xx,yy);
//     }
// }
