
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
    glColor3f(.9, .3, .3) # cor RGB
    glVertex2f( -1.0, 0.0 )  #  eixo x
    glVertex2f( 1.0, 0.0 )#  

    glColor3f(.3, .3, .9) # cor RGB
    glVertex2f( 0.0, -1.0 )#  eixo y
    glVertex2f( 0.0, 1.0 )  #  
    glEnd()
    

def desenho():    
    eixos()
    glPushMatrix()                # Push e Pop Isolam os efeitos das transformaçoes no objeto
    #glTranslate( 0.0, 0.0, 0.0)  #Transtaçao do objeto
    #glRotatef(5, .0, .0, 1.0)     #Rotaçao do objeto
    glScale(0.1, 0.1, 0,1)
    # Opçoes de objetos: GL_TRIANGLES, GL_POINTS, GL_LINES, GL_LINE_STRIP,
    # GL_LINE_LOOP, GL_TRIANGLE_STRIP, GL_TRIANGLE_FAN, GL_QUADS,
    # GL_QUAD_STRIP, GL_POLYGON.
    glBegin(GL_LINE_LOOP)# objeto casa
    glColor3f(.9, .9, .9) # cor RGB
    glVertex2f( 1.0, 0.0 )  #  ponto de vertice (o ponto [0,0] eh no meio da tela)
    glVertex2f( 1.0, 3.0 )
    glVertex2f( 3.0, 5.0 )
    glVertex2f( 5.0, 3.0 )
    glVertex2f( 5.0, 0.0 )  
    glEnd()


    glBegin(GL_LINE_LOOP)# objeto porta
    glColor3f(.9, .9, .1) # cor RGB
    glVertex2f( 2.0, 0.0 )  #  ponto de vertice (o ponto [0,0] eh no meio da tela)
    glVertex2f( 2.0, 2.0 )
    glVertex2f( 4.0, 2.0 )
    glVertex2f( 4.0, 0.0 )
    glEnd()
    
    glPopMatrix() 
    

def tela():
    glClear(GL_COLOR_BUFFER_BIT) # Limpar a tela
    desenho()                    
    glFlush()                    # Aplica o desenho


glutInit(argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH)
glutInitWindowSize(800,800)
glutCreateWindow(b"Aula01")
glutDisplayFunc(tela)
glutMainLoop()  # Inicia o laço de eventos da GLUT



