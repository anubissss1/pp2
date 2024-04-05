import pygame
from datetime import datetime

pygame.init()#init. pygame as a module
screen = pygame.display.set_mode((1400, 1050))#setting up screen

bg_image = pygame.image.load('/Users/_anubissss_/Desktop/clock.png')#assigning pictures to constats
sec_img = pygame.image.load('/Users/_anubissss_/Desktop/leftarm.png')
min_img = pygame.image.load('/Users/_anubissss_/Desktop/rightarm.png')


rect = bg_image.get_rect(center=(700, 525))#setting clock as a bg

process = True
while process :
    pygame.display.set_caption('Mickey Clock')
    screen.blit(bg_image, (0, 0))#centerring bg imagep
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            process = False

    time = datetime.now().time()
    angle_sec = -(time.second * 6)
    sec_in_img = pygame.transform.rotate(sec_img, angle_sec)
    sec_rect = sec_in_img.get_rect(center=rect.center)
    screen.blit(sec_in_img, sec_rect.topleft)

    min_angle = -(time.minute * 6)
    nmin_img = pygame.transform.rotate(min_img, min_angle)
    min_rect = nmin_img.get_rect(center=rect.center)
    screen.blit(nmin_img, min_rect.topleft)

    pygame.display.flip()