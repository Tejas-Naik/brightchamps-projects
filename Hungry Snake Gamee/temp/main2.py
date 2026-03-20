import pygame
import random
import math

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = GREEN
        self.direction = (1, 0)
        self.body = [pygame.Rect(x - i * GRID_SIZE, y, GRID_SIZE, GRID_SIZE) for i in range(3)]

    def move(self):
        new_head = self.body[0].copy()
        new_head.x += self.direction[0] * GRID_SIZE
        new_head.y += self.direction[1] * GRID_SIZE
        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1].copy())

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, self.color, segment)

class Food(GameObject):
    def __init__(self):
        super().__init__(0, 0)
        self.color = RED
        self.respawn()

    def respawn(self):
        self.x = random.randint(0, ((WIDTH-20) - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.y = random.randint(0, ((HEIGHT-20) - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.rect = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

class Bomb(GameObject):
    def __init__(self):
        super().__init__(0, 0)
        self.color = BLACK
        self.respawn()

    def respawn(self):
        self.x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.rect = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

class PowerUp(GameObject):
    def __init__(self):
        super().__init__(0, 0)
        self.color = BLUE
        self.active = False
        self.type = random.choice(["speed", "invincibility"])

    def activate(self):
        self.active = True
        self.x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.rect = pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE)

    def deactivate(self):
        self.active = False

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Improved Hungry Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.reset_game()

    def reset_game(self):
        self.snake = Snake(WIDTH // 2, HEIGHT // 2)
        self.food = Food()
        self.bombs = [Bomb() for _ in range(3)]
        self.power_up = PowerUp()
        self.score = 0
        self.game_speed = 10
        self.state = "menu"

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if self.state == "menu" and event.key == pygame.K_SPACE:
                    self.state = "playing"
                elif self.state == "playing":
                    if event.key == pygame.K_UP and self.snake.direction != (0, 1):
                        self.snake.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.snake.direction != (0, -1):
                        self.snake.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and self.snake.direction != (1, 0):
                        self.snake.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and self.snake.direction != (-1, 0):
                        self.snake.direction = (1, 0)
                elif self.state == "game_over" and event.key == pygame.K_SPACE:
                    self.reset_game()
                    self.state = "playing"
        return True

    def update(self):
        if self.state != "playing":
            return

        self.snake.move()

        # Check collision with food
        if self.snake.body[0].colliderect(self.food.rect):
            self.snake.grow()
            self.food.respawn()
            self.score += 1
            if self.score % 5 == 0:
                self.game_speed += 1

        # Check collision with bombs
        for bomb in self.bombs:
            if self.snake.body[0].colliderect(bomb.rect):
                self.state = "game_over"

        # Check collision with power-up
        if self.power_up.active and self.snake.body[0].colliderect(self.power_up.rect):
            if self.power_up.type == "speed":
                self.game_speed += 3
            elif self.power_up.type == "invincibility":
                self.snake.color = BLUE
            self.power_up.deactivate()

        # Check self-collision
        if self.snake.body[0].collidelist(self.snake.body[1:]) != -1:
            self.state = "game_over"

        # Check wall collision
        if (self.snake.body[0].left < 0 or self.snake.body[0].right > WIDTH or
            self.snake.body[0].top < 0 or self.snake.body[0].bottom > HEIGHT):
            self.state = "game_over"

        # Spawn power-up
        if not self.power_up.active and random.random() < 0.005:
            self.power_up.activate()

    def draw(self):
        self.screen.fill(WHITE)

        if self.state == "menu":
            self.draw_menu()
        elif self.state == "playing":
            self.draw_game()
        elif self.state == "game_over":
            self.draw_game_over()

        pygame.display.flip()

    def draw_menu(self):
        title = self.font.render("Hungry Snake Game", True, BLACK)
        start = self.font.render("Press SPACE to start", True, BLACK)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 3))
        self.screen.blit(start, (WIDTH // 2 - start.get_width() // 2, HEIGHT // 2))

    def draw_game(self):
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        for bomb in self.bombs:
            bomb.draw(self.screen)
        if self.power_up.active:
            self.power_up.draw(self.screen)
        
        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        self.screen.blit(score_text, (10, 10))

    def draw_game_over(self):
        game_over = self.font.render("Game Over", True, BLACK)
        score = self.font.render(f"Final Score: {self.score}", True, BLACK)
        restart = self.font.render("Press SPACE to restart", True, BLACK)
        
        self.screen.blit(game_over, (WIDTH // 2 - game_over.get_width() // 2, HEIGHT // 3))
        self.screen.blit(score, (WIDTH // 2 - score.get_width() // 2, HEIGHT // 2))
        self.screen.blit(restart, (WIDTH // 2 - restart.get_width() // 2, HEIGHT * 2 // 3))

    def run(self):
        running = True
        while running:
            self.clock.tick(FPS)
            running = self.handle_events()
            self.update()
            self.draw()

            if self.state == "playing":
                pygame.time.delay(max(50, 150 - self.game_speed * 10))

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()