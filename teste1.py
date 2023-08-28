import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Inicialização do Pygame e da OpenGL
pygame.init()
largura, altura = 800, 600
pygame.display.set_mode((largura, altura), DOUBLEBUF | OPENGL)
gluPerspective(45, (largura / altura), 0.1, 50.0)
glTranslatef(0.0, 0.0, -7)
glRotatef(45, 0, 1, 0)  # Rotação em 45 graus em torno do eixo Y

# Função para desenhar uma pirâmide vazada
def draw_empty_pyramid():
    glBegin(GL_LINES)
    glColor3f(1, 1, 0)  # Cor amarela
    # Base
    glVertex3f(-1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, -1)
    glVertex3f(1, -1, 1)
    glVertex3f(1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, 1)
    glVertex3f(-1, -1, -1)
    # Linhas das faces
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, -1)
    glVertex3f(0, 1, 0)
    glVertex3f(1, -1, -1)
    glVertex3f(0, 1, 0)
    glVertex3f(1, -1, 1)
    glVertex3f(0, 1, 0)
    glVertex3f(-1, -1, 1)
    glEnd()
    glPushMatrix()
    glColor4f(0.9, 0, 0, 0.5)
    glTranslate(4.75, 0, 0)
    glutSolidCube(2)
    glPopMatrix()

# Função para desenhar um cone vazado
def draw_empty_cone():
    glBegin(GL_LINES)
    glColor3f(0, 0, 1)  # Cor azul
    # Base
    # ...
    # Lados do cone
    # ...
    glEnd()

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutInit()
    
    # Desenhar a pirâmide na posição original
    draw_empty_pyramid()
    

    
    pygame.display.flip()
    pygame.time.wait(10)
