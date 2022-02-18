import pygame
import time

pygame.init()

display_width = 1280 
display_height = 720

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

ninja_width = 400

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ninja Hunter')
clock = pygame.time.Clock()

charImg = pygame.image.load('ninja1.png')

def ninja(x, y):
    gameDisplay.blit(charImg, (x, y))
    
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('C:\WINDOWS\FONTS\BRLNSR.TTF', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    pygame.display.update()
    
    time.sleep(2)
    
    game_loop()
    
def crash():
    message_display('You suck!')


def game_loop():
    x = (display_width * 0.25)
    y = (display_height * .09)
    
    x_change = 0
    
    gameExit = False
    
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                       
        x += x_change
        
        gameDisplay.fill(white)
        ninja(x, y)
        
        if x > display_width - ninja_width or x < -225:
            crash()
        
        pygame.display.update()
        clock.tick(120)

game_loop()
pygame.quit()
quit()