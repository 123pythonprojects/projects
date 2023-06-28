import pygame
from pygame.locals import *
import random

#initilize game
pygame.init()

#set constants
WIDTH = 800
HEIGHT = 600

#set screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Pong")
back = pygame.Surface((WIDTH, HEIGHT))
background = back.convert()
background.fill((0, 0, 0))

#create Player class
class Player():
    x = 0
    y = 0
    speed = 250.0
    move = 0
    score = 0
    height = 75
    width = 10
    image = pygame.Surface((width, height)).convert()
    image.fill((0, 0, 255))

#create players
player1 = Player()
player2 = Player()

#set player variables to values
player1.x, player1.y = 10, HEIGHT/2 - player1.height/2
player2.x, player2.y = WIDTH - 10 - player2.width, HEIGHT/2 - player2.height/2

#set clock
isRunning = True
clock = pygame.time.Clock()

#game loop
while isRunning:
    #event loop
    for event in pygame.event.get():
        #quit game
        if event.type == QUIT:
            isRunning = False
        #keyboard controller
        elif event.type == KEYDOWN:
            if event.key == K_w:
                player1.move = -player1.speed
            if event.key == K_s:
                player1.move = player1.speed
            if event.key == K_UP:
                player2.move = -player2.speed
            if event.key == K_DOWN:
                player2.move = player2.speed
                
    #standardize clock and movement speed
    timePassed = clock.tick(30)
    timeSecond = timePassed/1000.0
    player1.y += player1.move*timeSecond
    player2.y += player2.move*timeSecond

    #set boundraries 
    if player1.y >= HEIGHT - player1.height - 10:
        player1.y = HEIGHT - player1.height - 10
        player1.move = -player1.move
    elif player1.y <= 10 :
        player1.y = 10
        player1.move = -player1.move
    if player2.y >= HEIGHT - player2.height - 10:
        player2.y = HEIGHT - player2.height - 10
        player2.move = -player2.move
    elif player2.y <= 10:
        player2.y = 10
        player2.move = -player2.move

    #add images to gamewindow
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen,(255,255,255),Rect((5,5),(WIDTH - 10, HEIGHT - 10)),2)
    pygame.draw.aaline(screen, (255,255,255),(int(WIDTH/2),5),((int(WIDTH/2),HEIGHT-5)))
    screen.blit(player1.image, (player1.x, player1.y))
    screen.blit(player2.image, (player2.x, player2.y))
    
    pygame.display.update()

#end game loop and quit
pygame.quit()
