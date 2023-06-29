import pygame
from pygame.locals import *

#initilize game
pygame.init()

#set constants
WIDTH = 800
HEIGHT = 600

#set screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
back = pygame.Surface((WIDTH, HEIGHT))
background = back.convert()
background.fill((0, 0, 0))

class Character:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.speed = 75
        self.xMove = 0
        self.yMove = 0
        self.width = 20
        self.height = 20
        self.image = pygame.Surface((self.width, self.height)).convert()
        self.image.fill((0, 0, 255))
        self.image = self.image.convert()

player1 = Character()
level = Character()

level.x, level.y = 200, 200
level.width = 500

#set clock
isRunning = True
clock = pygame.time.Clock()

while isRunning:

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player1.xMove = player1.speed
            elif event.key == K_UP:
                player1.yMove = -player1.speed
            elif event.key == K_DOWN:
                player1.yMove = player1.speed
            elif event.key == K_LEFT:
                player1.xMove = -player1.speed

        #set boundraries 
    if player1.y >= HEIGHT - player1.height - 10:
        player1.y = HEIGHT - player1.height - 10
        player1.xMove = -player1.xMove
    elif player1.y <= 10 :
        player1.y = 10
        player1.xMove = -player1.xMovemove

    #gravity
    player1.yMove += 10

    timePassed = clock.tick(30)
    timeSec = timePassed/1000.0

    player1.y += player1.yMove*timeSec
    player1.x += player1.xMove*timeSec
    screen.blit(background, (0, 0))

    screen.blit(player1.image, (player1.x, player1.y))

    pygame.display.update()

#end game loop and quit
pygame.quit()
