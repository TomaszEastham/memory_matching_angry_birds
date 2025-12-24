import pygame
import sys
from pygame.locals import *

import random

pygame.init()

#desktop sizes
desktops_sizes=pygame.display.get_desktop_sizes()
desktop1_sizes=list(desktops_sizes[0])
desktop1_sizes[0]*=0.75
desktop1_sizes[1]*=0.75
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

def window_size():
    sizes=pygame.display.get_window_size()
    w,h=sizes[0],sizes[1]
    c_x,c_y=w//2,h//2
    return w,h,c_x,c_y
window_width, window_height, window_center_x, window_center_y=window_size()

#bird cards
#image sheet with bird sprites (images)
bird_sheet=pygame.image.load("angry_birds_characters.xcf").convert_alpha()
#the rectangles for each bird from the sheet
bird_extract_sizes={"terence":[4,7,165,180],
                    "matilda":[172,59,92,127],
                    "bomb":[273,65,77,123],
                    "chuck":[461,93,76,92],
                    "red":[539,103,63,82],
                    "stella":[602,106,76,77],
                    "the blues":[685,120,47,88],
                    "bubbles":[738,106,67,78]}

bird_scale=0.8

#bird surfaces to be blitted and their sizes
terence_image=bird_sheet.subsurface(bird_extract_sizes["terence"])
terence_image=pygame.transform.smoothscale_by(terence_image,bird_scale-0.15)
terence_image_w,terence_image_h=terence_image.get_size()

matilda_image=bird_sheet.subsurface(bird_extract_sizes["matilda"])
matilda_image=pygame.transform.smoothscale_by(matilda_image,bird_scale)
matilda_image_w,matilda_image_h=matilda_image.get_size()

bomb_image=bird_sheet.subsurface(bird_extract_sizes["bomb"])
bomb_image=pygame.transform.smoothscale_by(bomb_image,bird_scale)
bomb_image_w,bomb_image_h=bomb_image.get_size()

chuck_image=bird_sheet.subsurface(bird_extract_sizes["chuck"])
chuck_image=pygame.transform.smoothscale_by(chuck_image,bird_scale)
chuck_image_w,chuck_image_h=chuck_image.get_size()

red_image=bird_sheet.subsurface(bird_extract_sizes["red"])
red_image=pygame.transform.smoothscale_by(red_image,bird_scale)
red_image_w,red_image_h=red_image.get_size()

stella_image=bird_sheet.subsurface(bird_extract_sizes["stella"])
stella_image=pygame.transform.smoothscale_by(stella_image,bird_scale)
stella_image_w,stella_image_h=stella_image.get_size()

blues_image=bird_sheet.subsurface(bird_extract_sizes["the blues"])
blues_image=pygame.transform.smoothscale_by(blues_image,bird_scale)
blues_image_w,blues_image_h=blues_image.get_size()

bubbles_image=bird_sheet.subsurface(bird_extract_sizes["bubbles"])
bubbles_image=pygame.transform.smoothscale_by(bubbles_image,bird_scale)
bubbles_image_w,bubbles_image_h=bubbles_image.get_size()

#cards
card_scale=0.8
card_size=(200*card_scale,250*card_scale) #4:5 ratio
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

#bomb
bomb_card=pygame.Surface(card_size,pygame.SRCALPHA)
pygame.draw.rect(bomb_card,green,inner_rect)
pygame.draw.rect(bomb_card,blue,outer_rect,10,5)
bomb_card.blit(bomb_image,[card_width/2-bomb_image_w//2,card_height/2-bomb_image_h//2])

#chuck
chuck_card=pygame.Surface(card_size,pygame.SRCALPHA)
pygame.draw.rect(chuck_card,green,inner_rect)
pygame.draw.rect(chuck_card,blue,outer_rect,10,5)
chuck_card.blit(chuck_image,[card_width/2-chuck_image_w//2,card_height/2-chuck_image_h//2])
#red
red_card=pygame.Surface(card_size,pygame.SRCALPHA)
pygame.draw.rect(red_card,green,inner_rect)
pygame.draw.rect(red_card,blue,outer_rect,10,5)
red_card.blit(red_image,[card_width/2-red_image_w//2,card_height/2-red_image_h//2])

#stella
stella_card=pygame.Surface(card_size,pygame.SRCALPHA)
pygame.draw.rect(stella_card,green,inner_rect)
pygame.draw.rect(stella_card,blue,outer_rect,10,5)
stella_card.blit(stella_image,[card_width/2-stella_image_w//2,card_height/2-stella_image_h//2])

#the blues
blues_card=pygame.Surface(card_size,pygame.SRCALPHA)
pygame.draw.rect(blues_card,green, inner_rect)
pygame.draw.rect(blues_card,blue,outer_rect,10,5)
blues_card.blit(blues_image,[card_width/2-blues_image_w//2,card_height/2-blues_image_h//2])
#bubbles
bubbles_card=pygame.Surface(card_size,pygame.SRCALPHA)
pygame.draw.rect(bubbles_card,green,inner_rect)
pygame.draw.rect(bubbles_card,blue,outer_rect,10,5)
bubbles_card.blit(bubbles_image,[card_width/2-bubbles_image_w//2,card_height/2-bubbles_image_h//2])


#card shuffle
max_cards=False
possible_cards={1:2,2:2,3:2,4:2,5:2,6:2,7:2,8:2}
card_numbers=[]
for i in range(16):
    while True:
        card_number=random.randint(1,8)
        if possible_cards[card_number]>0:
            possible_cards[card_number]-=1
            break
    card_numbers.append(card_number)
print(card_numbers)

cards_clicked=[False]*16
card_limit=2
card_1=0
card_2=0
temp_r=0
player=1

#debug
if_debug=True

while True:
    mouse_position=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        if event.type==WINDOWRESIZED:
            window_width, window_height, window_center_x, window_center_y=window_size()
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type==MOUSEBUTTONDOWN:
            if event.button==1:
                for r in range(len(card_rects)):
                    if card_rects[r].collidepoint(mouse_position):
                        if card_limit>0:
                            cards_clicked[r]=True
                            if card_limit==2:
                                card_1=card_numbers[r]
                                temp_r=r
                            elif card_limit==1:
                                card_2=card_numbers[r]
                            card_limit-=1
                        else:
                            if card_1==card_2:
                                print(f"player {player} got a point")
                            else:
                                cards_clicked[temp_r],cards_clicked[r]=False,False
                            card_limit=2
                            card_1,card_2=0,0
                            if player==1:
                                player=2
                            else:
                                player=1

    #background colour
    window.fill(light_grey)
    #optional window center dot and lines
    if if_debug:
        pygame.draw.circle(window,red,[window_center_x,window_center_y],5)
        pygame.draw.line(window,red,[window_center_x,0],[window_center_x,window_height],3)
        pygame.draw.line(window, red, [0, window_center_y], [window_width, window_center_y], 3)

    #draw cards
    # card placement
    card_gap=25
    card_rects =[pygame.Rect(window_center_x-card_width*2-card_gap*1.5,window_center_y-card_height*2-card_gap*1.5,card_width,card_height),   #row 1
                pygame.Rect(window_center_x-card_width-card_gap/2,window_center_y-card_height*2-card_gap*1.5,card_width,card_height),
                pygame.Rect(window_center_x+card_gap/2,window_center_y-card_height*2-card_gap*1.5,card_width,card_height),
                pygame.Rect(window_center_x+card_width+card_gap*1.5,window_center_y-card_height*2-card_gap*1.5,card_width,card_height),
                pygame.Rect(window_center_x-card_width*2-card_gap*1.5,window_center_y-card_height-card_gap/2,card_width,card_height),       #row 2
                pygame.Rect(window_center_x-card_width-card_gap/2,window_center_y-card_height-card_gap/2,card_width,card_height),
                pygame.Rect(window_center_x+card_gap/2,window_center_y-card_height-card_gap/2,card_width,card_height),
                pygame.Rect(window_center_x+card_width+card_gap*1.5,window_center_y-card_height-card_gap/2,card_width,card_height),
                pygame.Rect(window_center_x-card_width*2-card_gap*1.5,window_center_y+card_gap/2,card_width,card_height),                   #row 3
                pygame.Rect(window_center_x-card_width-card_gap/2,window_center_y+card_gap/2,card_width,card_height),
                pygame.Rect(window_center_x+card_gap/2,window_center_y+card_gap/2,card_width,card_height),
                pygame.Rect(window_center_x+card_width+card_gap*1.5,window_center_y+card_gap/2,card_width,card_height),
                pygame.Rect(window_center_x-card_width*2-card_gap*1.5,window_center_y+card_height+card_gap*1.5,card_width,card_height),     #row 4
                pygame.Rect(window_center_x-card_width-card_gap/2,window_center_y+card_height+card_gap*1.5,card_width,card_height),
                pygame.Rect(window_center_x+card_gap/2,window_center_y+card_height+card_gap*1.5,card_width,card_height),
                pygame.Rect(window_center_x+card_width+card_gap*1.5,window_center_y+card_height+card_gap*1.5,card_width,card_height)]

    #draw the card
    for card in range(len(card_rects)):
        if cards_clicked[card]:
            if card_numbers[card]==1:
                window.blit(terence_card,card_rects[card])
            elif card_numbers[card]==2:
                window.blit(matilda_card,card_rects[card])
            elif card_numbers[card]==3:
                window.blit(bomb_card,card_rects[card])
            elif card_numbers[card]==4:
                window.blit(chuck_card,card_rects[card])
            elif card_numbers[card]==5:
                window.blit(red_card,card_rects[card])
            elif card_numbers[card]==6:
                window.blit(stella_card,card_rects[card])
            elif card_numbers[card]==7:
                window.blit(blues_card,card_rects[card])
            elif card_numbers[card]==8:
                window.blit(bubbles_card,card_rects[card])
        else:
            window.blit(hidden_card,card_rects[card])


    # window.blit(bubbles_card,[window_center_x-card_width-25,window_center_y-card_height//2])
    # window.blit(terence_card,[window_center_x+25,window_center_y-card_height//2])

    pygame.display.flip()