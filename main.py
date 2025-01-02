import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Constants
GRID_SIZE = 20  # Number of cells in both x and y directions
CELL_SIZE = 20  # Size of each cell in pixels
WIDTH = GRID_SIZE * CELL_SIZE  # Width of the window in pixels
HEIGHT = GRID_SIZE * CELL_SIZE  # Height of the window in pixels
BACKGROUND_COLOR = (0, 0, 0)  # Black background
GRID_COLOR = (50, 50, 50)  # Grid line color
TEXT_COLOR = (255, 255, 255)  # White text for score

SNAKE_COLOR = (0, 255, 0)  # Green color for the snake body
SNAKE_HEAD_COLOR = (255, 0, 0)  # Red color for the snake head
FOOD_COLOR = (255, 255, 0)  # Yellow color for the food

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Font for displaying score
font = pygame.font.SysFont('arial', 24)

# Direction vectors (right, left, down, up)
DIRECTIONS = {
    'UP': (0, -1),
    'DOWN': (0, 1),
    'LEFT': (-1, 0),
    'RIGHT': (1, 0),
}

# Snake initial position and length
snake = [(5, 5), (4, 5), (3, 5), (2, 5)]  # Snake starts with length 4 at (5, 5)
snake_direction = 'RIGHT'  # Snake initially moves to the right
score = 0

# Food initial position
food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

# Function to draw the grid
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

# Function to draw the score on the screen
def draw_score():
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_text, (10, 10))

# Function to draw the snake
def draw_snake():
    for idx, segment in enumerate(snake):
        x, y = segment
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        if idx == 0:  # Draw head with a different color
            pygame.draw.rect(screen, SNAKE_HEAD_COLOR, rect)
        else:
            pygame.draw.rect(screen, SNAKE_COLOR, rect)

# Function to draw the food
def draw_food():
    x, y = food
    rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(screen, FOOD_COLOR, rect)

# Function to move the snake
def move_snake():
    global score, food
    head_x, head_y = snake[0]
    direction = DIRECTIONS[snake_direction]
    new_head = (head_x + direction[0], head_y + direction[1])

    # Check for collision with the wall
    if new_head[0] < 0 or new_head[0] >= GRID_SIZE or new_head[1] < 0 or new_head[1] >= GRID_SIZE:
        game_over()
        return False  # Stop the game

    # Check if snake eats the food
    if new_head == food:
        # Snake eats the food, increase score and grow snake
        score += 1
        snake.insert(0, new_head)  # Add new head (grows snake)
        # Generate new food
        food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
    else:
        # No food eaten, move snake normally
        snake.insert(0, new_head)  # Add new head
        snake.pop()  # Remove the tail (last segment)

    # Check for collision with snake's own body (excluding the head)
    if new_head in snake[1:]:
        game_over()
        return False  # Stop the game

    return True

# Function to handle user input for snake direction
def handle_input():
    global snake_direction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'

# Function to reset the game state
def reset_game():
    global snake, snake_direction, score, food
    snake = [(5, 5), (4, 5), (3, 5), (2, 5)]  # Reset snake to initial position and length
    snake_direction = 'RIGHT'  # Reset direction to right
    score = 0  # Reset score
    food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))  # Reset food position

# Function to display the game over screen and ask for a new game
def game_over():
    global score
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, TEXT_COLOR)
    new_game_text = font.render("Press 'R' to Restart or 'Q' to Quit", True, TEXT_COLOR)

    screen.fill(BACKGROUND_COLOR)  # Fill the screen with background color
    screen.blit(game_over_text, (WIDTH // 4, HEIGHT // 3))
    screen.blit(new_game_text, (WIDTH // 4, HEIGHT // 2))

    pygame.display.update()

    # Wait for user input to either restart or quit
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game
                    reset_game()
                    waiting_for_input = False
                elif event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    sys.exit()

# Main function to run the game
def main():
    global score

    clock = pygame.time.Clock()

    # Game loop
    while True:
        handle_input()  # Handle user input
        if not move_snake():  # Move the snake, if it collides with the wall or itself, end the game
            continue  # Skip the drawing if game over

        screen.fill(BACKGROUND_COLOR)  # Fill the screen with background color
        draw_grid()  # Draw the grid
        draw_snake()  # Draw the snake
        draw_food()  # Draw the food
        draw_score()  # Draw the score

        pygame.display.update()  # Update the screen

        clock.tick(10)  # Set the game speed (10 frames per second)

if __name__ == '__main__':
    main()
