import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Friend Game')

# Load background image
location = "cantina"
background_image = pygame.image.load('backgrounds/cantina2.png')
background_image = pygame.transform.scale(background_image, (window_width, window_height))
background_rect = background_image.get_rect()

# Load map
map_image = pygame.image.load('map_elements/map.png')
open_map = False
pin_image = pygame.image.load('map_elements/pin.png')

# Load coin
coin_image = pygame.image.load('buttons/coin.png')
coin_image = pygame.transform.scale(coin_image, (100, 100))
coin_font = pygame.font.Font(None, 32)

# Load backpack/inventory
backpack_image = pygame.image.load('buttons/inventory.png')
backpack_image = pygame.transform.scale(backpack_image, (100, 100))

# Load heart
heart_image = pygame.image.load('buttons/heart.png')
heart_image = pygame.transform.scale(heart_image, (100, 100))

# Load globe image
globe_image = pygame.image.load('buttons/globe.png')
globe_width, globe_height = globe_image.get_size()
scale_factor = 0.1  # Adjust this factor to scale the image
new_globe_width = int(globe_width * scale_factor)
new_globe_height = int(globe_height * scale_factor)
globe_image = pygame.transform.scale(globe_image, (new_globe_width, new_globe_height))

# Load tom's buy buttons
buy_button = pygame.image.load('buttons/buy.png')
buy_button = pygame.transform.scale(buy_button, (100, 100))

# Load and scale player image
player_image = pygame.image.load("Characters/lucy.png")
player_image = pygame.transform.scale(player_image, (100, 100))  # size

# Load and scale Maya image
maya_image = pygame.image.load("Characters/maya.png")
maya_image = pygame.transform.scale(maya_image, (100, 100))  # size

# Load and scale Lena image
lena_image = pygame.image.load("Characters/lena.png")
lena_image = pygame.transform.scale(lena_image, (100, 100))  # size

# font
showText = False
showDialogue = False
pygame.font.init()
font = pygame.font.Font(None, 24)
dialogue_font = pygame.font.Font(None, 18)
toms_font = pygame.font.Font(None, 36)
font_color = (0, 0, 0)
font_background = (255, 255, 255)
title_surface = font.render("", True, font_color, font_background)
description_surface = font.render("", True, font_color, font_background)
dialogue_surface = dialogue_font.render("", True, font_color, font_background)

def clear_text():
    global title_surface, description_surface, showText
    title_surface = font.render("", True, font_color, font_background)
    description_surface = font.render("", True, font_color, font_background)
    showText = False

# Positioning the text on the screen
title_pos = (10, 10)  # Title in top left
description_pos = (10, 40)  # Below the title
dialogue_pos = (10, 550) # Bottom center


class Character:
    def __init__(self, name, location, likes, quests, image, x, y):
        self.name = name
        self.location = location
        self.likes = likes
        self.quests = quests
        self.image = pygame.image.load(image)  # Load the image
        self.image = pygame.transform.scale(self.image, (100, 100))  # size
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100


    def isClicked(self, mouse_x, mouse_y):
        if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
            return True
        return False
    

class Quest():
    def __init__(self, assigned, title, description, fulfill, completed):
        self.assigned = assigned
        self.title = title
        self.description = description
        self.fulfill = fulfill
        self.completed = completed


class Player():
    quests = []
    active_fulfills = []

    def __init__(self):
        self.inventory = []
        self.quests = []
        

        original_image = pygame.image.load("Characters/lucy.png")
        original_width, original_height = original_image.get_size()
        width_scale_factor = 10  # Adjust this factor to scale the width
        height_scale_factor = 9  # Adjust this factor to scale the height
        new_width = int(original_width * width_scale_factor)
        new_height = int(original_height * height_scale_factor)
        self.image = pygame.transform.scale(original_image, (new_width, new_height))


    def fetchQuests(self):
        return self.quests
    
    def fetchInventory(self):
        return self.inventory

# Create the player and characters
# Char: name, location, likes, quests, image, x, y
# Quest: assigned, title, description, fulfill, completed
player_instance = Player()

maya = Character("Maya", "Cantina", "nails", Quest("maya", "Give Lena a kiss", "Give Leonard a kiss from me!", "lena", False), "Characters/maya.png", 225, 400)
lena = Character("Lena", "Cantina", "4loko", Quest("lena", "Get Lena coffee from Amelia", "Can you please find Amelia to get me my coffee?", "amelia", False), "Characters\lena.png", 600, 470)
## amelia = Character("Amelia", "Cantina", "Diet Coke", "Walk Murphy", "amelia.png", x, y)
## mateo = Character("Mateo", "...", "...", "Buy produce", "mateo.png", x, y)
## skye = Character("Skye", "...", "Taco Bell", "Buy alcohol", "skye.png", x, y)
## mozi = Character("Mozi", "...", "Cigarettes", "Go to trampoline", "mozi.png", x, y)
emmy = Character("Emmy", "river", "Cigarettes", "Retrieve shirt from 111", "Characters/emmy.png", 550, 275)
## william = Character("William", "...", "...", "Retrieve shrooms from Maya", "william.png", x, y)
## zoe = Character("Zoe", "...", "Dutch Bros", "...", "Characters/zoe.png", x, y)
## murphy = Character("Murphy", "Cantina", "Cheese", None, "Characters/murphy.png", x, y)
## presley = Character("Presley", "...", "...", "...", "Characters/presley.png", x, y)
## iris = Character("Iris", "...", "...", "...", "Characters/iris.png", x, y)
## lucy = Character("Lucy", "EMU", "...", "...", "Characters/lucy.png", x, y)


money = 0
love = 0
questOfferActive = False

shop = {"coffee": 5,
                "nails": 5,
                "4loko": 15,
                "cheese": 10,
                "cigarettes": 30,
                "taco bell": 15,
                "diet coke": 5,
                "dutch bros": 10}

def open_quests():
    # Use the player_instance to fetch quests
    # print(player_instance.fetchQuests())
    pass

def open_inventory():
    print("Inventory: " + str([str(item) for item in player_instance.inventory]))


# Set initial player position
player_x = 340
player_y = 490

# Assuming player_image is a pygame.Surface object
player_width, player_height = player_image.get_size()

# Initialize key states
key_w = key_s = key_a = key_d = False

def calculate_distance(player_x, player_y, character_x, character_y):
    return ((player_x - character_x) ** 2 + (player_y - character_y) ** 2) ** 0.5

def location_changed():
    global questOfferActive, showDialogue, showText, player_x, player_y, location
    questOfferActive = False
    showDialogue = False
    clear_text()
    if location == "cantina":
        player_x = 340
        player_y = 490
    if location == "river":
        player_x = 74
        player_y = 496



while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Handle key presses inside the event loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:     # Q button opens quests menu
                if showText:
                    showText = False
                    questOfferActive = False
                else:
                    showText = True
                if showDialogue:
                    showDialogue = False

            if event.key == pygame.K_e:    # E button opens inventory menu
                open_inventory()
            if event.key == pygame.K_ESCAPE: # ESC button quits the game
                pygame.quit()
           
            if event.key == pygame.K_x:
                if questOfferActive:
                    questOfferActive = False
                    showText = False
                    clear_text()
            if event.key == pygame.K_y:
                if questOfferActive:
                    questOfferActive = False

                    Player.quests.append(offeredQuest)
                    Player.active_fulfills.append(offeredQuest.fulfill)

                    #text        
                    title_surface = font.render(f"Title: {Player.quests[0].title}", True, font_color, font_background)
                    description_surface = font.render(f"Description: {Player.quests[0].description}", True, font_color, font_background)
                    showText = True


            # Update key states for movement
            if event.key == pygame.K_w:
                key_w = True
            if event.key == pygame.K_s:
                key_s = True
            if event.key == pygame.K_a:
                key_a = True
            if event.key == pygame.K_d:
                key_d = True

        # Handle key releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                key_w = False
            if event.key == pygame.K_s:
                key_s = False
            if event.key == pygame.K_a:
                key_a = False
            if event.key == pygame.K_d:
                key_d = False

        # Update player position based on key states
        if key_w and player_y > 65:
            player_y -= 10
        if key_s and player_y < window_height - player_height:
            player_y += 10
        if key_a and player_x > -15:
            player_x -= 10
        if key_d and player_x < (window_width - player_width) + 15:
            player_x += 10


        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                mouse_x, mouse_y = pygame.mouse.get_pos()


                # Calculate distance from player to Lena
                distance_to_lena = calculate_distance(player_x, player_y, lena.x, lena.y)
                # Calculate distance from player to Maya
                distance_to_maya = calculate_distance(player_x, player_y, maya.x, maya.y)
                # Calculate distance from player to Amelia
                ## distance_to_amelia = calculate_distance(player_x, player_y, amelia.x, amelia.y)


                # Check if globe is clicked
                if 730 <= mouse_x <= 730 + new_globe_width and 5 <= mouse_y <= 5 + new_globe_height:
                    if open_map:
                        open_map = False
                    else:
                        open_map = True
                
                # Check if backpack/inventory is clicked
                if 580 <= mouse_x <= 680 and -15 <= mouse_y <= 85:
                    open_inventory()

                # Clicking a pin
                if open_map:
                    if 230 <= mouse_x <= 255 and 390 <= mouse_y <= 420:  # Cantina
                        location = "cantina"
                        location_changed()
                        background_image = pygame.image.load('backgrounds/cantina2.png')
                        background_image = pygame.transform.scale(background_image, (window_width, window_height))
                        background_rect = background_image.get_rect()
                        open_map = False
                    if 510 <= mouse_x <= 540 and 425 <= mouse_y <= 460:  # Tom's
                        location = "toms"
                        location_changed()
                        background_image = pygame.image.load('backgrounds/toms.png')
                        background_image = pygame.transform.scale(background_image, (window_width, window_height))
                        background_rect = background_image.get_rect()
                        open_map = False
                    if 530 <= mouse_x <= 560 and 170 <= mouse_y <= 210: # river
                        location = "river"
                        location_changed()
                        background_image = pygame.image.load('backgrounds/river.png')
                        background_image = pygame.transform.scale(background_image, (window_width, window_height))
                        background_rect = background_image.get_rect()
                        open_map = False

                # Shopping in Tom's
                if location == "toms" and (0 <= mouse_x <= 75):
                    if 85 <= mouse_y <= 115:
                        if money >= shop["coffee"]:
                            money -= shop["coffee"]
                            player_instance.inventory.append("coffee")
                            description_surface = font.render("You purchased coffee", True, font_color, font_background)
                            showText = True
                        else:
                            description_surface = font.render("You don't have enough money", True, font_color, font_background)
                            showText = True
                    if 145 <= mouse_y <= 175:
                        if money >= shop["nails"]:
                            money -= shop["nails"]
                            player_instance.inventory.append("nails")
                            description_surface = font.render("You purchased nails", True, font_color, font_background)
                            showText = True
                        else:
                            description_surface = font.render("You don't have enough money", True, font_color, font_background)
                            showText = True
                    if 205 <= mouse_y <= 235:
                        if money >= shop["4loko"]:
                            money -= shop["4loko"]
                            player_instance.inventory.append("4loko")
                            description_surface = font.render("You purchased 4loko", True, font_color, font_background)
                            showText = True
                        else:
                            description_surface = font.render("You don't have enough money", True, font_color, font_background)
                            showText = True
                    if 265 <= mouse_y <= 295:
                        if money >= shop["cheese"]:
                            money -= shop["cheese"]
                            player_instance.inventory.append("cheese")
                            description_surface = font.render("You purchased cheese", True, font_color, font_background)
                            showText = True
                        else:
                            description_surface = font.render("You don't have enough money", True, font_color, font_background)
                            showText = True
                    if 325 <= mouse_y <= 355:
                        if money >= shop["cigarettes"]:
                            money -= shop["cigarettes"]
                            player_instance.inventory.append("cigarettes")
                            description_surface = font.render("You purchased cigarettes", True, font_color, font_background)
                            showText = True
                        else:
                            description_surface = font.render("You don't have enough money", True, font_color, font_background)
                            showText = True
                    if 385 <= mouse_y <= 415:
                        if money >= shop["taco bell"]:
                            money -= shop["taco bell"]
                            player_instance.inventory.append("taco bell")
                            description_surface = font.render("You purchased Taco Bell", True, font_color, font_background)
                            showText = True
                        else:
                            description_surface = font.render("You don't have enough money", True, font_color, font_background)
                            showText = True
                    if 445 <= mouse_y <= 475:
                        if money >= shop["diet coke"]:
                            money -= shop["diet coke"]
                            player_instance.inventory.append("diet coke")
                            description_surface = font.render("You purchased Diet Coke", True, font_color, font_background)
                            showText = True
                        else:
                            description_surface = font.render("You don't have enough money", True, font_color, font_background)
                            showText = True
                    if 505 <= mouse_y <= 535:
                        if money >= shop["dutch bros"]:
                            money -= shop["dutch bros"]
                            player_instance.inventory.append("dutch bros")
                            description_surface = font.render("You purchased Dutch Bros", True, font_color, font_background)
                            showText = True
                        else:
                            description_surface = font.render("You don't have enough money", True, font_color, font_background)
                            showText = True

                # Check if Maya is clicked and within 150 pixels
                if maya.isClicked(mouse_x, mouse_y) and distance_to_maya <= 150:
                    if "maya" in player_instance.active_fulfills: # if maya is involved in a quest
                        # Fill in when there is a maya quest
                        pass
                    elif questOfferActive == False and maya.quests.completed == False: # if there is no quest currently being OFFERED and maya's quest has noT been completed yet
                        showDialogue = False
                        questOfferActive = True
                        showText = True
                        title_surface = font.render("Maya wants to give you a quest! Press Y to accept! Press X to reject", True, font_color, font_background)
                        description_surface = font.render("Title: " + maya.quests.title, True, font_color, font_background)
                        offeredQuest = maya.quests
                    elif maya.likes in player_instance.inventory: # give gift
                        clear_text()
                        dialogue_surface = font.render("Maya: Thank you for the nails! Here is some love", True, font_color, font_background)
                        love += 10
                        showDialogue = True
                        player_instance.inventory.remove("nails")
                    elif maya.quests.completed: # if maya's quest has been completed
                        clear_text()
                        dialogue_surface = font.render("Maya: I don't have any quests for you right now", True, font_color, font_background)
                        showDialogue = True


                # Check if Lena is clicked and within 150 pixels
                if lena.isClicked(mouse_x, mouse_y) and distance_to_lena <= 150:
                    if "lena" in player_instance.active_fulfills:
                        clear_text()
                        Player.active_fulfills.remove("lena")
                        Player.quests.remove(Player.quests[0])
                        maya.quests.completed = True
                        dialogue_surface = font.render("Lena: Thank you for the kiss! Here is some money", True, font_color, font_background)
                        money += 10
                        love += 10
                        showDialogue = True
                    elif questOfferActive == False and lena.quests.completed == False:
                        showDialogue = False
                        questOfferActive = True
                        showText = True
                        title_surface = font.render("Lena wants to give you a quest! Press Y to accept! Press X to reject", True, font_color, font_background)
                        description_surface = font.render("Title: " + lena.quests.title, True, font_color, font_background)
                        offeredQuest = lena.quests
                    elif lena.quests.completed:
                        clear_text()
                        dialogue_surface = font.render("Lena: I don't have any quests for you right now", True, font_color, font_background)
                        showDialogue = True
   


    # Draw the background
    window.blit(background_image, background_rect)

    # tan bar at top
    TAN = (210, 180, 140)
    pygame.draw.rect(window, TAN, (0, 0, 800, 70))  # Adjust the height as needed
    # coin icon
    window.blit(coin_image, (640, -5))
    money_text = coin_font.render(str(money), True, font_color, None)
    window.blit(money_text, (710, 25))
    # backpack icon
    window.blit(backpack_image, (580, -15))
    # heart icon
    window.blit(heart_image, (490, -10))
    love_text = coin_font.render(str(love), True, font_color, None)
    window.blit(love_text, (560, 25))

    # Draw the player
    if not location == "toms":
        window.blit(player_image, (player_x, player_y))
    if location == "cantina":
        window.blit(maya.image, (maya.x, maya.y))
        window.blit(lena.image, (lena.x, lena.y))
    if location == "river":
        window.blit(emmy.image, (emmy.x, emmy.y))

    # Draw the globe icon
    window.blit(globe_image, (730, 0))

    # Draw the text
    if showText and not open_map:
        window.blit(title_surface, title_pos)
        window.blit(description_surface, description_pos)
    if showDialogue and not open_map:
        window.blit(dialogue_surface, dialogue_pos)
    
    # Draw Tom's menu (maybe make as a backdrop)
    if location == "toms":
        y_pos = 90
        for item in shop:
            toms_text = toms_font.render(f"{item}: ${shop[item]}", True, font_color, font_background)
            window.blit(toms_text, (85, y_pos)) # menu item
            window.blit (buy_button, (-10, y_pos-35)) # buy button
            y_pos += 60

    # Draw the map, this should always be at the end so that it draws map on top of everything
    if open_map:
        window.blit(map_image, (175, 150))
        window.blit(pin_image, (210, 375)) # Cantina
        window.blit(pin_image, (490, 410)) # Tom's
        window.blit(pin_image, (510, 150)) # River
        window.blit(pin_image, (230, 210)) # Biggest dome

    pygame.display.update()
