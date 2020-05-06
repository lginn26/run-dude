import pygame

class player(pygame.sprite.Sprite):

    def __init__(self, x, y,):
        super().__init__()

        self.image = None
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 1
        self.jump_dur = 10
