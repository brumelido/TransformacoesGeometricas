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
     # Configurações para o estilo do cubo
     glClearColor(background_color[0], background_color[1], background_color[2], background_color[3])
     glColor(drawing_color)

     # Projeção
     glMatrixMode(GL_PROJECTION)
     glLoadIdentity()
     gluPerspective(60, (screen_width / screen_height), 0.1, 100.0)

     # modelview
     glMatrixMode(GL_MODELVIEW)
     glTranslate(0, 0, -5)
     glLoadIdentity()
     glViewport(0, 0, screen.get_width(), screen.get_height())
     glEnable(GL_DEPTH_TEST)
     glTranslate(0, 0, -2)


tx = 0
tdirecao = 0.1
sxyz = 1
sdirecao = -0.1

def display():
     global tx, tdirecao, sxyz, sdirecao

     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
     glRotatef(1, 10, 0, 1) # Transformação geométrica Rotação
     glTranslatef(tx, 0, 0) # Transformação geométrica Translação
     glScalef(sxyz, sxyz, sxyz)
     
     tx += tdirecao
     sxyz += sdirecao

     if tx >= 0.2 or tx <= -0.3:
          tdirecao *= -1
     
     if sxyz >= 1.1 or sxyz <= 0.9:
          sdirecao *= -1
     
     glPushMatrix()
     wireCube()
     glPopMatrix()


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