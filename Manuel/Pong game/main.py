# Import modules
import pygame, sys
from pygame.locals import QUIT

# Initializes Pygame 
pygame.init()

# Set up the window
window_width, window_height = 400, 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Ping Pong')

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Paddle
paddle_width, paddle_height = 80, 10
paddle_x, paddle_y = (window_width - paddle_width) // 2, window_height - paddle_height - 10

# Ball
ball_radius = 5
ball_x, ball_y = window_width // 2, window_height // 2
ball_speed_x, ball_speed_y = 3, -3

# Score
score = 0

# Font for displaying score
font = pygame.font.Font(None, 36)

# Game loop
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddle with left and right arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= 5
    if keys[pygame.K_RIGHT] and paddle_x < window_width - paddle_width:
        paddle_x += 5

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Draw everything
    window.fill(WHITE)  
    paddle = pygame.draw.rect(window, GREEN, (paddle_x, paddle_y, paddle_width, paddle_height))  
    ball = pygame.draw.circle(window, BLACK, (ball_x, ball_y), ball_radius)

    # Display the score
    score_text = font.render("Score: " + str(score), True, BLACK)
    window.blit(score_text, (10, 10))

    pygame.display.update()


    # Ball collisions with walls
    if ball.left <= 0 or ball.right >= window_width:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    # Ball collisions with paddle using colliderect
    if pygame.Rect.colliderect(ball, paddle):
        ball_speed_y *= -1
        score += 1

    # Check if the ball touches the bottom line
    if ball.bottom >= window_height:
        game_over = True

  # Control the game's speed (adjust this value to change the game's speed)
    pygame.time.delay(30)

# Clear the screen and display the "Game Over" message in the middle
window.fill(WHITE)
score_text = font.render("Score: " + str(score), True, BLACK)
window.blit(score_text, (10, 10))
game_over_text = font.render("Game Over", True, BLACK)
window.blit(game_over_text, ((window_width - game_over_text.get_width()) // 2, (window_height- game_over_text.get_height())//2))
pygame.display.update()

# Wait for a few seconds before closing the window
pygame.time.delay(2000)
# Game over, quit Pygame
pygame.quit()
sys.exit()
