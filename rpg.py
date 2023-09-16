"""
|X| | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | |O|
"""

from random import randint

# size of world map
SIZE_X = 5
SIZE_Y = 5

# position of character ("X")
character_position_x = 1
character_position_y = 1
character_sign = "X"

# position of exit portal ("O")
exit_x = randint(0, SIZE_X - 1)
exit_y = randint(0, SIZE_Y - 1)
portal_sign = "O"

turns = 0

# infinite game loop (ctrl + c for manual break)
while True:

    # building world map with character and exit
    world_map = ""

    win_condition = character_position_x == exit_x and character_position_y == exit_y

    if win_condition:
        character_sign = "W"

    for y_coordinate in range(SIZE_Y):
        row = "|"   # zeroing the map, "row" is a variable for drawing the map

        for x_coordinate in range(SIZE_X):
            if character_position_x == x_coordinate and character_position_y == y_coordinate:
                row += f"{character_sign}|"
            elif exit_x == x_coordinate and exit_y == y_coordinate:
                row += f"{portal_sign}|"
            else:
                row += " |"
        
        world_map += f"{row}\n"

    print(world_map)
    print(f"Turns: {turns}")
    print("-" * 11)

    if win_condition:
        print(f"Congratulations! You've reached the portal in {turns} turns!")
        break

    # user chooses direction -> X moves
    direction = input("Enter direction (u / d / l / r): ")

    if direction == "u" and character_position_y > 0:
        character_position_y -= 1
    elif direction == "d" and character_position_y < SIZE_Y - 1:
        character_position_y += 1
    elif direction == "l" and character_position_x > 0:
        character_position_x -= 1
    elif direction == "r" and character_position_x < SIZE_X - 1:
        character_position_x += 1

    turns += 1