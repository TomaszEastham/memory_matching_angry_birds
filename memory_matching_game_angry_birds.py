import pygame
import sys
from pygame.locals import *

pygame.init()
#desktop sizes
desktops_sizes=pygame.display.get_desktop_sizes()
desktop1_sizes=list(desktops_sizes[0])
desktop1_sizes[0]*=0.5
desktop1_sizes[1]*=0.5
desktop1_width=desktop1_sizes[0]
desktop1_height=desktop1_sizes[1]
desktop1_center_x=desktop1_width//2
desktop1_center_y=desktop1_height//2

#colours
light_grey=(128,128,128) #grey
dark_grey=(105,105,105) #dimgrey
black=(0,0,0) #black
white=(255,255,255) #white
red=(220,20,60) #crimson
green=(50,205,50) #lime green
blue=(30,144,255) #dodger blue
gold=(207,181,59) #old gold

#window creation
window=pygame.display.set_mode(desktop1_sizes,pygame.NOFRAME)

#bird cards
#main image
bird_sheet=pygame.image.load("angry_birds_characters.xcf").convert_alpha()
#the rectangles if each bird from the sheet
bird_extract_sizes={"terence":[4,7,165,180],
                    "matilda":[172,59,92,127],
                    "bomb":[273,65,77,123],
                    "chuck":[461,93,76,92],
                    "red":[539,103,63,82],
                    "stella":[602,106,76,77],
                    "the blues":[685,120,47,88],
                    "bubbles":[738,106,67,78]}
#bird surfaces to be blitted
terence_surface=bird_sheet.subsurface(bird_extract_sizes["terence"])
matilda_surface=bird_sheet.subsurface(bird_extract_sizes["matilda"])


while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
    window.fill(light_grey)
    pygame.display.flip()