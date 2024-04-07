'''
Friend Game
Lucy Acheson
3/1/24
'''

import pygame
import sys

pygame.init()


# Set up the screen
screen = pygame.display.set_mode((640, 480))
background = pygame.surface.Surface((640, 480))
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (640, 480))
background_x = 0
background_y = 0


# Player sprite
player = pygame.sprite.Sprite()
player.image = pygame.image.load("player.jpg")
player.rect = player.image.get_rect()
player.rect.x = 100 # x and y coords
player.rect.y = 100
player.image = pygame.transform.scale(player.image, (10, 40)) # size
player.speed_x = 0
player.speed_y = 0


#game loop
while True:

    # Handle events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the background and the player.
    screen.blit(background, (0, 0))
    screen.blit(player.image, player.rect)

    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("player.jpg")
            self.rect = self.image.get_rect()
            self.rect.x = 100
            self.rect.y = 100
            self.image = pygame.transform.scale(self.image, (10, 40))
            self.speed_x = 0
            self.speed_y = 0

        def update(self):
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
        
        def move(self, x, y):
            self.rect.x = x
            self.rect.y = y


    # scrolling
    # Update the background's position.
    # background_x == -(player.speed_x / 2)
    # background_y == -(player.speed_y / 2)

    # If the background has moved off the screen, reset its position.
    if background_x < -background.get_width():
        background_x = 0

    # moving the player 
    if event.type == pygame.KEYDOWN:
        print("key pressed")
        if event.key == pygame.K_LEFT:
            player.speed_x = -1
            
        if event.key == pygame.K_RIGHT or event.key == ord('d'):
            player.speed_x = 5
        if event.key == pygame.K_UP or event.key == ord('w'):
            player.speed_y = -5
        if event.key == pygame.K_DOWN or event.key == ord('s'):
            player.speed_y = 5

    # Update the player's position.
    player.rect.x += player.speed_x
    player.rect.y += player.speed_y
    player.update()

    # Update the display.
    pygame.display.update()