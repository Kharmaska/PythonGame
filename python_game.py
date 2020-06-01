"""
This is where I am training on Pygame by creating a Frogger like game
"""

# Start the game loop
# Use game loop to render graphics

import pygame
pygame.init()

# Size of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Crossy RPG'
# Colors for the screen
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Creation of the game clock to enable to refresh rate with the tickrate
clock = pygame.time.Clock()
TICK_RATE = 60
is_game_over = False

# Creates the window of specified size in white to display the game
game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Sets the game window color to white
game_screen.fill(WHITE_COLOR)
pygame.display.set_caption(SCREEN_TITLE)

# Main game loop, used to update all gameplay such as movements, checks and graphics
# Runs until is_game_over = True
while not is_game_over:

    # Loop to get all the game events at any given time
    # Like mouse movements, key press,buttons clicks, exit, etc.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game_over = True
        print(event)

    # Update all game graphics
    pygame.display.update()
    # Tick the clock  to update everything within the game
    clock.tick(TICK_RATE)

# quits Pygame and the program
pygame.quit()
quit()
