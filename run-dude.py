import pygame
from game_objects import Player, Astetic_Object

# Initialize game engine
pygame.init()

# Stages
START = 0
PLAYING = 1
DEAD = 3
END = 2
PAUSE = 4

# Variables
done = False
stage = START

# Window
WIDTH = 1920
HEIGHT = 1080
SIZE = (WIDTH, HEIGHT)
TITLE = "Run Dude"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60
display_clock = 0

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (100, 255, 100)
SKYBLUE = (0, 238, 255)


# Fonts

# Functions
def setup():
    """
    Creates all game objects
    """

    global decoration, player, dude

    # Create a player object
    dude = Player(960, 865)

    player = pygame.sprite.GroupSingle()
    player.add(dude)

    # Create decoration
    decoration = pygame.sprite.Group()

    decorations = [
        Astetic_Object(0, 965, 10, pygame.image.load('assets/sprites/ground.png')),
        Astetic_Object(1920, 965, 10, pygame.image.load('assets/sprites/ground.png')),
        Astetic_Object(3840, 965, 10, pygame.image.load('assets/sprites/ground.png')),
        Astetic_Object(0, 100, 10, pygame.image.load('assets/sprites/cloud.png')),
        Astetic_Object(300, 300, 10, pygame.image.load('assets/sprites/cloud.png')),
        Astetic_Object(600, 200, 10, pygame.image.load('assets/sprites/cloud.png')),
        Astetic_Object(900, 100, 10, pygame.image.load('assets/sprites/cloud.png')),
        Astetic_Object(1200, 300, 10, pygame.image.load('assets/sprites/cloud.png')),
        Astetic_Object(1500, 200, 10, pygame.image.load('assets/sprites/cloud.png')),

    ]
    for item in decorations:
        decoration.add(item)

# Game loop
setup()

while not done:
    # Input handling (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif stage == START:
                if event.key == pygame.K_SPACE:
                    stage = PLAYING
            elif stage == PLAYING:
                if event.key == pygame.K_p:
                    stage = PAUSE
                    pygame.mixer.music.pause()
            elif stage == PAUSE:
                if event.key == pygame.K_p:
                    stage = PLAYING
                    pygame.mixer.music.unpause()
            elif stage == END or stage == DEAD:
                if event.key == pygame.K_r:
                    setup()
                    pygame.mixer.music.rewind()

    # Game Logic (Preforms ingame actions and controls the program.)
    player.update(pygame.key.get_pressed(), SIZE)
    decoration.update(SIZE)

    # Drawing Logic (Draws the graphics and sprites on screen)
    pygame.Surface.fill(screen, SKYBLUE)
    player.draw(screen)
    decoration.draw(screen)

    # Update screen (Draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()