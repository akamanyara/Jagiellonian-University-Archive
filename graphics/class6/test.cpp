#include <GLUT/glut.h>

void init() {
    glClearColor(0.56f, 0.56f, 0.73f, 0.0f); // Tło zbliżone do Twojego kodu
}

void display(void) {
    glClear(GL_COLOR_BUFFER_BIT);

    glColor3f(1.0f, 1.0f, 0.0f); // Żółty kolor
    glBegin(GL_POLYGON);
        glVertex3f(0.0f, 0.0f, 0.0f);
        glVertex3f(0.75f, 0.0f, 0.0f);
        glVertex3f(0.75f, 0.5f, 0.0f);
        glVertex3f(0.0f, 0.5f, 0.0f);
    glEnd();

    glFlush();
}

int main(int argc, char *argv[]) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB);
    glutInitWindowSize(400, 400);
    glutInitWindowPosition(200, 200);
    
    glutCreateWindow("window opengl");

    init();
    glutDisplayFunc(display);

    glutMainLoop();
    return 0;
}


// Compile with:
// g++ test.cpp -o test -framework OpenGL -framework GLUT -Wno-deprecated