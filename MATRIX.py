import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Set up colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set up the snake
snake_size = 20
snake_speed = 15
x_pos = width // 2
y_pos = height // 2
x_change = 0
y_change = 0

snake_body = []
snake_length = 1

# Set up the game clock
clock = pygame.time.Clock()

game_over = False

# Function to display the snake
def draw_snake(snake_body):
    for x in snake_body:
        pygame.draw.rect(window, GREEN, [x[0], x[1], snake_size, snake_size])

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_size
                y_change = 0
            elif event.key == pygame.K_UP:
                y_change = -snake_size
                x_change = 0
            elif event.key == pygame.K_DOWN:
                y_change = snake_size
                x_change = 0

    # Update snake position
    x_pos += x_change
    y_pos += y_change

    # Check for boundaries
    if x_pos >= width or x_pos < 0 or y_pos >= height or y_pos < 0:
        game_over = True

    # Clear the screen
    window.fill(BLACK)

    # Update snake body
    snake_head = []
    snake_head.append(x_pos)
    snake_head.append(y_pos)
    snake_body.append(snake_head)

    if len(snake_body) > snake_length:
        del snake_body[0]

    # Check for self-collision
    for x in snake_body[:-1]:
        if x == snake_head:
            game_over = True

    # Draw the snake
    draw_snake(snake_body)

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()
