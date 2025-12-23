import pygame
import sys
from pygame.locals import *

import random

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
window=pygame.display.set_mode(desktop1_sizes,pygame.RESIZABLE)

window_sizes=pygame.display.get_window_size()
window_width,window_height=window_sizes[0],window_sizes[1]

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
#bird surfaces to be blitted and their sizes
terence_image=bird_sheet.subsurface(bird_extract_sizes["terence"])
terence_image_w,terence_image_h=terence_image.get_size()

matilda_image=bird_sheet.subsurface(bird_extract_sizes["matilda"])
matilda_image_w,matilda_image_h=matilda_image.get_size()

bomb_image=bird_sheet.subsurface(bird_extract_sizes["bomb"])
bomb_image_w,bomb_image_h=bomb_image.get_size()

chuck_image=bird_sheet.subsurface(bird_extract_sizes["chuck"])
chuck_image_w,chuck_image_h=chuck_image.get_size()

red_image=bird_sheet.subsurface(bird_extract_sizes["red"])
red_image_w,red_image_h=red_image.get_size()

stella_image=bird_sheet.subsurface(bird_extract_sizes["stella"])
stella_image_w,stella_image_h=stella_image.get_size()

blues_image=bird_sheet.subsurface(bird_extract_sizes["the blues"])
blues_image_w,blues_image_h=blues_image.get_size()

bubbles_image=bird_sheet.subsurface(bird_extract_sizes["bubbles"])
bubbles_image_w,bubbles_image_h=bubbles_image.get_size()

#cards
card_size=(200,250) #4:5 ratio
card_width,card_height=card_size[0],card_size[1]
#card sizes
#outer frame -> (0,0,200,250)
outer_rect=pygame.Rect(0,0,card_width,card_height)
#inner filling -> (10,10,200-20=180,250-20=230
inner_rect=pygame.Rect(10,10,card_width-20,card_height-20)

#hidden
hidden_card=pygame.Surface(card_size,pygame.SRCALPHA)
pygame.draw.rect(hidden_card,green,inner_rect)
pygame.draw.rect(hidden_card,blue,outer_rect,10,5)
#terence
terence_card=pygame.Surface(card_size,pygame.SRCALPHA)
pygame.draw.rect(terence_card,green,inner_rect)
pygame.draw.rect(terence_card,blue,outer_rect,10,5)
terence_card.blit(terence_image,[card_width/2-terence_image_w//2,card_height/2-terence_image_h//2])

#matilda
matilda_card=pygame.Surface(card_size,pygame.SRCALPHA)
pygame.draw.rect(matilda_card,green,inner_rect)
pygame.draw.rect(matilda_card,blue,outer_rect,10,5)
matilda_card.blit(matilda_image,[card_width/2-matilda_image_w//2,card_height/2-matilda_image_h//2])

#card shuffle
max_cards=False
possible_cards={0:2,1:2,2:2,3:2,4:2,5:2,6:2,7:2}
card_numbers=[]
for i in range(16):
    while True:
        card_number=random.randint(0,7)
        if possible_cards[card_number]>0:
            possible_cards[card_number]-=1
            break
    card_numbers.append(card_number)

cards_clicked=[0]*16

while True:
    mouse_position=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                h=1

    #background colour
    window.fill(light_grey)
    #window center
    pygame.draw.circle(window,red,[desktop1_center_x,desktop1_center_y],5)

    window.blit(matilda_card,[desktop1_center_x-225,desktop1_center_y-125])
    window.blit(terence_card,[desktop1_center_x+25,desktop1_center_y-125])

    pygame.display.flip()