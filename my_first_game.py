import pygame

pygame.init() # automatically initialize modules needed for the game

# Initials
WIDTH, HEIGHT = 1600, 1000
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pavlo's First Python Game")
game_running = True # flag for while-loop

# colors
bright_green = (170,255,0)
hot_pink = (255,105,180)
red = (255,0,0)
black = (0,0,0)

# paddle dimentions
paddle_width, paddle_height = 20, 150
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 50 - paddle_width/2, WIDTH - (50 - paddle_width/2)

# paddle speed
right_paddle_velocity_x = left_paddle_velocity_y = 1, 1

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
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP: # check if UP key is pressed
                right_paddle_velocity_x = -1
    
    # movements
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # OBJECTS (ball and paddles) in the game window:
    pygame.draw.circle(window, bright_green, (ball_x, ball_y), radius)
    pygame.draw.rect(window, hot_pink, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(window, red, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.display.update() # this line makes the ball and paddles visible

    # actions if ball goes out the screen
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius: # top-bottom boundaries
        ball_velocity_y *= -1 # don't know why there's no difference between '*= -1' and '= -1'
    if ball_x >= WIDTH: # reset the ball position to the center, if it goes out of the screen (RIGHT)
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_velocity_x *= -1
        ball_velocity_y *= -1
    if ball_x <= 0: # reset the ball position to the center, if it goes out of the screen (LEFT)
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        ball_velocity_x, ball_velocity_y = 0


