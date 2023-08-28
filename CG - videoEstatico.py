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
glRotatef(45, 0, 1, 0)  # Rotação em 45 graus em torno do eixo Y

# Função para desenhar uma pirâmide vazada
def draw_empty_pyramid(r, g, b, x):
    glPushMatrix()
    glTranslate(x, 0, 0)
    glBegin(GL_LINES)
    glColor3f(r, g, b)  
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
    glPopMatrix()

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
    #glTranslate(0.01, 0, 0)
    draw_empty_pyramid(1, 1, 0, 0)
    #glTranslate(0.07, 0, 0)
    draw_empty_pyramid(1, 0, 0, 2.75)
    #glTranslate(0.09, 0, 0)
    draw_empty_pyramid(0, 0, 1, -2.75)

    animate_horizontal()
    pygame.display.flip()
    pygame.time.wait(10)
