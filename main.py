import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Cube import wireCube

pygame.init()

# project settings
screen_width = 1000
screen_height = 800
background_color = (0, 0, 0, 1)
drawing_color = (1, 1, 1, 1)

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('OpenGL in Python')

def initialise():
    glClearColor(*background_color)
    glColor(*drawing_color)

    # Projeção
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

    # Modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslate(0, 0, -5)
    glViewport(0, 0, screen.get_width(), screen.get_height())
    glEnable(GL_DEPTH_TEST)

def mirror(axis='x'):
    """ Aplica um espelhamento no eixo escolhido ('x', 'y' ou 'z'). """
    if axis == 'x':
        glScalef(-1, 1, 1)
    elif axis == 'y':
        glScalef(1, -1, 1)
    elif axis == 'z':
        glScalef(1, 1, -1)

# Transformações
tx = 0
tdirecao = 0.1
sxyz = 1
sdirecao = -0.1

def display():
    global tx, tdirecao, sxyz, sdirecao

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslate(0, 0, -5)
    glRotatef(1, 10, 0, 1)
    glTranslatef(tx, 0, 0)
    glScalef(sxyz, sxyz, sxyz)

    # Desenha o cubo original
    glPushMatrix()
    glTranslatef(-1.5, 0, 0)  # Move o cubo original para a esquerda
    wireCube()
    glPopMatrix()

    # Desenha o cubo espelhado
    glPushMatrix()
    glTranslatef(1.5, 0, 0)  # Move o cubo espelhado para a direita
    mirror('x')  # Aplica espelhamento no eixo X
    wireCube()
    glPopMatrix()

    # Atualiza valores de translação e escala
    tx += tdirecao
    sxyz += sdirecao

    if tx >= 0.2 or tx <= -0.3:
        tdirecao *= -1

    if sxyz >= 1.1 or sxyz <= 0.9:
        sdirecao *= -1

done = False
initialise()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    display()
    pygame.display.flip()
    pygame.time.wait(100)
pygame.quit()