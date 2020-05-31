
"""
Initiating the game over status of the game
"""
is_game_over: bool = False

p_0_x_pos: int = 0
e_0_x_pos: int = 3
e_1_x_pos: int = 5

p_0_x_pos += 2
if p_0_x_pos in (e_0_x_pos, e_1_x_pos):
    is_game_over: bool = True
else:
    e_0_x_pos += 1
    e_1_x_pos += 1

p_x_pos: int = 2
e_x_pos: int = 3
end_x_pos: int = 10


while not is_game_over:
    print('player position' + str(p_x_pos))
    print('enemy position' + str(e_x_pos))
    if p_x_pos == e_x_pos:
        print('You lose')
        is_game_over = True
    elif p_x_pos >= end_x_pos:
        is_game_over = True
        print('You win')
    else:
        p_x_pos += 3
        e_x_pos += 1

x_pos = 5
movements = [1, -2, 6, -3, -2, 4]

for movement in movements:
    x_pos += movement
    print(x_pos)