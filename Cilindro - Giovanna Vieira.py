import math
from sys import argv
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_NAME = "Cilindro"

def cilindro(r, h, n):
    angle = 2.0 * math.pi / n
    top_x, top_y, top_z = 0.0, h/2.0, 0.0
    bottom_x, bottom_y, bottom_z = 0.0, -h/2.0, 0.0

    glBegin(GL_TRIANGLES)
    for i in range(n):
        p0_x = r * math.cos(i * angle)
        p0_y = 0.0
        p0_z = r * math.sin(i * angle)

        p1_x = r * math.cos((i + 1) * angle)
        p1_y = 0.0
        p1_z = r * math.sin((i + 1) * angle)

        glNormal3f(0.0, 1.0, 0.0)
        glColor3f(.9, .1, .1)
        glVertex3f(top_x, top_y, top_z)
        glVertex3f(p0_x, top_y, p0_z)
        glVertex3f(p1_x, top_y, p1_z)

        glNormal3f(p0_x / r, 0.0, p0_z / r)
        glColor3f(.1, .1, .9)
        glVertex3f(p0_x, top_y, p0_z)
        glVertex3f(p0_x, bottom_y, p0_z)
        glVertex3f(p1_x, top_y, p1_z)

        glNormal3f(p0_x / r, 0.0, p0_z / r)
        glColor3f(.1, .9, .1)
        glVertex3f(p1_x, top_y, p1_z)
        glVertex3f(p0_x, bottom_y, p0_z)
        glVertex3f(p1_x, bottom_y, p1_z)

        glNormal3f(0.0, -1.0, 0.0)
        glColor3f(.9, .1, .1)
        glVertex3f(p1_x, bottom_y, p1_z)
        glVertex3f(p0_x, bottom_y, p0_z)
        glVertex3f(bottom_x, bottom_y, bottom_z)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(3.0, 3.0, 3.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    # Cilindro
    cilindro(1.0, 2.0, 100)

    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b'Cilindro')

    glutDisplayFunc(display)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(75.0, 1.0 * WINDOW_WIDTH / WINDOW_HEIGHT, 10e-3, 10e3)

    glutMainLoop()

if __name__ == "__main__":
    main()
