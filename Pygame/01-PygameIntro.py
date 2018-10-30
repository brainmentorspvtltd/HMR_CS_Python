import pygame

pygame.init()

black = 0,0,0
white = 255,255,255
blue = 0,0,255
color_1 = 100,200,150

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

while True:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(color_1)

    pygame.display.update()