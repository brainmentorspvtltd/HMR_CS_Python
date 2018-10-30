import pygame, random
pygame.init()

width = 1000
height = 500
red = 255,0,0

screen = pygame.display.set_mode((width, height))

class Ball():
    def __init__(self):
        self.x = 0
        self.y = 0

        self.moveX = random.randint(0,4)
        self.moveY = random.randint(0,4)

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - 50:
            self.moveX = -(random.randint(0, 4))
        elif self.x < 50:
            self.moveX = random.randint(0, 4)
        elif self.y > height - 50:
            self.moveY = -(random.randint(0, 4))
        elif self.y < 50:
            self.moveY = random.randint(0, 4)

# ball_1 = Ball()
# ball_2 = Ball()
ballList = []
for i in range(100):
    ball = Ball()
    ballList.append(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # This will quit pygame
            pygame.quit()
            # This will quit python
            quit()

    screen.fill((255,255,255))

    # pygame.draw.circle(screen, red, [ball_1.x, ball_1.y], 50)
    # ball_1.update()
    #
    # pygame.draw.circle(screen, red, [ball_2.x, ball_2.y], 50)
    # ball_2.update()

    for i in range(len(ballList)):
        pygame.draw.circle(screen, red, [ballList[i].x ,
                                         ballList[i].y], 50)
        ballList[i].update()

    pygame.display.update()