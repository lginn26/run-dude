import pygame

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


# Fonts

# Functions
def setup():
    pass

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

    # Drawing Logic (Draws the graphics and sprites on screen)

    # Update screen (Draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()