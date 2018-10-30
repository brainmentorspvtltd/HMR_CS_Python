import pygame
import random

pygame.init()

yellow = 255,255,0

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

bgImage = pygame.image.load("images/background.png")

shootSound = pygame.mixer.Sound('sounds/shot_sound.wav')

zombies = []
for i in range(4):
    img = pygame.image.load("images/zombie_{}.png".format(i+1))
    zombies.append(img)

zombieImage = random.choice(zombies)
zombieImageWidth = zombieImage.get_width()
zombieImageHeight = zombieImage.get_height()
zombieX = random.randint(0, width - zombieImageWidth)
zombieY = random.randint(0, height - zombieImageHeight)

gun_pointer = pygame.image.load("images/aim_pointer.png")
pointer_width = gun_pointer.get_width()
pointer_height = gun_pointer.get_height()

gunImage = pygame.image.load("images/gun_1.png")

counter = 0
def score(c):
    # font = pygame.font.SysFont(None,40)
    font = pygame.font.Font('font_1.ttf', 40)
    text = font.render('Score : {}'.format(c), True, yellow)
    screen.blit(text, (10,10))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            shootSound.play()
            if zombieRect.colliderect(gunPointerRect):
                zombieImage = random.choice(zombies)
                zombieImageWidth = zombieImage.get_width()
                zombieImageHeight = zombieImage.get_height()
                zombieX = random.randint(0, width - zombieImageWidth)
                zombieY = random.randint(0, height - zombieImageHeight)
                counter += 1

    posx, posy = pygame.mouse.get_pos()

    screen.blit(bgImage, (0,0))
    screen.blit(zombieImage, (zombieX, zombieY))
    screen.blit(gun_pointer, (posx - pointer_width/2, posy - pointer_height/2))
    screen.blit(gunImage, (posx, height - 250))

    zombieRect = pygame.Rect(zombieX, zombieY, zombieImageWidth, zombieImageHeight)
    gunPointerRect = pygame.Rect(posx - pointer_width/2, posy - pointer_height/2, pointer_width, pointer_height)

    score(counter)

    pygame.display.update()







