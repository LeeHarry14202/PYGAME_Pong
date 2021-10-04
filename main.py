import pygame
import sys
import my_class
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BORDER = 20

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

# Object init
world = my_class.WORLD()
COLOR = my_class.COLOR()
ball = my_class.BALL(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
wall = my_class.WALL()
paddle = my_class.PADDLE(SCREEN_WIDTH - BORDER, SCREEN_HEIGHT / 2)

while True:
    screen.fill(COLOR.BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                paddle.direction = 'UP'
            if event.key == pygame.K_DOWN:
                paddle.direction = 'DOWN'

        # Draw Ball
        ball.draw()

        # Draw wall
        wall.draw(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

        # Draw paddle
        paddle.draw(screen)

        pygame.display.update()
        clock.tick(60)
