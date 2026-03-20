import pygame
import random
pygame.init()


dis_width =800
dis_height =600


screen = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Coin Collecter")

bg_image = pygame.image.load("Images/bg.jpg")
bg_image = pygame.transform.scale(bg_image, (800,600))
sprite = pygame.image.load("Images/character.png")
sprite = pygame.transform.scale(sprite, (100,100))
coin = pygame.image.load("Images/coin.jpg")
coin = pygame.transform.scale(coin, (40,40))

sprite_width = sprite.get_width()
sprite_height = sprite.get_height()
sprite_x = dis_width // 2 - sprite_width // 2
sprite_y = dis_height - sprite_height - 40

coin_width = coin.get_width()
coin_height = coin.get_height()
coin_x = random.randint(0, dis_width - coin_width)
coin_y = 50

clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 36)
player_speed = 5
coin_speed = 4

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and sprite_x > 0:
        sprite_x -= player_speed
    if keys[pygame.K_RIGHT] and sprite_x < dis_width - sprite_width:
        sprite_x += player_speed

    # Coin Movement
    coin_y += coin_speed
    if coin_y > dis_height:
        coin_y = -50
        coin_x = random.randint(0, dis_width - coin_width)

    # Collision Detection
    player_rect = pygame.Rect(sprite_x, sprite_y, sprite_width, sprite_height)
    coin_rect = pygame.Rect(coin_x, coin_y, coin_width, coin_height)
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_y = -50
        coin_x = random.randint(0, dis_width - coin_width)
        coin_speed += 0.5

    screen.blit(bg_image, (0, 0))
    screen.blit(sprite, (sprite_x, sprite_y))
    screen.blit (coin, (coin_x, coin_y))
    
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)



pygame.quit()
