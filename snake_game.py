import pygame
import random
import sys

# Initialize Pygame 
pygame.init()

# Set up game window
window_width = 600
window_height = 600 
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_pos = [random.randrange(1, window_width/10)*10, 
            random.randrange(1, window_height/10)*10]
food_spawn = True
direction = 'RIGHT'
change_direction = direction
score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Validate direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and change_direction != 'DOWN':
                change_direction = 'UP'
            elif event.key == pygame.K_DOWN and change_direction != 'UP':
                change_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and change_direction != 'RIGHT':
                change_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and change_direction != 'LEFT':
                change_direction = 'RIGHT'

    # Update snake position        
    if change_direction == 'UP':
        snake_pos[1] -= 10
    if change_direction == 'DOWN':
        snake_pos[1] += 10
    if change_direction == 'LEFT':
        snake_pos[0] -= 10
    if change_direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn food
    if not food_spawn:
        food_pos = [random.randrange(1, window_width/10)*10, 
                    random.randrange(1, window_height/10)*10]
        food_spawn = True

    # Game over
    if snake_pos[0] < 0 or snake_pos[0] > window_width-10:
        pygame.quit()
        sys.exit() 
    if snake_pos[1] < 0 or snake_pos[1] > window_height-10:
        pygame.quit()
        sys.exit()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            pygame.quit()
            sys.exit()

    # Draw elements on screen
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(
            pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, red, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

    # Update screen
    pygame.display.flip()

    # Refresh rate
    pygame.time.Clock().tick(10)