"""
Initializing the player's position
"""
x_pos = 0
e_x_pos = 4


def move():
    """
    move
    """
    global x_pos
    x_pos += 1


move()


def move_by(amount):
    """
    move by amount
    """
    global x_pos
    x_pos += amount


def check_for_collision():
    """
    Check for the collision between enemy and player
    :return: True if collision happened
    """
    global x_pos
    global e_x_pos
    if x_pos == e_x_pos:
        return True
    else:
        return False


move_by(8)
did_collide = check_for_collision()
print(did_collide)
