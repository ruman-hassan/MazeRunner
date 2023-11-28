import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Set the caption
pygame.display.set_caption("Word Maze")

# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Define the maze
maze = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]

# Define the letters
letters = ["H", "E", "L", "L", "O"]

# Define the player's position
player_x = 0
player_y = 0

# Define the goal position
goal_x = 4
goal_y = 4

# Define the font
font = pygame.font.Font(None, 32)

# Define the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_y -= 1
            if event.key == pygame.K_DOWN:
                player_y += 1
            if event.key == pygame.K_LEFT:
                player_x -= 1
            if event.key == pygame.K_RIGHT:
                player_x += 1

    # Check if the player has collided with a wall
    if maze[player_y][player_x] == 1:
        player_x = 0
        player_y = 0

    # Check if the player has collected a letter
    if letters[player_y][player_x] != "":
        new_string = letters[player_y][:player_x] + letters[player_y][player_x + 1:]
        letters[player_y] = new_string

    # Check if the player has reached the goal
    if player_x == goal_x and player_y == goal_y:
        print("You win!")
        running = False

    # Fill the screen with black
    screen.fill(black)

    # Draw the maze
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == 1:
                pygame.draw.rect(screen, white, (x * 100, y * 100, 100, 100))
            else:
                pygame.draw.rect(screen, black, (x * 100, y * 100, 100, 100))

    # Draw the player
    pygame.draw.rect(screen, red, (player_x * 100, player_y * 100, 100, 100))

    # Draw the goal
    pygame.draw.rect(screen, green, (goal_x * 100, goal_y * 100, 100, 100))

    # Display the collected letters
    collected_letters = "".join(letters)
    text = font.render(f"Collected Letters: {collected_letters}", True, white)
    screen.blit(text, (10, 10))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
