import pygame
from pygame.locals import *
#Colors
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
grey= (122, 122, 122)

#variables
frame = 600
leadx = 300
leady = 300
xchange = 0
ychange = 0
snake_size = 20
clock = pygame.time.Clock()
#window
display = pygame.display.set_mode((frame, frame))

game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                xchange = -snake_size
                ychange = 0
            if event.key == K_RIGHT:
                xchange = snake_size
                ychange = 0
            if event.key == K_UP:
                ychange -= snake_size
                xchange = 0
            if event.key == K_DOWN:
                ychange = snake_size
                xchange = 0
    leadx += xchange
    leady += ychange
    display.fill(white)
    display.fill(red, rect=[leadx, leady, snake_size, snake_size])
    pygame.display.update()
    clock.tick(40)
