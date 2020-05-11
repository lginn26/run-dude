import pygame, random
from game_objects import Player, Astetic_Object, Obstacle, Coin

# Initialize game engine
pygame.init()

# Stages
START = 0
PLAYING = 1
DEAD = 3
END = 2
PAUSE = 4

# Game Variables
done = False
stage = START
score = 0

# Obstacle Variables
max_next_obst = 100
min_next_obst = 5
next_obst = 20

# Collectable Variables
coin_value = 50
coin_chance = 1, 5
coin_cue = 1

# Score Variables
org_next_point = 10
next_point = 10
point_reward = 2

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
font_title = pygame.font.Font("assets/fonts/AbrilFatface-Regular.ttf", 100)
font_sub_title = pygame.font.Font("assets/fonts/AbrilFatface-Regular.ttf", 50)
score_font = pygame.font.Font("assets/fonts/AbrilFatface-Regular.ttf", 40)

# Graphic Functions

def show_score(x, y, score):
    """

    :param x: X axis location where the text with be displayed
    :param y: Y axis location where the text with be displayed
    :param score: Current value stored in score
    """
    score_text = score_font.render(("000000000" + str(score))[-8:], 1, BLACK)
    w = score_text.get_width()
    screen.blit(score_text, [x, y])

def show_title_card(big_text, little_text):
    """
    Displays a title card using given text
    :param big_text: Text that appears on the top row
    :param little_text: Smaller text that appears on the bottom row
    """

    title_text = font_title.render(big_text, 1, BLACK)
    w = title_text.get_width()

    lower_text = font_sub_title.render(little_text, 1, BLACK)
    w2 = lower_text.get_width()

    screen.blit(title_text, [(SIZE[0]/2 - w/2), 400])
    screen.blit(lower_text, [(SIZE[0]/2 - w2/2), 500])

# Logic Functions

def setup():
    """
    Creates all game objects
    """
    global score, collectables, obstacle, decoration, player, dude

    # Sets initial game state
    stage == START
    score = 0

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

    # Create obstacles
    obstacle = pygame.sprite.Group()

    # Create collectable
    collectables = pygame.sprite.Group()

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
                    stage = START
                    setup()
                    pygame.mixer.music.rewind()

    # Game Logic (Preforms ingame actions and controls the program.)

    if stage == PLAYING:
        player.update(pygame.key.get_pressed(), obstacle, SIZE)

        if dude.check_obst_collide(obstacle, False):
            stage = DEAD

        if dude.check_obst_collide(collectables, True):
            score += coin_value

        decoration.update(SIZE)
        obstacle.update(SIZE)
        collectables.update(SIZE)

        # Generates obstacles and collectables at varying heights at varying distances
        next_obst -= 1

        if next_obst <= 0:
            next_obstacle = Obstacle(1990, 10, random.choice(["short", "medium", "tall", "extall"]))
            obstacle.add(next_obstacle)

            if random.randint(coin_chance[0], coin_chance[1]) == coin_cue:
                coin = Coin(next_obstacle.rect.x, next_obstacle.rect.y - 60, next_obstacle.speed)
                collectables.add(coin)

            next_obst += random.randint(min_next_obst, max_next_obst)

        # Increments the score
        next_point -= 1

        if next_point <= 0:
            score += point_reward
            next_point = org_next_point

    # Drawing Logic (Draws the graphics and sprites on screen)
    pygame.Surface.fill(screen, SKYBLUE)
    player.draw(screen)
    decoration.draw(screen)
    obstacle.draw(screen)
    collectables.draw(screen)

    if stage == START:
        show_title_card("--Run Dude--", "--Press SPACE to start--")
    elif stage == PAUSE:
        show_title_card("--PAUSED--", "--Press P to resume--")
    elif stage == DEAD:
        show_title_card("--You Crashed--", "--Press r to restart--")

    show_score(25, 25, score)
    # Update screen (Draw the picture in the window.)
    pygame.display.flip()

    # Limit refresh rate of game loop
    clock.tick(refresh_rate)

# Close window and quit
pygame.quit()