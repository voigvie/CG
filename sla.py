from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import pygame

# Variáveis para controle da rotação com o mouse
rotate_x = 0
rotate_y = 0
dragging = False

def draw_cylinder(radius, height, sides):
    glBegin(GL_QUAD_STRIP)
    for i in range(sides + 1):
        angle = 2.0 * math.pi * float(i) / float(sides)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)

        glVertex3f(x, y, height)
        glVertex3f(x, y, 0.0)

    glEnd()

    # Draw the top and bottom faces of the cylinder
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 0.0, height)
    for i in range(sides + 1):
        angle = 2.0 * math.pi * float(i) / float(sides)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, height)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0, 0.0, 0.0)
    for i in range(sides + 1):
        angle = 2.0 * math.pi * float(i) / float(sides)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, 0.0)
    glEnd()

def mouse_motion(x, y):
    global rotate_x, rotate_y, dragging
    sensitivity = 0.1

    if dragging:
        delta_x = x - rotate_x
        delta_y = y - rotate_y
        rotate_x = x
        rotate_y = y

        glRotatef(delta_x * sensitivity, 0, 1, 0)
        glRotatef(delta_y * sensitivity, 1, 0, 0)
        glutPostRedisplay()

def mouse(button, state, x, y):
    global rotate_x, rotate_y, dragging

    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            dragging = True
            rotate_x = x
            rotate_y = y
        else:
            dragging = False

def main():
    width, height = 800, 600
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"Cylinder Example")
    gluPerspective(45, (width / height), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    sides = 20
    radius = 1.0
    height = 2.0

    glutMouseFunc(mouse)
    glutMotionFunc(mouse_motion)

    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cylinder(radius, height, sides)
        glutSwapBuffers()

if __name__ == "__main__":
    main()

