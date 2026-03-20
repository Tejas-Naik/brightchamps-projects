# Import required modules
import pygame
import random
import sys
import os

# Get the absolute path to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Initialize the Pygame mixer before the main pygame init.
# This is a common fix for sound issues on macOS.
pygame.mixer.pre_init(44100, -16, 2, 512)

# Initialize the Pygame library
pygame.init()

# Set up the game window dimensions
window_width, window_height = 400, 300
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Simon Says')

# Load images and sounds for superheroes
SUPERHEROES = {
  1: {
    'image': pygame.transform.scale(pygame.image.load(os.path.join(script_dir, 'superman.png')),
                                    (50, 100)),
    'sound': pygame.mixer.Sound(os.path.join(script_dir, 'superman.wav'))
  },
  2: {
    'image': pygame.transform.scale(pygame.image.load(os.path.join(script_dir, 'ironman.png')),
                                    (50, 100)),
    'sound': pygame.mixer.Sound(os.path.join(script_dir, 'ironman.wav'))
  },
  3: {
    'image': pygame.transform.scale(pygame.image.load(os.path.join(script_dir, 'batman.png')),
                                    (50, 100)),
    'sound': pygame.mixer.Sound(os.path.join(script_dir, 'batman.wav'))
  },
  4: {
    'image':
    pygame.transform.scale(pygame.image.load(os.path.join(script_dir, 'spiderman.png')), (50, 100)),
    'sound':
    pygame.mixer.Sound(os.path.join(script_dir, 'spiderman.wav'))
  },
}

# List to store the generated sequence
sequence = []


# Function to display a message on the screen
def display_message(message):
  font = pygame.font.SysFont(None, 30)
  text = font.render(message, True, (0, 0, 0))
  text_rect = text.get_rect(center=(window_width // 2, window_height // 4))
  window.fill((255, 255, 255))
  window.blit(text, text_rect)
  pygame.display.update()


# Function to display the superhero images at the bottom of the screen
def display_superhero_images():
  for i in range(1, 5):
    window.blit(SUPERHEROES[i]['image'], ((i - 1) * 100 + 25, 150))
  pygame.display.update()


# Function to play the sequence of sounds and images
def play_sequence(length):
  global sequence
  sequence = [random.randint(1, 4) for _ in range(length)
              ]  # Generate a sequence of random superheroes

  # Display the message to listen and remember the sequence
  display_message("Listen the sequence!")

  # Play the sounds in the sequence
  for superhero_num in sequence:
    SUPERHEROES[superhero_num]['sound'].play()
    pygame.time.delay(1000)

  display_message("Your turn to repeat the sequence!")
  display_superhero_images()


# Function to play the sequence and get the player's response
def play_sound_and_get_response():
  global sequence

  # Increase the sequence length by one
  sequence_length = len(sequence) + 1

  # Play the sequence
  play_sequence(sequence_length)

  player_sequence = []
  # Wait for the player's response
  while len(player_sequence) < len(sequence):
    waiting_for_input = True
    while waiting_for_input:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_x, mouse_y = pygame.mouse.get_pos()
          clicked_superhero = None
          # Check which superhero was clicked
          for i in range(1, 5):
            image_rect = SUPERHEROES[i]['image'].get_rect(topleft=((i - 1) * 100 + 25, 150))
            if image_rect.collidepoint(mouse_x, mouse_y):
              clicked_superhero = i
              SUPERHEROES[i]['sound'].play() # Play sound on click for feedback
              break
          
          if clicked_superhero and clicked_superhero == sequence[len(player_sequence)]:
            player_sequence.append(clicked_superhero)
            waiting_for_input = False # Move to next input
          elif clicked_superhero: # Clicked the wrong one
            return False # Game over

  return True  # Correct sequence, continue the game


# Main game loop
gameover = False
while not gameover:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      gameover = True

  # Play sound and get player's response
  correct_sequence = play_sound_and_get_response()

  if correct_sequence:
    display_message("Correct sequence! Well done!")
    pygame.time.delay(1500)
  else:
    display_message("Wrong sequence! Game over.")
    pygame.time.delay(2000)
    gameover = True

# Quit the Pygame library and exit the program
pygame.quit()
sys.exit()
