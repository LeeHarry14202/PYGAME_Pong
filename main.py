import pygame
import sys
import my_class

pygame.init()

SCREEN_WIDTH = my_class.SCREEN_WIDTH
SCREEN_HEIGHT = my_class.SCREEN_HEIGHT
BORDER = my_class.BORDER

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()

# Object init
world = my_class.WORLD()
color = my_class.COLOR()
ball = my_class.BALL(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
wall = my_class.WALL()
paddle = my_class.PADDLE(SCREEN_WIDTH - BORDER, SCREEN_HEIGHT / 2)

# sample = open("game.csv", "w")

# print("x,t,vx,vy,Paddle.y", file = sample)


def main():
    while True:
        screen.fill(color.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Press ESC to exit
                if world.game_status:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                    if event.key == pygame.K_UP:
                        paddle.direction = 'UP'
                    if event.key == pygame.K_DOWN:
                        paddle.direction = 'DOWN'
                # else:
                #     # Press SPACE to restart
                #     if event.key == pygame.K_SPACE and world.game_status is False:
                #         world.restart(ball, paddle)

            if world.game_status:
                # Draw Ball
                ball.draw()

                # Draw wall
                wall.draw(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

                # Draw paddle
                paddle.draw(screen)

                # Check collision
                if ball.rect.colliderect(paddle.rect):
                    ball.VELOCITY_X *= -1

                if ball.x > SCREEN_WIDTH - BORDER:
                    world.restart(ball, paddle)

                # Collect data
                # print("{},{},{},{},{}".format(ball.x, ball.y, ball.VELOCITY_X, ball.VELOCITY_Y, paddle.y), file = sample)

            pygame.display.update()
            clock.tick(90)


if __name__ == "__main__":
    main()
