# Librerias necesarias
import pygame
import os
import time
import random

#Resolution
WIDTH, HEIGHT = 750, 750
#setting the window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#name of the window
pygame.display.set_caption("Space Shooter Tutorial")



# Cargamos las imagenes
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
# Player ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))
# Lasers 
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
# Background
BG = pygame.image.load(os.path.join("assets", "Background-black.png"))


def main():
    #variable que
    run = True
    #Velocidad de fotogramas por segundo
    FPS = 60
    clock = pygame.time.Clock()
    
    while run:
        
        #Velocidad del juego 
        clock.tick(FPS)
        
        #detector de eventos en la pantalla
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #acaba el juego al dar click en salir
                run = False
            
main()
            
        