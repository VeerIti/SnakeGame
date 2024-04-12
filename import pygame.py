import pygame
import time
import random

pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Snake initial position and speed
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_dir = 'RIGHT'
change_to = snake_dir
speed = 15

# Food initial position
food_pos = [random.randrange(1, (WIDTH//10)) * 10,
            random.randrange(1, (HEIGHT//10)) * 10]

food_spawn = True

# Initial game score
score = 0

# Game Over Flag
game_over = False

# Game Loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Validate direction
    if change_to == 'UP' and not snake_dir == 'DOWN':
        snake_dir = 'UP'
    if change_to == 'DOWN' and not snake_dir == 'UP':
        snake_dir = 'DOWN'
    if change_to == 'LEFT' and not snake_dir == 'RIGHT':
        snake_dir = 'LEFT'
    if change_to == 'RIGHT' and not snake_dir == 'LEFT':
        snake_dir = 'RIGHT'

    # Move the snake in the current direction
    if snake_dir == 'UP':
        snake_pos[1] -= 10
    if snake_dir == 'DOWN':
        snake_pos[1] += 10
    if snake_dir == 'LEFT':
        snake_pos[0] -= 10
    if snake_dir == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    # if food and snake collide then scores increase by 10
    # and new food will be generated
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 10
        food_spawn = False
    else:
        snake_body.pop()
         
    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH//10)) * 10,
                    random.randrange(1, (HEIGHT//10)) * 10]
        food_spawn = True

    # Check if snake hits the border
    if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
        game_over = True

    WIN.fill(BLACK)
    
    # Draw the snake
    for block in snake_body:
        pygame.draw.rect(WIN, GREEN, pygame.Rect(
            block[0], block[1], 10, 10))
    
    # Draw the food
    pygame.draw.rect(WIN, RED, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # Draw the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    WIN.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()
    
    # Refresh rate
    pygame.time.Clock().tick(speed)

# Display "Game Over" message
font = pygame.font.Font(None, 74)
game_over_text = font.render("Game Over", True, WHITE)
WIN.blit(game_over_text, (WIDTH//2 - 200, HEIGHT//2 - 37))
pygame.display.flip()

# Wait for a few seconds before quitting
time.sleep(3)

pygame.quit()
