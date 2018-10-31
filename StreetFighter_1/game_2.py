import pygame
import time

pygame.init()

black = 0,0,0
white = 255,255,255
blue = 0,0,255
color_1 = 100,200,150

width = 1200
height = 550
screen = pygame.display.set_mode((width, height))

class Spritesheet(pygame.sprite.Sprite):
    def __init__(self, filename):
        super().__init__()
        self.file = filename
    def getSprite(self,x,y,w,h):
        image = pygame.Surface((width, height))
        image.blit(self.file, (0, 0), (x, y, w, h))
        image.set_colorkey(black)

        return image

class Player_1(pygame.sprite.Sprite):

    walkingFrames = []
    standingFrames = []
    punchFrames = []
    kickFrames = []

    def __init__(self):
        super().__init__()

        sprite = Spritesheet(ken)

        self.image = sprite.getSprite(48, 247, 106, 239)
        self.standingFrames.append(self.image)
        self.image = sprite.getSprite(264, 240, 113, 249)
        self.standingFrames.append(self.image)
        self.image = sprite.getSprite(482, 248, 106, 237)
        self.standingFrames.append(self.image)
        self.image = sprite.getSprite(687, 247, 112, 241)
        self.standingFrames.append(self.image)

        self.image = sprite.getSprite(42, 247, 116, 243)
        self.walkingFrames.append(self.image)
        self.image = sprite.getSprite(44, 731, 118, 243)
        self.walkingFrames.append(self.image)
        self.image = sprite.getSprite(256, 731, 118, 243)
        self.walkingFrames.append(self.image)

        self.image = sprite.getSprite(42, 490, 118, 240)
        self.punchFrames.append(self.image)
        self.image = sprite.getSprite(260, 489, 166, 240)
        self.punchFrames.append(self.image)
        self.image = sprite.getSprite(472, 487, 122, 245)
        self.punchFrames.append(self.image)

        self.rect = self.image.get_rect()
        self.rect.x = width / 2 - 300
        self.rect.y = height / 2
        self.moveX = 0
        self.pos = 0

        self.walking = False
        self.punch = False
        self.kick = False

    def update(self):
        self.pos += 2
        keypressd = pygame.key.get_pressed()
        if keypressd[pygame.K_RIGHT]:
            self.moveX = 1
            self.walking = True
        elif keypressd[pygame.K_LEFT]:
            self.moveX = -1
        elif keypressd[pygame.K_SPACE]:
            self.punch = True
        else:
            self.moveX = 0
            self.walking = False
            self.punch = False

        self.rect.x += self.moveX
        frame = (self.pos // 30) % len(self.standingFrames)

        # print(self.pos)
        # print(self.pos//30)
        # print(self.pos//30 % len(self.standingFrames))

        self.image = self.standingFrames[frame]

        # time.sleep(10)

        if self.walking:
            frame = (self.pos // 30) % len(self.walkingFrames)
            self.image = self.walkingFrames[frame]

        elif self.punch:
            frame = (self.pos // 30) % len(self.punchFrames)
            self.image = self.punchFrames[frame]

ken = pygame.image.load("images/ken_.png")
background = pygame.image.load("images/background_1.jpg")

all_groups = pygame.sprite.Group()

player_1 = Player_1()
sprite_1 = pygame.sprite.Group()

sprite_1.add(player_1)
all_groups.add(player_1)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # screen.fill(color_1)
    screen.blit(background, (0,0))

    all_groups.update()
    all_groups.draw(screen)

    pygame.display.update()