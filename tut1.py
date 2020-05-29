import pygame

#Colors
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
grey= (122, 122, 122)

display = pygame.display.set_mode((600, 600))

game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    display.fill(white)
    display.fill(red, rect=[300, 300, 20, 20])
    pygame.display.update()
