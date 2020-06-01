# Start the basic game set up
# Set up the display

import pygame

# Size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# Colors for the screen
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)

# Creates the window of specified size in white to display the game
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Sets the game window color to white
game_screen.fill(WHITE_COLOR)