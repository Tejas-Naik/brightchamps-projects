import pygame, sys
from pygame.locals import QUIT

# Initialize Pygame
pygame.init()

# Set up the window
window_width, window_height = 600, 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ping Pong - 2 Player")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Paddle dimensions and speed
paddle_width, paddle_height = 20, 100
paddle_speed = 5

# Paddle positions
blue_paddle_x, blue_paddle_y = 50, window_height // 2 - paddle_height // 2
red_paddle_x, red_paddle_y = window_width - 50 - paddle_width, window_height // 2 - paddle_height // 2

# Ball dimensions and speed
ball_radius = 10
ball_speed_x, ball_speed_y = 5, 5

# Ball position
ball_x, ball_y = window_width // 2, window_height // 2

# Lives
blue_lives, red_lives = 3, 3

# Font for displaying lives
font = pygame.font.Font(None, 36)

# Load the background image
background_image = pygame.image.load("ping_pong.png").convert()  

# Game loop
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Blit the background image onto the window
    window.blit(background_image, (0, 0))

    # Clear the screen and draw everything
    blue_paddle = pygame.draw.rect(window, BLUE, (blue_paddle_x, blue_paddle_y, paddle_width, paddle_height))
    red_paddle = pygame.draw.rect(window, RED, (red_paddle_x, red_paddle_y, paddle_width, paddle_height))
    ball = pygame.draw.circle(window, BLACK, (ball_x, ball_y), ball_radius) 

    # Ball collisions with walls
    if ball.top < 0 or ball.bottom > window_height:
        ball_speed_y *= -1

    # Ball collisions with paddles
    if pygame.Rect.colliderect(ball, blue_paddle):
        ball_speed_x *= -1

    if pygame.Rect.colliderect(ball, red_paddle):
        ball_speed_x *= -1
      
    # Move paddles based on input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and blue_paddle.top > 0:
        blue_paddle_y -= paddle_speed
    if keys[pygame.K_s] and blue_paddle.bottom < window_height:
        blue_paddle_y += paddle_speed

    if keys[pygame.K_UP] and red_paddle.top > 0:
        red_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and red_paddle.bottom < window_height:
        red_paddle_y += paddle_speed

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Check if ball goes out of bounds deduct live and reset ball position
    if ball.left <= 0:
        blue_lives -= 1
        ball_x, ball_y = window_width // 2, window_height // 2
    elif ball.right >= window_width:    
        red_lives -= 1
        ball_x, ball_y = window_width // 2, window_height // 2
      
    # Display the lives
    blue_lives_text = font.render("Player Blue: " + str(blue_lives), True, BLACK)
    red_lives_text = font.render("Player Red: " + str(red_lives), True, BLACK)
    window.blit(blue_lives_text, (20, 20))
    window.blit(red_lives_text, (window_width - red_lives_text.get_width() - 20, 20))

    pygame.display.update()

    # Control the game's speed (adjust this value to change the game's speed)
    pygame.time.delay(30)

    # Check if any player has won (reached a certain score)
    if blue_lives == 0 or red_lives == 0:
        game_over = True

# Display the winner
winner_text = font.render("Player Red Wins!" if blue_lives == 0 else "Player Blue Wins!", True, BLACK)
window.blit(winner_text, ((window_width - winner_text.get_width()) // 2, (window_height - winner_text.get_height()) // 2))
pygame.display.update()

# Wait for a few seconds before closing the window
pygame.time.delay(3000)

# Close the Pygame window and quit
pygame.quit()
sys.exit()
