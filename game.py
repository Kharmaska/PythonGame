"""
Game character class definition
"""


class GameCharacter:
    """
    Class for our Game Characters
    """
    speed = 5

    def __init__(self, name, width, height, x_pos, y_pos):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):
        """
        Function to handle the characters movement
        :param by_x_amount: left or right movement
        :param by_y_amount: up or down movement
        """
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount


character_0 = GameCharacter('char0', 50, 100, 100, 100)
print(character_0.name,character_0.width)
character_0.name = 'char1'
print(character_0.name,character_0.width)

character_0.move(50, -100)
print(character_0.x_pos)
print(character_0.y_pos)
