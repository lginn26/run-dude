import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()

        # graphical variables
        self.max_frame_dur = 6
        self.cur_frame_dur = 6
        self.cur_frame = 0

        self.walk_cycle = [
            pygame.image.load('assets/sprites/rundude-walk00.png'),
            pygame.image.load('assets/sprites/rundude-walk01.png'),
            pygame.image.load('assets/sprites/rundude-walk02.png'),
            pygame.image.load('assets/sprites/rundude-walk01.png')
        ]

        # basic variables
        self.image = pygame.image.load('assets/sprites/rundude-walk00.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # logic variables
        self.speed = 10
        self.jump_dur = 10

    def change_sprite(self):
        if self.cur_frame_dur > 0:
            self.cur_frame_dur -= 1
        else:
            print("frame shift")
            self.cur_frame += 1
            self.cur_frame_dur = self.max_frame_dur

            if self.cur_frame > len(self.walk_cycle) - 1:
                self.cur_frame = 0

        self.image = self.walk_cycle[self.cur_frame]

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
        """
        Makes instances preform intended actions
        :param us_input: Short for user input, intakes the player's keyboard presses
        """
        self.controls(us_input)
        self.change_sprite()

class Astetic_Object(pygame.sprite.Sprite):

    def __init__(self, x, y, speed, image):
        super().__init__()

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed

    def update(self, screen_size):
        self.rect.x -= self.speed

        if self.rect.right < screen_size[0]-screen_size[0]:
            self.rect.x = screen_size[0]