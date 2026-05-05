#include <GLUT/glut.h>

float angleX = 20.0f;
float angleY = 20.0f;

void init() {
    glClearColor(0.560784, 0.560784, 0.737255, 0.0);
    glEnable(GL_DEPTH_TEST);
}

void display(void) {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    glRotatef(angleX, 1.0f, 0.0f, 0.0f);
    glRotatef(angleY, 0.0f, 1.0f, 0.0f);

    // wypełnione przednie ściany, tylne jako linie
    glPolygonMode(GL_FRONT, GL_FILL);
    glPolygonMode(GL_BACK, GL_LINE);

    glBegin(GL_QUADS); //
        // Ściana przednia - czerwona
        glColor3f(1.0f, 0.0f, 0.0f);
        glVertex3f(-0.6f, -0.6f, 0.6f);
        glVertex3f(0.6f, -0.6f, 0.6f);
        glVertex3f(0.6f, 0.6f, 0.6f);
        glVertex3f(-0.6f, 0.6f, 0.6f);

        // Ściana tylna - zielona
        glColor3f(0.0f, 1.0f, 0.0f);
        glVertex3f(-0.6f, 0.6f, -0.6f);
        glVertex3f(0.6f, 0.6f, -0.6f);
        glVertex3f(0.6f, -0.6f, -0.6f);
        glVertex3f(-0.6f, -0.6f, -0.6f);

        // Ściana lewa - niebieska
        glColor3f(0.0f, 0.0f, 1.0f);
        glVertex3f(-0.6f, -0.6f, -0.6f);
        glVertex3f(-0.6f, -0.6f, 0.6f);
        glVertex3f(-0.6f, 0.6f, 0.6f);
        glVertex3f(-0.6f, 0.6f, -0.6f);

        // Ściana prawa - żółta
        glColor3f(1.0f, 1.0f, 0.0f);
        glVertex3f(0.6f, 0.6f, -0.6f);
        glVertex3f(0.6f, 0.6f, 0.6f);
        glVertex3f(0.6f, -0.6f, 0.6f);
        glVertex3f(0.6f, -0.6f, -0.6f);

        // Ściana dolna - magenta
        glColor3f(1.0f, 0.0f, 0.6f);
        glVertex3f(-0.6f, -0.6f, 0.6f);
        glVertex3f(-0.6f, -0.6f, -0.6f);
        glVertex3f(0.6f, -0.6f, -0.6f);
        glVertex3f(0.6f, -0.6f, 0.6f);

        // dodana gorna sciana
        glColor3f(0.0f, 1.0f, 1.0f);
        glVertex3f(-0.6f, 0.6f, 0.6f);
        glVertex3f(0.6f, 0.6f, 0.6f);
        glVertex3f(0.6f, 0.6f, -0.6f);
        glVertex3f(-0.6f, 0.6f, -0.6f);
    glEnd();

    glFlush();
}

void keyboard(unsigned char key, int x, int y) {
    if (key == 'w') angleX += 5.0f;
    if (key == 's') angleX -= 5.0f;
    if (key == 'a') angleY -= 5.0f;
    if (key == 'd') angleY += 5.0f;
    glutPostRedisplay(); // Odśwież obraz po naciśnięciu klawisza
}

int main(int argc, char *argv[]) {
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH);
    glutInitWindowSize(400, 400);
    glutInit(&argc, argv);
    glutCreateWindow("Zadanie: Szescian Final");

    init();
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard); // Rejestracja sterowania klawiaturą

    glutMainLoop();
    return 0;
}