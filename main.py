import pygame
import sys
import pandas as pd
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
#
# print("x,y,vx,vy,Paddle.y", file = sample)

pong = pd.read_csv('./game.csv')
pong = pong.drop_duplicates()

from sklearn.neighbors import KNeighborsRegressor

X = pong.drop(columns ="Paddle.y")
y = pong["Paddle.y"]

clf = KNeighborsRegressor(n_neighbors = 3)

clf = clf.fit(X, y)

df = pd.DataFrame(columns=['x','y','vx','vy'])

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

                # Predict y position of paddle
                to_predict = df.append({'x' : ball.x, 'y' : ball.y,
                                        'vx': ball.VELOCITY_X, 'vy' : ball.VELOCITY_Y}, ignore_index = True)
                new_paddle_y_pos = clf.predict(to_predict)
                new_paddle_y_pos = float(new_paddle_y_pos[0])
                paddle.y = new_paddle_y_pos

                # Draw paddle
                paddle.draw(screen)

                # Draw wall
                wall.draw(screen, SCREEN_WIDTH, SCREEN_HEIGHT)

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
