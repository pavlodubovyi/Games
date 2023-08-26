import pygame

pygame.init()

# Initials
WIDTH, HEIGHT = 1600, 1000
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pavlo's First Python Game")
game_running = True

# colors
bright_green = (170,255,0)
hot_pink = (255,105,180)
red = (255,0,0)
black = (0,0,0)

# paddle dimentions
paddle_width, paddle_height = 20, 150
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 50 - paddle_width/2, WIDTH - (50 - paddle_width/2)

# ball structure
radius = 25
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_velocity_x, ball_velocity_y = 1, 1 # increasing these numbers will increase the speed

# main loop
while game_running:
    window.fill(black) # need this for the ball not to leave a trace when moving. Each time the loop is started (ball "moves"), the screen is filled with black. 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game_running = False
    
    # movements
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # OBJECTS (ball and paddles) in the game window:
    pygame.draw.circle(window, bright_green, (ball_x, ball_y), radius)
    pygame.draw.rect(window, hot_pink, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(window, red, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    pygame.display.update() # this line makes the ball and paddles visible