"""Carve your own jack-o-lantern, by Em and Riley."""

import pygame
  
pygame.init()   

# setting the screen, the title, and the pumpkin
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
bg_image = pygame.image.load("halloween.jpeg")
bg_image = pygame.transform.scale(bg_image,(SCREEN_WIDTH, SCREEN_HEIGHT))
text_font = pygame.font.Font(None, 50)
instructions_font = pygame.font.Font(None, 25)
title = text_font.render(("Decorate Your Own Pumpkin!"), True, "#000000" )
instructions = instructions_font.render(("Click on the object to decorate your pumpkin"), True, "#000000")
pumpkin = pygame.image.load("pumpkin.png")
pumpkin = pygame.transform.scale(pumpkin, (300, 300))


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # creates the screen
# loading button images
witch = pygame.image.load("witch_hat.png").convert_alpha()
witch_on_pumpkin = pygame.transform.scale(witch, (150,150))
party = pygame.image.load("party.png").convert_alpha()
party_on_pumpkin = pygame.transform.scale(party, (150,150))
devil = pygame.image.load("devil.png").convert_alpha()
devil_on_pumpkin = pygame.transform.scale(devil, (250,250))
triangle = pygame.image.load("triangle.png").convert_alpha()
triangle_on_pumpkin = pygame.transform.scale(triangle, (150,100))
cute = pygame.image.load("cute.png").convert_alpha()
cute_on_pumpkin = pygame.transform.scale(cute, (150, 90))
evil = pygame.image.load("evil.png").convert_alpha()
evil_on_pumpkin = pygame.transform.scale(evil, (150, 100))
surpise = pygame.image.load("surpise.png").convert_alpha()
surpise_on_pumpkin = pygame.transform.scale(surpise, (125, 75))
goofy = pygame.image.load("goofy.png").convert_alpha()
goofy_on_pumpkin = pygame.transform.scale(goofy, (125, 75))
fangs = pygame.image.load("fangs.png").convert_alpha()
fangs_on_pumpkin = pygame.transform.scale(fangs, (125, 75))



# button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
        
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action

# creating button instances

# hat buttons
witch_button = Button(100, 350, witch, 0.2 )
witch_visible = False
party_button = Button(300, 390, party, 0.4)
party_visible = False
devil_button = Button(500, 350, devil, 0.2)
devil_visible = False

# eye buttons
triangle_button = Button(40, 140, triangle, 0.35)
triangle_visible = False
cute_button = Button(40, 217, cute, 0.15)
cute_visible = False
evil_button = Button(40, 260, evil, 0.15)
evil_visible = False

# mouth buttons
surpise_button = Button(600, 150, surpise, 0.17)
surpise_visible = False
goofy_button = Button(600, 225, goofy, 0.13)
goofy_visible = False
fangs_button = Button(600, 300, fangs, 0.13)
fangs_visible = False

run = True 
while run: 
    screen.blit(bg_image,(0,0))
    screen.blit(title, (150,40))
    screen.blit(instructions, (220, 75))
    screen.blit(pumpkin, (250, 100))
    # running the hats
    if witch_button.draw():
        devil_visible = False
        party_visible = False
        witch_visible = True
    if witch_visible == True:
        screen.blit(witch_on_pumpkin, (325, 75))
    if party_button.draw():
        devil_visible = False
        witch_visible = False
        party_visible = True
    if party_visible == True:
        screen.blit(party_on_pumpkin, (250, 75))
    if devil_button.draw():
        witch_visible = False
        party_visible = False
        devil_visible = True
    if devil_visible == True:
        screen.blit(devil_on_pumpkin, (270, 45))
    
    # running the eyes
    if triangle_button.draw():
        evil_visible = False
        cute_visible = False
        triangle_visible = True
    if triangle_visible == True:
        screen.blit(triangle_on_pumpkin, (315, 200))
    if cute_button.draw():
        evil_visible = False
        triangle_visible = False
        cute_visible = True
    if cute_visible == True:
        screen.blit(cute_on_pumpkin, (315, 225))
    if evil_button.draw():
        cute_visible = False
        triangle_visible = False
        evil_visible = True
    if evil_visible == True:
        screen.blit(evil_on_pumpkin, (315, 220))

    # running the mouth
    if surpise_button.draw():
        goofy_visible = False
        fangs_visible = False
        surpise_visible = True
    if surpise_visible == True:
        screen.blit(surpise_on_pumpkin, (330, 280))
    if goofy_button.draw():
        fangs_visible = False
        surpise_visible = False
        goofy_visible = True
    if goofy_visible == True:
        screen.blit(goofy_on_pumpkin, (330, 280))
    if fangs_button.draw():
        surpise_visible = False
        goofy_visible = False
        fangs_visible = True
    if fangs_visible == True:
        screen.blit(fangs_on_pumpkin, (335, 280))
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
    
pygame.quit()