import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load("../img/blob.png")
        self.image = pygame.transform.scale(self.img, (36, 25))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction

        self.move_counter += 1
        if self.move_counter > 40:
            self.move_direction *= -1
            self.move_counter *= -1

blob_group = pygame.sprite.Group()

