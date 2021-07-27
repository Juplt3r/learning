import pygame
import time
pygame.init()
#Colours
red = (255 , 0, 0)
white = (255 ,255 ,255)
black = (0, 0, 0)
green = (0, 255, 0)

#Board Size
width = 500
height = 500
Display = pygame.display.set_mode((width,height))
running = True
clock = pygame.time.Clock()

#Snake starting Location
SNx1 = width/2
SNy1 = height/2

#change in snake
ChangeX1 = 0
ChangeY1 = 0

font_style = pygame.font.SysFont(None, 50)
def message(msg):
    mesg = font_style.render(msg, True, red)
    Display.blit(mesg, [width/3, height/3])

while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ChangeX1 = -10
                ChangeY1 = 0
            if event.key == pygame.K_RIGHT:
                ChangeX1 = 10
                ChangeY1 = 0  
            if event.key == pygame.K_UP:
                ChangeX1 = 0
                ChangeY1 = -10                             
            if event.key == pygame.K_DOWN:
                ChangeX1 = 0
                ChangeY1 = 10               
    if  width<SNx1 or SNx1<0 or height<SNy1 or SNy1<0:
        running = False



    SNx1 += ChangeX1
    SNy1 += ChangeY1   
    print(SNx1,SNy1)
    pygame.draw.rect(Display,green,[SNx1,SNy1,10,10])
    pygame.display.update()
    clock.tick(10)
    Display.fill(white)
message("Game Over")
pygame.display.update()
time.sleep(2)
pygame.quit()



