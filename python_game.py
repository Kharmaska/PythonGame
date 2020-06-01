"""
This is where I am training on Pygame by creating a Frogger like game
"""

import pygame

# Size of the screen
SCREEN_TITLE = 'Crossy RPG'
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
# Colors for the screen
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
# Creation of the game clock to enable to refresh rate with the tick rate
clock = pygame.time.Clock()

pygame.font.init()
font = pygame.font.SysFont('comicsans', 75)


class Game:
    """
    Main class for the game
    """
    # Refresh rate to 30 frames per sec as 60 is too fast for 144hz screens
    TICK_RATE = 30

    # Initializer for the game class to set up width, height and title
    def __init__(self, image_path, title, width, height):
        self.title = title
        self.width = width
        self.height = height

        # Creates the window of specified size in white to display the game
        self.game_screen = pygame.display.set_mode((width, height))
        # Sets the game window color to white
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)

        background_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(background_image, (width, height))


    def run_game_loop(self, level_speed):
        """
        Main loop for the game to draw graphics per tick rate
        and also to quit game once game is over
        """
        is_game_over = False
        did_win = False
        direction = 0

        player_character = PlayerCharacter('player.png', 375, 700, 50, 50)
        enemy_0 = EnemyCharacter('enemy.png', 20, 600, 40, 40)
        enemy_0.SPEED += level_speed + 1

        enemy_1 = EnemyCharacter('enemy.png', self.width - 40, 450, 40, 40)
        enemy_1.SPEED += level_speed + 2

        enemy_2 = EnemyCharacter('enemy.png', 20, 300, 40, 40)
        enemy_2.SPEED += level_speed + 3

        enemy_3 = EnemyCharacter('enemy.png', 20, 150, 40, 40)
        enemy_3.SPEED += level_speed + 5

        treasure = GameObject('treasure.png', 375, 50, 40, 40)

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


            # Redraws the screen to a blank white window
            self.game_screen.fill(WHITE_COLOR)
            self.game_screen.blit(self.image, (0, 0))

            score = font.render('Speed: ' + str(level_speed), True, WHITE_COLOR)
            self.game_screen.blit(score, (75, 700))

            # Draws the treasure
            treasure.draw(self.game_screen)

            # Updates the player position
            player_character.move(direction, self.height)
            # Draws the player at the new position
            player_character.draw(self.game_screen)

            # Same logic as above but with the enemy
            enemy_0.move(self.width)
            enemy_0.draw(self.game_screen)

            if level_speed > 3:
                enemy_1.move(self.width)
                enemy_1.draw(self.game_screen)
            if level_speed > 6:
                enemy_2.move(self.width)
                enemy_2.draw(self.game_screen)
            if level_speed > 10:
                enemy_3.move(self.width)
                enemy_3.draw(self.game_screen)

            # End game if collision between enemy or treasure
            if player_character.detect_collision(enemy_0):
                is_game_over = True
                did_win = False
                text = font.render('You lose! :(', True, BLACK_COLOR)
                self.game_screen.blit(text, (300, 500))
                pygame.display.update()
                clock.tick(1)
                break
            elif player_character.detect_collision(treasure):
                is_game_over = True
                did_win = True
                text = font.render('You win! :D', True, BLACK_COLOR)
                self.game_screen.blit(text, (300, 500))
                pygame.display.update()
                clock.tick(1)
                break

            # Update all game graphics
            pygame.display.update()
            # Tick the clock  to update everything within the game
            clock.tick(self.TICK_RATE)
        if did_win:
            self.run_game_loop(level_speed + 1)
        else:
            return


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

        if self.y_pos >= max_height - 40:
            self.y_pos = max_height - 40

    def detect_collision(self, other_sprite):
        """
        Method to handle collisions
        :param other_sprite: any other object like an enemy or the treasyre
        :return: boolean to tell we are colliding or not
        """

        # collision detection in case enemy is above or below player position
        if self.y_pos > other_sprite.y_pos + other_sprite.height or \
                self.y_pos + self.height < other_sprite.y_pos:
            return False
        # collision detection in case enemy at the same Y but left or right of the
        # player's position
        if self.x_pos > other_sprite.x_pos + other_sprite.width or \
                self.x_pos + self.width < other_sprite.x_pos:
            return False
        return True


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
        elif self.x_pos >= max_width - 40:
            self.SPEED = -abs(self.SPEED)
        self.x_pos += self.SPEED


pygame.init()

new_game = Game('background.png', SCREEN_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT)
new_game.run_game_loop(1)

# quits Pygame and the program
pygame.quit()
quit()
