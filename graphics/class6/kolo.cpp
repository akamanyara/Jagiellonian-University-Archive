#include <GLUT/glut.h>
#include <math.h>

void init() {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
}

void display(void) {
    glClear(GL_COLOR_BUFFER_BIT);

    const GLfloat GL_PI = 3.14f;
    GLfloat r = 0.5f; // promień koła
    
    glColor3f(1.0f, 1.0f, 1.0f); 

    glBegin(GL_TRIANGLE_FAN);

        glVertex3f(0.0f, 0.0f, 0.0f); 

        GLfloat krok = (2.0f * GL_PI) / 60.0f;

        for (GLfloat kat = 0.0f; kat <= ceil(2.0f * GL_PI); kat += krok) {
            
            GLfloat x = cos(kat) * r;
            GLfloat y = sin(kat) * r;
            
            glVertex3f(x, y, 0.0f);
        }
        
        glVertex3f(cos(0.0f) * r, sin(0.0f) * r, 0.0f);
        
    glEnd();
    glFlush();
}

int main(int argc, char *argv[]) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    
    glutInitWindowSize(500, 500); 
    glutInitWindowPosition(100, 100);
    glutCreateWindow("kolo");

    init();
    glutDisplayFunc(display);

    glutMainLoop();
    return 0;
}