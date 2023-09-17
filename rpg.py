"""
|X| | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | |O|
"""

from random import randint, choice

# size of world map
SIZE_X = randint(5, 10)
SIZE_Y = randint(5, 10)

def check_game_state(character_position_x, character_position_y, character_sign,
                     exit_x, exit_y,
                     enemy_position_x, enemy_position_y):
    
    win_condition = character_position_x == exit_x and character_position_y == exit_y
    loss_condition = character_position_x == enemy_position_x and character_position_y == enemy_position_y

    if win_condition:
        character_sign = "W"
        print(f"Congratulations! You've reached the portal in {turns} turns!")
    elif loss_condition:
        character_sign = "_"
        print(f"After {turns} turns of battle Enemy killed you!")
    
    return character_sign

def generate_map(character_position_x, character_position_y, character_sign,
                 exit_x, exit_y, exit_sign,
                 enemy_position_x, enemy_position_y, enemy_sign,
                 size_x=SIZE_X, size_y=SIZE_Y):
    
    world_map = ""

    for y_coordinate in range(size_y):
        row = "|"   # zeroing the map, "row" is a variable for drawing the map

        for x_coordinate in range(size_x):
            if character_position_x == x_coordinate and character_position_y == y_coordinate:
                row += f"{character_sign}|"
            elif enemy_position_x == x_coordinate and enemy_position_y == y_coordinate:
                row += f"{enemy_sign}|"
            elif exit_x == x_coordinate and exit_y == y_coordinate:
                row += f"{exit_sign}|"
            else:
                row += " |"
        
        world_map += f"{row}\n"

    return world_map

def move(direction, x, y, size_x=SIZE_X, size_y=SIZE_Y):
    
    if direction == "u" and y > 0:
        y -= 1
    elif direction == "d" and y < size_y - 1:
        y += 1
    elif direction == "l" and x > 0:
        x -= 1
    elif direction == "r" and x < size_x - 1:
        x += 1
    
    return x, y

# character position ("H")
character_position_x = randint(0, SIZE_X - 1)
character_position_y = randint(0, SIZE_Y - 1)
character_sign = "H"

# enemy position ("E")
enemy_position_x = randint(0, SIZE_X - 1)
enemy_position_y = randint(0, SIZE_Y - 1)
enemy_sign = "E"

# position of exit portal ("O")
exit_x = randint(0, SIZE_X - 1)
exit_y = randint(0, SIZE_Y - 1)
exit_sign = "O"

turns = 0

# infinite game loop (ctrl + c for manual break)
while True:

    character_sign = check_game_state(character_position_x, character_position_y, character_sign,
                     exit_x, exit_y,
                     enemy_position_x, enemy_position_y)

    # world_map will take it's structure from result of "generate_map" function
    world_map = generate_map(character_position_x, character_position_y, character_sign,
                             enemy_position_x, enemy_position_y, enemy_sign,
                             exit_x, exit_y, exit_sign)

    print(world_map)
    print(f"Turns: {turns}")
    print("-" * 11)

    if character_sign != "H":
        break

    # directions of Hero and Enemy
    direction = input("Enter direction (u / d / l / r): ")
    character_position_x, character_position_y = move (direction, character_position_x, character_position_y)

    enemy_direction = choice("udlr")
    enemy_position_x, enemy_position_y = move(enemy_direction, enemy_position_x, enemy_position_y)

    # counter of turns
    turns += 1