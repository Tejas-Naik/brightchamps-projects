import pygame
import sys
import math
from pygame.locals import QUIT, MOUSEBUTTONDOWN

# Initialize Pygame
pygame.init()

# Set up the window
window_width, window_height = 600, 400
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Fidget Spinner")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load the background image and resize it to fit the window
background_image = pygame.image.load("background.png").convert()
background_image = pygame.transform.scale(background_image, (window_width, window_height))

# Load the spinner images and resize them
spinner_images = [
    pygame.image.load("fidgetspinner1.png").convert_alpha(),
    pygame.image.load("fidgetspinner2.png").convert_alpha(),
    pygame.image.load("fidgetspinner3.png").convert_alpha()
]

spinner_width, spinner_height = 300, 300  # Desired spinner dimensions
spinner_images = [pygame.transform.scale(image, (spinner_width, spinner_height)) for image in spinner_images]

# Spinner position and rotation
spinner_x, spinner_y = window_width // 2, window_height // 2
spinner_rotation = 0

# Spinner speed and index 
spinner_rotation_speed = 0
current_spinner = 0

# Font for displaying speed
font = pygame.font.Font(None, 24)

# Function to change the spinner option
def change_spinner():
    global current_spinner
    current_spinner += 1
    if current_spinner >= len(spinner_images):
        current_spinner = 0

# Game loop
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            change_spinner()

    # Rotate the spinner based on mouse movement
    mouse_x, mouse_y = pygame.mouse.get_pos()
    angle = math.atan2(mouse_y - spinner_y, mouse_x - spinner_x)
    spinner_rotation_speed = math.degrees(angle)  # Convert radians to degrees

    # Rotate the spinner image
    spinner_rotation += spinner_rotation_speed
    rotated_spinner = pygame.transform.rotate(spinner_images[current_spinner], -spinner_rotation)
    spinner_rect = rotated_spinner.get_rect(center=(spinner_x, spinner_y))
  
    # Draw the background image
    window.blit(background_image, (0, 0))

    # Draw the rotated spinner image on top of the background
    window.blit(rotated_spinner, spinner_rect)
  
    # Display the selected spinner number
    spinner_text = font.render("Spinner: {}".format(current_spinner + 1), True, BLACK)
    window.blit(spinner_text, (10, window_height - 30))

    pygame.display.update()

    # Control the game's speed (adjust this value to change the game's speed)
    pygame.time.delay(30)

# Close the Pygame window and quit
pygame.quit()
sys.exit()
