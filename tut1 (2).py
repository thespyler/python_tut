import pygame

pygame.display.set_mode((600, 600))

game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
