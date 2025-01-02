import pygame
import sys

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

# Function to draw the grid
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)

# Function to draw the score on the screen
def draw_score(score):
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

# Function to move the snake
def move_snake():
    global snake_direction
    head_x, head_y = snake[0]
    direction = DIRECTIONS[snake_direction]
    new_head = (head_x + direction[0], head_y + direction[1])

    # Add new head to the snake
    snake.insert(0, new_head)
    # Remove the tail (last segment)
    snake.pop()

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

# Main function to run the game
def main():
    clock = pygame.time.Clock()
    score = 0

    # Game loop
    while True:
        handle_input()  # Handle user input
        move_snake()  # Move the snake

        screen.fill(BACKGROUND_COLOR)  # Fill the screen with background color
        draw_grid()  # Draw the grid
        draw_snake()  # Draw the snake
        draw_score(score)  # Draw the score

        pygame.display.update()  # Update the screen

        clock.tick(10)  # Set the game speed (10 frames per second)

if __name__ == '__main__':
    main()
