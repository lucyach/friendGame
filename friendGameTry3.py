'''
Friend Game 2nd Try
ChatGPT getting me started
Lucy Acheson
'''

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Pygame Background Scrolling')

# Load background image
background_image = pygame.image.load('background.jpg')
background_rect = background_image.get_rect()
background_x = 0  # Initial background position
background_y = 0
background_scale = 1.5  # Background zoom factor
scroll_speed = 2  # Set the speed of background scrolling

# Load player image
player_image = pygame.Surface((50, 50))
player_image = pygame.image.load("player.jpg")
player_image = pygame.transform.scale(player_image, (10, 40)) # size

# Set initial player position
player_x = window_width // 2
player_y = window_height // 2
background_center = (background_x + background_rect.width * background_scale / 2,
                     background_y + background_rect.height * background_scale / 2)

# Define NPC (Friend) class
class Friend:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.Surface((30, 30))
        self.image.fill((0, 255, 0))  # Green square for friend

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

# Specify coordinates for friends on the background
friend_coordinates = [
    (100, 200),
    (400, 300),
    (600, 400),
    (1000, 500),
    # Add more points as needed
]

# Instantiate friends at specified positions on the background
friends = [Friend(x, y) for x, y in friend_coordinates]

# Main game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the state of all keyboard keys
    keys = pygame.key.get_pressed()

    # Scroll background based on key presses
    if keys[pygame.K_w]:
        if background_y < 0:
            background_y += scroll_speed
            background_center = (background_center[0], background_center[1] + scroll_speed)
            for friend in friends:
                friend.y += scroll_speed
    if keys[pygame.K_s]:
        if background_y > window_height - background_rect.height * background_scale:
            background_y -= scroll_speed
            background_center = (background_center[0], background_center[1] - scroll_speed)
            for friend in friends:
                friend.y -= scroll_speed
    if keys[pygame.K_a]:
        if background_x < 0:
            background_x += scroll_speed
            background_center = (background_center[0] + scroll_speed, background_center[1])
            for friend in friends:
                friend.x += scroll_speed
    if keys[pygame.K_d]:
        if background_x > window_width - background_rect.width * background_scale:
            background_x -= scroll_speed
            background_center = (background_center[0] - scroll_speed, background_center[1])
            for friend in friends:
                friend.x -= scroll_speed
    if keys[pygame.K_PLUS] or keys[pygame.K_EQUALS]:
        background_scale += 0.1
    if keys[pygame.K_MINUS]:
        background_scale -= 0.1
        if background_scale < 0:
            background_scale = 0

    # Clear the screen
    window.fill((0, 0, 0))

    # Scale and draw background
    scaled_background = pygame.transform.scale(background_image,
                                               (int(background_rect.width * background_scale),
                                                int(background_rect.height * background_scale)))
    window.blit(scaled_background, (background_x, background_y))

    # Draw player
    window.blit(player_image, (player_x, player_y))

    # Draw friends relative to the background
    for friend in friends:

        # Calculate friend position relative to the background
        friend_pos_x = friend.x - background_x
        friend_pos_y = friend.y - background_y
        # Draw friend only if it's within the visible window
        if 0 <= friend_pos_x < window_width and 0 <= friend_pos_y < window_height:
            friend.draw(window)

    # Update the display
    pygame.display.update()