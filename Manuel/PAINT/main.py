import pygame
from pygame.locals import QUIT

# Initialize Pygame
pygame.init()

# Constants for WINDOW dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TOOLBAR_HEIGHT = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Create the WINDOW
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("PAINT")

# Variables
drawing = False
brush_size = 2
min_brush_size = 1
max_brush_size = 10
brush_color = BLACK
eraser_mode = False
last_pos = None

# Create a surface for drawing (same as the WINDOW size)
canvas = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT - TOOLBAR_HEIGHT))
canvas.fill(WHITE)

# Create a surface for the toolbar
toolbar = pygame.Surface((WINDOW_WIDTH, TOOLBAR_HEIGHT))
toolbar.fill(GRAY)

# Main game loop
running = True
while running:
    # Draw the toolbar
    toolbar.fill(GRAY)
    font = pygame.font.Font(None, 24)  # Adjust font size
    pen_text = font.render("P", True, BLACK)
    eraser_text = font.render("E", True, BLACK)
    decrease_text = font.render("-", True, BLACK)
    increase_text = font.render("+", True, BLACK)
    clear_text = font.render("C", True, BLACK)
    toolbar.blit(pen_text, (40, 20))
    toolbar.blit(eraser_text, (80, 20))
    toolbar.blit(decrease_text, (120, 20))
    toolbar.blit(increase_text, (160, 20))
    toolbar.blit(clear_text, (200, 20))

    # Draw the color selection buttons
    color_button_width = 20
    color_button_height = 20
    black_color_button = pygame.draw.circle(toolbar, BLACK, (240, 25), color_button_width // 2)  # Black color button
    red_color_button = pygame.draw.circle(toolbar, RED, (280, 25), color_button_width // 2)    # Red color button
    yellow_color_button = pygame.draw.circle(toolbar, YELLOW, (320, 25), color_button_width // 2) # Yellow color button
    blue_color_button = pygame.draw.circle(toolbar, BLUE, (360, 25), color_button_width // 2)   # Blue color button

    # Fill the WINDOW with white color
    WINDOW.fill(WHITE)

    # Draw the canvas and toolbar on the WINDOW
    WINDOW.blit(canvas, (0, TOOLBAR_HEIGHT))
    WINDOW.blit(toolbar, (0, 0))

    # Handle the Events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] <= TOOLBAR_HEIGHT:  # Check if the click is on the toolbar
                pen_rect = pen_text.get_rect(topleft=(40, 20))
                eraser_rect = eraser_text.get_rect(topleft=(80, 20))
                decrease_rect = decrease_text.get_rect(topleft=(120, 20))
                increase_rect = increase_text.get_rect(topleft=(160, 20))
                clear_rect = clear_text.get_rect(topleft=(200, 20))

                if pen_rect.collidepoint(event.pos):
                    # Pen tool selected
                    eraser_mode = False
                elif eraser_rect.collidepoint(event.pos):
                    # Eraser tool selected
                    eraser_mode = True
                elif decrease_rect.collidepoint(event.pos):
                    # Decrease brush size
                    brush_size = max(min_brush_size, brush_size - 1)
                elif increase_rect.collidepoint(event.pos):
                    # Increase brush size
                    brush_size = min(max_brush_size, brush_size + 1)
                elif clear_rect.collidepoint(event.pos):
                    # Clear button clicked
                    canvas.fill(WHITE)
                elif black_color_button.collidepoint(event.pos):
                    # Black color selected
                    brush_color = BLACK
                elif red_color_button.collidepoint(event.pos):
                    # Red color selected
                    brush_color = RED
                elif yellow_color_button.collidepoint(event.pos):
                    # Yellow color selected
                    brush_color = YELLOW
                elif blue_color_button.collidepoint(event.pos):
                    # Blue color selected
                    brush_color = BLUE
            else:
                drawing = True
                last_pos = (event.pos[0], event.pos[1] - TOOLBAR_HEIGHT)  # Adjust last_pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            last_pos = None  # Reset last_pos when not drawing
        elif event.type == pygame.MOUSEMOTION and drawing:
            color = brush_color if not eraser_mode else WHITE
            pygame.draw.line(canvas, color, last_pos, (event.pos[0], event.pos[1] - TOOLBAR_HEIGHT), brush_size)
            last_pos = (event.pos[0], event.pos[1] - TOOLBAR_HEIGHT)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

