#include <GLUT/glut.h>

void init() {
    glClearColor(0.4f, 0.7f, 1.0f, 1.0f);
    glShadeModel(GL_FLAT);
}

void display(void) {
    glClear(GL_COLOR_BUFFER_BIT);

    // grass
    glColor3f(0.2f, 0.8f, 0.2f); // jasnozielony kolor
    glBegin(GL_POLYGON);
        glVertex2f(-1.0f, -1.0f); // lewy dolny
        glVertex2f(1.0f, -1.0f);  // prawy dolny
        glVertex2f(1.0f, -0.3f);  // prawy górny
        glVertex2f(-1.0f, -0.3f); // lewy górny
    glEnd();

    // baza
    glColor3f(0.9f, 0.8f, 0.6f); // bezowy
    glBegin(GL_QUADS);
        glVertex2f(-0.4f, -0.4f);
        glVertex2f(0.4f, -0.4f);
        glVertex2f(0.4f, 0.2f);
        glVertex2f(-0.4f, 0.2f);
    glEnd();

    // dach
    glColor3f(0.8f, 0.1f, 0.1f); // czerwony
    glBegin(GL_TRIANGLES);
        glVertex2f(-0.5f, 0.2f); // lewo
        glVertex2f(0.5f, 0.2f); // prawo
        glVertex2f(0.0f, 0.6f); // gora
    glEnd();

    // drzwi
    glColor3f(0.4f, 0.2f, 0.0f); // brazowy
    glBegin(GL_QUADS);
        glVertex2f(-0.2f, -0.4f);
        glVertex2f(0.0f, -0.4f);
        glVertex2f(0.0f, -0.05f);
        glVertex2f(-0.2f, -0.05f);
    glEnd();

    // okno
    glColor3f(0.4f, 0.8f, 1.0f);
    glBegin(GL_QUADS);
        glVertex2f(0.1f, -0.1f);
        glVertex2f(0.3f, -0.1f);
        glVertex2f(0.3f, 0.1f);
        glVertex2f(0.1f, 0.1f);
    glEnd();

    // rama okna
    glColor3f(1.0f, 1.0f, 1.0f); // biala rama
    glLineWidth(3.0f);
    glBegin(GL_LINES);
        // pionowo
        glVertex2f(0.2f, -0.1f); 
        glVertex2f(0.2f, 0.1f);
        // poziomo
        glVertex2f(0.1f, 0.0f); 
        glVertex2f(0.3f, 0.0f);
    glEnd();
    glLineWidth(1.0f);

    glFlush();
}

int main(int argc, char *argv[]) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
    glutInitWindowSize(600, 600);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("domek");

    init();
    glutDisplayFunc(display);

    glutMainLoop();
    return 0;
}