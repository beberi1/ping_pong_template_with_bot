import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
BALL_SPEED = [10, 10]
PADDLE_SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Define the paddles and the ball
# where will spawn in x axis,where will spawn in y axis, width, height
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 10, 10)
player_paddle = pygame.Rect(60, HEIGHT // 2 - 60, 10, 120)
opponent_paddle = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 60, 10, 120)

# Initialize the ball's direction
ball_dx, ball_dy = BALL_SPEED

# Initialize scores
player_score = 0
opponent_score = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move Player 1's paddle (the bot) to track the ball's vertical position
    if player_paddle.centery < ball.centery:
        player_paddle.y += PADDLE_SPEED
    elif player_paddle.centery > ball.centery:
        player_paddle.y -= PADDLE_SPEED

    # Move Player 2's paddle with arrow keys, up and down
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and opponent_paddle.top > 0:
        opponent_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and opponent_paddle.bottom < HEIGHT:
        opponent_paddle.y += PADDLE_SPEED

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Ball collisions
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1

    if ball.colliderect(player_paddle) or ball.colliderect(opponent_paddle):
        ball_dx *= -1

    if ball.left < 50:
        # Ball out of bounds, opponent scores a point
        opponent_score += 1
        ball.x = WIDTH // 2 - 15
        ball.y = HEIGHT // 2 - 15
        ball_dx *= -1
        print("Opponent scores a point. Player: {}, Opponent: {}".format(player_score, opponent_score))

    if ball.right > WIDTH-50:
        # Ball out of bounds, player scores a point
        player_score += 1
        ball.x = WIDTH // 2 - 15
        ball.y = HEIGHT // 2 - 15
        ball_dx *= -1
        print("Player scores a point. Player: {}, Opponent: {}".format(player_score, opponent_score))

    # Clear the screen
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, player_paddle)
    pygame.draw.rect(screen, WHITE, opponent_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    pygame.time.delay(30)
