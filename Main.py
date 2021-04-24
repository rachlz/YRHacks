# Project Name: GreenCode
# Date: April 24, 2021
# Author: Rachel Zhang  
# Description: This pygame program showcases everyday items that are damaging the environment. Through GreenCode, people, especially students, will learn about different alternatives to protect the environment.  

import pygame, sys, os 
from pygame import *

# Start up pygame
pygame.init()

# Setting up the window where we will draw our shapes and display animations
# The numbers represent the resolution of the screen
WIN = pygame.display.set_mode((900, 700))
pygame.display.set_caption('Harry V.S. Horcruxes')

# Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
LIGHTBROWN = (199,167,93)
BLUE = (0,0,255)
DARKGREEN = (23,85,16)
LIGHTGRAY = (249,249,249)
GRAY = (174,174,174)
LIGHTGREEN = (116,213,123)
ORANGE = (255,212,125)
# Creating font sizes
font = pygame.font.SysFont("Georgia",28)
font_1 = pygame.font.SysFont ("Georgia",30)
font_2 = pygame.font.SysFont ("Georgia", 18)
font_3 = pygame.font.SysFont ("Georgia", 20)
menu_font = pygame.font.SysFont("Georgia",50)
instructions_font = pygame.font.SysFont("Comic Sans MS", 20)
ESC_font = pygame.font.SysFont("Comic Sans MS", 20)
textbox = pygame.font.SysFont("Comic Sans MS",18)
def drawText(text, font, color, surface, x, y):
    graphics = font.render(text,1,color)
    WIN.blit(graphics,(x,y))

click = False
# Menu Page main loop
def menu_page():
    
    # Background Picture for Menu Page
    loc = os.getcwd()
    img = 'main_background.jpg'
    path = loc + "\\" + img
    imgbeach = pygame.image.load(path)
    imgX = 0
    imgY = 0
    # Background music
    loc_music = os.getcwd()
    music = 'main_music.wav'
    path_music = loc_music + "\\" + music
    theme = pygame.mixer.music.load('main_music.wav')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops = -1)
    
    while True:
        WIN.fill(BLACK)
        
        WIN.blit(imgbeach,(imgX,imgY)) 
        
        drawText("GreenCode",menu_font, BLACK, WIN, 350, 200)
        # Get the mouse cursor position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Create Buttons on menu 
        button_instructions = pygame.Rect(305,305,325,40)
        
        button_gray_instructions = pygame.Rect(270,290,400,70)
        
        button_game = pygame.Rect(305,438,325,40)
        button_gray_game = pygame.Rect(270,425,400,70)
        # Create collide point to test if a point is in the button
        if button_instructions.collidepoint(mouse_x,mouse_y):
            if click:
                instructions()
        if button_game.collidepoint(mouse_x,mouse_y):
            if click:
                explore()
        # Create buttons and text
        pygame.draw.rect(WIN,GRAY, button_gray_instructions)
        pygame.draw.rect(WIN,ORANGE,button_instructions)       
        drawText("Instructions", font, (BLACK),WIN,393,305)
        
        pygame.draw.rect(WIN,GRAY, button_gray_game)
        pygame.draw.rect(WIN,ORANGE,button_game)
        drawText("Explore!", font, (BLACK), WIN, 420,440)        

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.type == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

# Instructions Page loop
def instructions():
    run = True
    # Picture

    loc_instr = os.getcwd()
    img_instr = 'instruction_background.jpg'
    path_instr = loc_instr + "\\" + img_instr
    imginstr = pygame.image.load(path_instr)
    instrX = 0
    instrY = 0
 
    while run:
        WIN.fill(LIGHTGRAY)
        WIN.blit(imginstr,(instrX,instrY))
        drawText("Press ESC to exit to menu", ESC_font, (WHITE),WIN,20,30)
        # Instructions
        drawText("Welcome to GreenCode!", font_1, (WHITE),WIN,50,130)
        drawText("GreenCode is an educational game platform that showcase global environmental issues.", font_3, (BLACK),WIN,50,230)
        drawText("By EXPLORING the game,", font_3, (BLACK),WIN,50,260)
        drawText("you will be presented with 2 household products that are harmful to the environment.", font_3, (BLACK),WIN,50,290)    
        drawText("Clicking the products, you will be able to view more information about the products!", font_3, (BLACK),WIN,50,320) 
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        pygame.display.update()

# Game Page loop                     
def explore():
    run = True
    # Background Picture for Explore Page
    loc_explore = os.getcwd()
    img_back = 'main_explore.jpg'
    path_back = loc_explore + "\\" + img_back
    imgexplore = pygame.image.load(path_back)
    exploreX = 0
    exploreY = 0

    # 5 Items
    loc_plastic = os.getcwd()
    img_plastic = 'plastic.png'
    path_plastic = loc_plastic + "\\" + img_plastic
    imgplastic = pygame.image.load(path_plastic)
    plasticX = 100
    plasticY = 450

    loc_wipe = os.getcwd()
    img_wipe = 'wipes.png'
    path_wipe = loc_wipe + "\\" + img_wipe
    imgwipe = pygame.image.load(path_wipe)
    wipeX = 350
    wipeY = 300
    
    while run:
        WIN.fill(LIGHTBROWN)
        pygame.time.delay(10)
        WIN.blit(imgexplore,(exploreX,exploreY))
        WIN.blit(imgplastic, (plasticX, plasticY))
        WIN.blit(imgwipe, (wipeX,wipeY))
        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        pygame.display.update()

        click = False
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
            pygame.display.update()
        # Get the mouse cursor position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Create Buttons on menu 
        button_plastic = pygame.Rect(100,450,180,269)

        button_wipe = pygame.Rect(350,300,500,500)
        
        # Create collide point to test if a point is in the button

        if button_plastic.collidepoint(mouse_x,mouse_y):
            if click:
                click = True 
                plastic()
        elif button_wipe.collidepoint(mouse_x,mouse_y):
            if click: 
                wipe()
        pygame.display.update()

def plastic():
    run = True
    # Background 
    loc_plastic = os.getcwd()
    img_back = 'plastic_background.jpg'
    path_back = loc_plastic + "\\" + img_back
    imgplastic = pygame.image.load(path_back)
    imgplasticX = 0
    imgplasticY = 0

    
    while True:
        WIN.fill(BLACK)
        WIN.blit(imgplastic,(imgplasticX,imgplasticY))
        drawText("Plastic Bags", font, (LIGHTGRAY),WIN,375,75)

        # TEXT
        drawText("Plastic bags are one of the most damaging sources of everyday pollution.", font_2, (LIGHTGRAY),WIN,75,470)
        drawText("By some estimates, 1 trillion non-biodegradable plastic bags are disposed of each year,", font_2, (LIGHTGRAY),WIN,75,500)
        drawText("breaking down in waterways, clogging landfill sites and releasing toxic chemicals when burned", font_2, (LIGHTGRAY),WIN,75,530)

        #SOLUTION
        drawText("Solution", font, (LIGHTGRAY),WIN,75,570)
        drawText("Refuse plastic bags. Use a durable, foldable and inexpensive reusable bag for daily usage.", font_2, (LIGHTGRAY),WIN,75,610)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        pygame.display.update()

                  
def wipe():
    run = True
    # Background 
    loc_wipe = os.getcwd()
    img_back = 'wipe_background.png'
    path_back = loc_wipe + "\\" + img_back
    imgwipe = pygame.image.load(path_back)
    imgwipeX = 0
    imgwipeY = 0
    
    while True:
        WIN.fill(BLACK)
        WIN.blit(imgwipe,(imgwipeX,imgwipeY))
        drawText("Disposable Wipes", font, (BLACK),WIN,375,75)
        # TEXT
        drawText("20 million pounds of disposable wipes are thrown away every day in the U.S.", font_2, (BLACK),WIN,75,470)
        drawText("Made from plastic fibers and drenched in chemicals", font_2, (BLACK),WIN,75,500)
        drawText("Makeup wipes, wet wipes, and other single-use wipes are built to be durable once they get to the landfill.", font_2, (BLACK),WIN,75,530)
        drawText("As wipes break down, they drop plastic fibers into the soil, oftentime getting picked up by critters and wildlife or leaching chemicals into soil or water.", font_2, (BLACK),WIN,75,560)
        drawText("The vast majority brands are NOT biodegradable.", font_2, (BLACK),WIN,75,590)

        #SOLUTION
        drawText("Solution", font, (BLACK),WIN,75,570)
        drawText("Makeup wipe alternative: Invest in a soft washcloth and a makeup remover of your choice.", font_2, (BLACK),WIN,75,620)
        drawText("Microfiber cloths are suggested as an alternative since they can be washed regularly to avoid bacterial or viral build- up.", font_2, (BLACK),WIN,75,650)
        drawText("A better choice than using packages of disposable wipes.", font_2, (BLACK),WIN,75,680)

        
menu_page()


 





















