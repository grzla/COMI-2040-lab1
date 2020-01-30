"""
Lesson 1 - Lab 1 - Splatter art

Greg Lundberg
1/29/20

User clicks to splatter paint on canvas randomly. After 10 clicks, canvas is reset.
"""

import random

# Import and initialize pygame.
import pygame

pygame.init()

# Define constants and annotate variables
SIZE: int = 600
# Rough offset for splatter centers
SPLAT_OFFSET: int = 100
background: pygame.Surface
red_splatter: pygame.Surface
orange_splatter: pygame.Surface
yellow_splatter: pygame.Surface
green_splatter: pygame.Surface
blue_splatter: pygame.Surface
purple_splatter: pygame.Surface
splatter: pygame.image
splatters: []
captions: []
user_quit: bool
count: int
event: pygame.event.Event
canvas_h: tuple
canvas_w: tuple
x: int
y: int

# Load assets
background = pygame.image.load("art_studio.jpg")
red_splatter = pygame.image.load("red_splatter.png")
orange_splatter = pygame.image.load("orange_splatter.png")
yellow_splatter = pygame.image.load("yellow_splatter.png")
green_splatter = pygame.image.load("green_splatter.png")
blue_splatter = pygame.image.load("blue_splatter.png")
purple_splatter = pygame.image.load("purple_splatter.png")

# Load splatters and final captions in lists to simplify random selection
splatters = [
    red_splatter, 
    orange_splatter, 
    yellow_splatter, 
    green_splatter, 
    blue_splatter, 
    purple_splatter
    ]

captions = [
    "A masterpiece!",
    "Finished!", 
    "Ready for MOBA!", 
    "A work of genius!", 
    "You've really got something!"
    ]

# Define canvas height and width ranges
canvas_h = (64,452)
canvas_w = (72,378)

# Create a pygame window.
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Click to paint!")

# Prepare game loop for run
screen.blit(background, (0,0))   
user_quit = False
count = 0

while not user_quit:
    for event in pygame.event.get():
        # Process a quit choice
        if event.type == pygame.QUIT:
            user_quit = True
        # Process clicks 
        elif event.type == pygame.MOUSEBUTTONUP:
            # Reset on click following tenth splatter
            if count == 10:
                screen.blit(background, (0,0))
                pygame.display.set_caption("Click to paint!")
                count = 0
            else: 
                # Draw random splatter
                splatter = random.choice(splatters)
                x = random.randint(*canvas_w) - SPLAT_OFFSET
                y = random.randint(*canvas_h) - SPLAT_OFFSET
                screen.blit(random.choice(splatters), (x,y))
                pygame.display.set_caption("Perfect!")
                count += 1
                # Select random caption if tenth click
                if count == 10:
                    pygame.display.set_caption(random.choice(captions))
    # Show the drawing
    pygame.display.flip()

pygame.quit()