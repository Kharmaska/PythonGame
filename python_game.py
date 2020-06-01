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
    """
    Main loop of the game
    """
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
        """
        Main loop for the game to draw graphics per tick rate and also to quit game once game is over
        """
        is_game_over = False
        direction = 0

        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
        enemy_0 = EnemyCharacter('enemy.png', 20, 400, 50, 50)

        # Main game loop, used to update all gameplay such as movements, checks and graphics
        # Runs until is_game_over = True
        while not is_game_over:

            # Loop to get all the game events at any given time
            # Like mouse movements, key press,buttons clicks, exit, etc.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        direction = 1
                    elif event.key == pygame.K_DOWN:
                        direction = -1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        direction = 0
                print(event)

            self.game_screen.fill(WHITE_COLOR)
            player_character.move(direction)
            player_character.draw(self.game_screen)

            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)
            # Update all game graphics
            pygame.display.update()
            # Tick the clock  to update everything within the game
            clock.tick(self.TICK_RATE)


class GameObject:
    """
    superclass to build all the game objects (player, enemy and treasure)
    """

    def __init__(self, image_path, x, y, width, height):
        object_image = pygame.image.load(image_path)
        # Scales the image up
        self.image = pygame.transform.scale(object_image, (width, height))

        self.x_pos = x
        self.y_pos = y

        self.width = width
        self.height = height

    def draw(self, background):
        """
        draws game objects on top of the game background
        :param background:
        """
        background.blit(self.image, (self.x_pos, self.y_pos))


class PlayerCharacter(GameObject):
    """
    Draws the player's character
    """
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, direction, max_height):
        """
        moves the player's character along the Y axis only
        :return:
        """
        if direction > 0:
            self.y_pos -= self.SPEED
        elif direction < 0:
            self.y_pos += self.SPEED

        if self.y_pos >= max_height - 20:
            self.y_pos = max_height - 20


class EnemyCharacter(GameObject):
    """
    Draws the enemy characters
    """
    SPEED = 10

    def __init__(self, image_path, x, y, width, height):
        super().__init__(image_path, x, y, width, height)

    def move(self, max_width):
        """
        moves the enemies on the X axis only and bounce back from
        left to right once reaching end of screen
        :return:
        """
        if self.x_pos <= 20:
            self.SPEED = abs(self.SPEED)
        elif self.x_pos >= max_width - 20:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED

pygame.init()

new_game = Game(SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop()

# quits Pygame and the program
pygame.quit()
quit()
