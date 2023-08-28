
from math import cos
from math import pi
from math import sin
import timeit
#import numpy
import ctypes
import random
from sys import argv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *



def eixos():      #desenha os eixos x e y do plano cartesiano.
    glBegin(GL_LINES)# objeto
    glColor3f(.9, .1, .1) # cor RGB
    glVertex3f( -5.0, 0.0, 0.0 )  #  eixo x
    glVertex3f( 5.0, 0.0, 0.0 )#  

    glColor3f(.1, .1, .9) # cor RGB
    glVertex3f( 0.0, -5.0, 0.0)#  eixo y
    glVertex3f( 0.0, 5.0, 0.0 )  #

    glColor3f(.1, .9, .1) # cor RGB
    glVertex3f( 0.0, 0.0, 5.0)#  eixo z
    glVertex3f( 0.0, 0.0, -5.0 )  # 
    glEnd()
    

def desenho():    
    eixos()
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    #glTranslate( -1.0, -2.0, 0.0)  #Transtaçao do objeto
    glRotatef(-30, -0.5, 1.0, 0.0)     #Rotaçao do objeto
    glScale(0.1, 0.1, 0.1)

    # Opçoes de objetos: GL_TRIANGLES, GL_POINTS, GL_LINES, GL_LINE_STRIP,
    # GL_LINE_LOOP, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_QUADS,
    # GL_QUAD_STRIP, GL_POLYGON.
    
    glBegin(GL_POLYGON)# face1
    glColor3f(.1, .6, .1) # cor RGB
    glVertex3f( 0.0, 5.0, 0.0  )  #  ponto de vertice
    glVertex3f( 5.0, 5.0, 0.0  )  #  ponto de vertice
    glVertex3f( 5.0, 0.0, 0.0  )  #  ponto de vertice
    glVertex3f( 0.0, 0.0, 0.0  )  #  ponto de vertice
    glEnd()

    glBegin(GL_POLYGON)# face 2 LD
    glColor3f(.1, .6, .4) # cor RGB
    glVertex3f( 5.0, 5.0, 0.0  )  #  ponto de vertice
    glVertex3f( 5.0, 5.0, -5.0  )  #  ponto de vertice
    glVertex3f( 5.0, 0.0, -5.0  )  #  ponto de vertice
    glVertex3f( 5.0, 0.0, 0.0  )  #  ponto de vertice
    glEnd()

    glBegin(GL_POLYGON)# face 3  tampa
    glColor3f(.4, .6, .4) # cor RGB
    glVertex3f( 0.0, 5.0, 0.0  )  #  ponto de vertice
    glVertex3f( 0.0, 5.0, -5.0  )  #  ponto de vertice
    glVertex3f( 5.0, 5.0, -5.0  )  #  ponto de vertice
    glVertex3f( 5.0, 5.0, 0.0  )  #  ponto de vertice
    glEnd()

    

    
    glPopMatrix()
    #desenho do cubo pelo glut
    #glutWireCube(1.0)

def iluminacao_da_cena():
    # Configurando os parâmetros para as fontes de luz
    # GL_DIFFUSE define o parâmetro usado
    # para luz difusa (no formato RGBA)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1., 1., 1., 1.])
    # Os três parâmetros definem a posição da fonte luminosa
    # O quarto define se a fonte é direcional (0) ou posicional (1)
    glLightfv(GL_LIGHT0, GL_POSITION, [-5., 5., -5., 1.])
    # Aplica os parâmetros de iluminação
    glEnable(GL_LIGHTING)
    # Inclui a fonte de luz 0 no calculo
    # da iluminação
    glEnable(GL_LIGHT0)

def tela():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Limpar a tela
    glClearColor(1.0, 1.0, 1.0, 1.0) # Limpa a janela com a cor especificada
    glMatrixMode(GL_PROJECTION) # Muda a matriz de projeçao
    glLoadIdentity()# carrega a matriz identidade
    gluPerspective(distancia,1,0.1,500) # Especifica a projeção perspectiva
    glMatrixMode(GL_MODELVIEW) # Especifica sistema de coordenadas do modelo
    glLoadIdentity() # Inicializa sistema de coordenadas do modelo
    gluLookAt(0,0,10, 0,0,0, 0,5,0) # Especifica posição do observador e do alvo
    #iluminacao_da_cena()
    glEnable(GL_DEPTH_TEST) # verifica os pixels que devem ser desenhados no desenho 3d

    desenho()                    
    glFlush()                    # Aplica o desenho

# Função callback chamada para gerenciar eventos do mouse
def ControleMouse(button, state, x, y):
    global distancia
    if (button == GLUT_LEFT_BUTTON):
        if (state == GLUT_DOWN): 
            if (distancia >= 10):
                distancia -= 2
		
    if (button == GLUT_RIGHT_BUTTON):
        if (state == GLUT_DOWN):   # Zoom-out
            if (distancia <= 130):
                distancia += 2
    tela()
    glutPostRedisplay()

global distancia

glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(800,800)
glutCreateWindow(b"Aula01")
distancia = 20
glutDisplayFunc(tela)
glutMouseFunc(ControleMouse)
glutMainLoop()  # Inicia o laço de eventos da GLUT



