import pygame, math

GROUND = 965
JUMPDUR = 10
GRAVITY = 1
DEAD = 3

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
        self.jump_force = 7

        self.jump_dur = 10

        self.max_gravity = 17
        self.vector_y = 0

    def check_obst_collide(self, obsts):
        """
        Checks if Player instance has collided with a obstacle instance
        :param obsts: A list of Obstacle instances
        :return: A boolian value: Player instance has collided with a obstacle instance?
        """

        hit_list = pygame.sprite.spritecollide(self, obsts, False, pygame.sprite.collide_mask)

        return len(hit_list) > 0

    def do_jump_dur_reset(self):
        if self.rect.bottom >= GROUND:
            self.jump_dur = JUMPDUR

    def do_gravity(self):
        if self.vector_y >= self.max_gravity:
            self.vector_y = self.max_gravity
        elif self.vector_y <= -self.max_gravity:
            self.vector_y = -self.max_gravity

        self.rect.y -= self.vector_y

        if self.rect.bottom < GROUND:
            self.vector_y -= GRAVITY

    def do_bounds_control(self, screen):
        if self.rect.left < screen[0]-screen[0]:
            self.rect.x += self.speed
        elif self.rect.right > screen[0]:
            self.rect.x -= self.speed

        if self.rect.bottom > GROUND:
            self.rect.bottom -= (self.rect.bottom - GROUND)

    def change_sprite(self):
        if self.cur_frame_dur > 0:
            self.cur_frame_dur -= 1
        else:
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

        if (control[pygame.K_UP] or control[pygame.K_SPACE]) and self.jump_dur > 0:
            self.vector_y += self.jump_force
            self.jump_dur -= GRAVITY

        if not control[pygame.K_UP]:
            self.jump_dur = 0

    def update(self, us_input, obsts, screen):
        """
        Makes instances preform intended actions
        :param us_input: Short for user input, intakes the player's keyboard presses
        """
        self.controls(us_input)
        self.do_gravity()
        self.do_jump_dur_reset()
        self.do_bounds_control(screen)
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

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, x, speed, type):
        super().__init__()

        if type == "short":
            self.image = pygame.image.load('assets/sprites/wood_obstacle_short.png')
        elif type == "medium":
            self.image = pygame.image.load('assets/sprites/wood_obstacle_medium.png')
        elif type == "tall":
            self.image = pygame.image.load('assets/sprites/wood_obstacle_tall.png')
        elif type == "extall":
            self.image = pygame.image.load('assets/sprites/wood_obstacle_extall.png')
        else:
            self.image = pygame.image.load('assets/sprites/wood_obstacle_short.png')

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = GROUND - self.rect[3]

        self.speed = speed

    def update(self,  screen_size):
        self.rect.x -= self.speed

        if self.rect.right < screen_size[0] - screen_size[0]:
            self.kill()