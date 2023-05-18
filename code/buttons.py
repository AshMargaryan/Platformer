import pygame
from settings import *

restart_image = pygame.image.load("../img/restart_btn.png")

start_image = pygame.image.load("../img/start_btn.png")

exit_image = pygame.image.load("../img/exit_btn.png")

class Button():
    def __init__(self, x, y, image):
        self.image = image

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.clicked = False

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        screen.blit(self.image, self.rect)

        return action

restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, restart_image)
start_button = Button(screen_width // 2 - 300, screen_height // 2, start_image)
exit_button = Button(screen_width // 2 + 50, screen_height // 2, exit_image)