#include <GLUT/glut.h>
#include <math.h>

void init() {
    glClearColor(0.56f, 0.56f, 0.73f, 1.0f);
    glEnable(GL_DEPTH_TEST);
}

void display(void) {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    glRotatef(20.0f, 1.0f, 0.0f, 0.0f);
    glRotatef(15.0f, 0.0f, 1.0f, 0.0f);

    const GLfloat PI = 3.14f;
    GLfloat r = 0.5f;
    GLfloat y_dol = -0.4f;
    GLfloat y_gora = 0.5f;
    GLfloat krok = (2.0f * PI) / 60.0f;

    // podstawa
    glColor3f(0.0f, 0.0f, 1.0f);
    glBegin(GL_TRIANGLE_FAN);
        glVertex3f(0.0f, y_dol, 0.0f); // środek koła na dole
        for (GLfloat kat = 0.0f; kat <= ceil(2.0f * PI); kat += krok) {
            glVertex3f(cos(kat) * r, y_dol, sin(kat) * r);
        }
 
    glEnd();
    
    // boki stozka
    glColor3f(1.0f, 1.0f, 0.0f);
    glBegin(GL_TRIANGLE_FAN);
    glVertex3f(0.0f, y_gora, 0.0f); // wierzchołek stożka na górze
        for (GLfloat kat = 0.0f; kat <= ceil(2.0f * PI); kat += krok) {
            glVertex3f(cos(kat) * r, y_dol, sin(kat) * r);
        }
    
    glEnd();
    glFlush();
}

int main(int argc, char *argv[]) {
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH);
    glutInitWindowSize(400, 400);
    glutInit(&argc, argv);
    glutCreateWindow("stozek");

    init();
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}