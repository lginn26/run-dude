import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.image.load('assets/sprites/rundude-walk00.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # graphical variables
        self.cur_frame_dur = 10

        # logic variables
        self.speed = 10
        self.jump_dur = 10

    def controls(self, control):
        """
        Makes instances react to player inputs
        :param control: Currently pressed keys
        """

        # Changes vector values based on player input

        if control[pygame.K_LEFT]:
            self.rect.x -= self.speed
        elif control[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def update(self, us_input):
        self.controls(us_input)


