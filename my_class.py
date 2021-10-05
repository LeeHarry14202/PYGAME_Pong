import pygame.draw

BORDER = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class WORLD:
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.game_status = True

    def restart(self, ball, paddle):

        ball.x = SCREEN_WIDTH / 2
        ball.y = SCREEN_HEIGHT / 2
        ball.VELOCITY_X *= -1
        ball.VELOCITY_Y *= -1

        paddle.x = SCREEN_WIDTH - BORDER
        paddle.y = SCREEN_HEIGHT / 2

        # self.game_status = True


class COLOR:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)


class BALL:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.VELOCITY_X = -5
        self.VELOCITY_Y = -5
        self.RADIUS = 15
        self.rect = pygame.Rect(self.x, self.y, self.RADIUS * 2, self.RADIUS * 2)

    def draw(self):
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.update()
        pygame.draw.circle(screen, COLOR.RED, (self.x, self.y), self.RADIUS)

    def update(self):
        newx = self.x + self.VELOCITY_X
        newy = self.y + self.VELOCITY_Y

        # Reverse velocity
        if newx < BORDER + self.RADIUS:
            self.VELOCITY_X *= -1
        elif newy < BORDER + self.RADIUS or newy > SCREEN_HEIGHT - BORDER - self.RADIUS:
            self.VELOCITY_Y *= - 1
        else:
            self.x += self.VELOCITY_X
            self.y += self.VELOCITY_Y
        # Update ball rect
        self.rect = pygame.Rect(self.x, self.y, self.RADIUS * 2, self.RADIUS * 2)


class PADDLE:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.WIDTH = 20
        self.HEIGHT = 150
        self.direction = 'UP'
        self.rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)

    def draw(self, screen):
        self.update()
        pygame.draw.rect(screen, COLOR.WHITE, self.rect)

    def update(self):
        if self.direction == 'UP':
            self.y -= 5
            if self.y <= 0 + BORDER:
                self.direction = 'DOWN'
        if self.direction == 'DOWN':
            self.y += 5
            if self.y > SCREEN_HEIGHT - BORDER:
                self.direction = 'UP'
        # Update paddle rect
        self.rect = pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)


class WALL:
    def __init__(self):
        global BORDER

    def draw(self, screen, width, height):
        pygame.draw.rect(screen, COLOR.WHITE, pygame.Rect(0, 0, width, BORDER))
        pygame.draw.rect(screen, COLOR.WHITE, pygame.Rect(0, 0, BORDER, height))
        pygame.draw.rect(screen, COLOR.WHITE, pygame.Rect(0, height - BORDER, width, BORDER))
