import pygame
from settings import *

def draw_text(text, font,col, x, y):
    img = font.render(text, True, col)
    screen.blit(img, (x, y))