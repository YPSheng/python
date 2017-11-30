import os
import pygame
from pygame.locals import *



pygame.init()
text = u"1234"

font = pygame.font.SysFont("Microsoft YaHei",64)
ftext = font.render(text,True,(65,83,130),(255,255,255))
pygame.image.save(ftext,"D:/pythontab.jpg")