#include <GLUT/glut.h>
#include <math.h>

bool denka = false; // do przelaczania miedzy zadaniami
float angleX = 20.0f;
float angleY = 15.0f;

void init() {
    glClearColor(0.56f, 0.56f, 0.73f, 1.0f);
    glEnable(GL_DEPTH_TEST);
}

void display(void) {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    glRotatef(angleX, 1.0f, 0.0f, 0.0f);
    glRotatef(angleY, 0.0f, 1.0f, 0.0f);

    const GLfloat PI = 3.14f;
    GLfloat r = 0.5f;
    GLfloat y_dol = -0.4f;
    GLfloat y_gora = 0.4f;
    GLfloat krok = (2.0f * PI) / 60.0f;

    if (!denka) {
        // walec bez denek
        glPolygonMode(GL_FRONT, GL_FILL);
        glPolygonMode(GL_BACK, GL_LINE);
    } else {
        // walec z denkami
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL);
    }

    // tuba walca
    glColor3f(0.0f, 0.0f, 1.0f);
    glBegin(GL_QUAD_STRIP);
        for (GLfloat kat = 0.0f; kat <= ceil(2.0f * PI); kat += krok) {
            glVertex3f(cos(kat) * r, y_gora, sin(kat) * r);
            glVertex3f(cos(kat) * r, y_dol,  sin(kat) * r);
        }
    glEnd();

    // dodawanie denek
    if (denka) {
        // gorne
        glColor3f(1.0f, 1.0f, 0.0f);
        glBegin(GL_TRIANGLE_FAN);
            glVertex3f(0.0f, y_gora, 0.0f);
            for (GLfloat kat = 0.0f; kat <= ceil(2.0f * PI); kat += krok) {
                glVertex3f(cos(kat) * r, y_gora, sin(kat) * r);
            }
        glEnd();

        // dolne
        glColor3f(0.0f, 0.0f, 0.5f);
        glBegin(GL_TRIANGLE_FAN);
            glVertex3f(0.0f, y_dol, 0.0f);
            for (GLfloat kat = 0.0f; kat <= ceil(2.0f * PI); kat += krok) {
                glVertex3f(cos(kat) * r, y_dol, sin(kat) * r);
            }
        glEnd();
    }

    glFlush();
}

void keyboard(unsigned char key, int x, int y) {
    if (key == ' ') {
        denka = !denka;
        glutPostRedisplay();
    }
    if (key == 'w') angleX += 5.0f;
    if (key == 's') angleX -= 5.0f;
    if (key == 'a') angleY -= 5.0f;
    if (key == 'd') angleY += 5.0f;
    if (key == 'q') exit(0);
    glutPostRedisplay();
}

int main(int argc, char *argv[]) {
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH);
    glutInitWindowSize(400, 400);
    glutInit(&argc, argv);
    glutCreateWindow("walec");

    init();
    glutDisplayFunc(display);
    glutKeyboardFunc(keyboard);

    glutMainLoop();
    return 0;
}