import pygame

pygame.init()

black = 0,0,0
white = 255,255,255
blue = 0,0,255
color_1 = 100,200,150

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball_2.png")

x = 0
y = 0
moveX = 1
moveY = 1
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(color_1)
    screen.blit(ball, (x,y))

    x += moveX
    y += moveY

    if x > width - ball.get_width():
        moveX = -1
    elif x < 0:
        moveX = 1
    elif y > height - ball.get_height():
        moveY = -1
    elif y < 0:
        moveY = 1

    pygame.display.update()