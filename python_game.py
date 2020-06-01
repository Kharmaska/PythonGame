"""
This is where I am training on Pygame by creating a Frogger like game
"""

# Start the game loop
# Use game loop to render graphics

import pygame

# Size of the screen
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# Colors for the screen
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Creation of the game clock to enable to refresh rate with the tickrate
clock = pygame.time.Clock()

class Game:

    TICK_RATE = 60


    # Initializer for the game class to set up width, height and title
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Creates the window of specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        # Sets the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

    def run_game_loop(self):
        is_game_over = False

        # Main game loop, used to update all gameplay such as movements, checks and graphics
        # Runs until is_game_over = True
        while not is_game_over:

            # Loop to get all the game events at any given time
            # Like mouse movements, key press,buttons clicks, exit, etc.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                print(event)

            # Draws a rectangle on top of the game screen canvas (x, y, width, height)
            # pygame.draw.rect(game_screen, BLACK_COLOR, [350, 350, 100, 100])
            # Draws a circle on top of the game screen canvas (x, y, radius)
            # pygame.draw.circle(game_screen, BLACK_COLOR, (400, 300), 50)

            #game_screen.blit(player_image, (375, 375))

            # Update all game graphics
            pygame.display.update()
            # Tick the clock  to update everything within the game
            clock.tick(self.TICK_RATE)

pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()



# quits Pygame and the program
pygame.quit()
quit()

# player_image = pygame.image.load('player.png')
# player_image = pygame.transform.scale(player_image, (50,50))