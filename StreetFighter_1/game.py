import pygame

pygame.init()

black = 0,0,0
white = 255,255,255
blue = 0,0,255
color_1 = 100,200,150

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

class Player_1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)
        self.moveX = 0

    def update(self):
        keypressd = pygame.key.get_pressed()
        if keypressd[pygame.K_RIGHT]:
            self.moveX = 1
        elif keypressd[pygame.K_LEFT]:
            self.moveX = -1
        else:
            self.moveX = 0
        self.rect.x += self.moveX

all_groups = pygame.sprite.Group()

player_1 = Player_1()
sprite_1 = pygame.sprite.Group()

sprite_1.add(player_1)
all_groups.add(player_1)

while True:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(color_1)

    all_groups.draw(screen)
    all_groups.update()

    pygame.display.update()