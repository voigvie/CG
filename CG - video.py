import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Inicialização do Pygame e da OpenGL
pygame.init()
largura, altura = 800, 600
pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL)
gluPerspective(45, (largura / altura), 0.1, 50.0)
glTranslatef(0.0, 0.0, -7)

# Função para desenhar uma pirâmide
def draw_pyramid():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 1, 0)  # Cor amarela
    # Base
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    # Faces laterais
    glVertex3f(0, 1, 0)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(0, 1, 0)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glEnd()

# Função de animação para girar na horizontal
def animate_horizontal():
    global angle_horizontal
    glRotatef(1, 0, 1, 0)  # Rotação horizontal
    angle_horizontal += 1

angle_horizontal = 0

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_pyramid()
    animate_horizontal()
    pygame.display.flip()
    pygame.time.wait(10)
