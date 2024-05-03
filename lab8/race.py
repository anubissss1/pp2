import pygame
import random
import time
import sys

pygame.init()

FPS = pygame.time.Clock()

SPEED = 5
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

background_image = pygame.image.load('AnimatedStreet.png')
player_image = pygame.image.load('Player.png')
enemy_image = pygame.image.load('Enemy.png')
coin_image = pygame.image.load('Coin.png')
coin_image = pygame.transform.scale(coin_image, (30, 30))
player_rect = player_image.get_rect()
enemy_rect = enemy_image.get_rect()
coin_rect = coin_image.get_rect()
font = pygame.font.Font(None, 36)
coin_cnt = 0
player_rect.center = (200, 520)
background_image = pygame.transform.scale(background_image, (400, 600))

screen = pygame.display.set_mode((400, 600))

done = False


def move(rect):
    pressed = pygame.key.get_pressed()

    if rect.left > 0:
        if pressed[pygame.K_LEFT]:
            rect.move_ip(-5, 0)
    if rect.right < 600:
        if pressed[pygame.K_RIGHT]:
            rect.move_ip(5, 0)


def spawn(rect):
    rect.move_ip(0, SPEED)
    if rect.top > 600:
        rect.top = 0
        rect.center = (random.randint(30, 370), 0)


def respawn(rect, enemy_rect):
    rect.top = 0
    while True:
        rect.center = (random.randint(30, 370), 0)
        if not rect.colliderect(enemy_rect):  # Check if coin doesn't collide with enemy
            break


while not done:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5

        if event.type == pygame.QUIT:
            done = True

    screen.blit(background_image, (0, 0))

    coin_text = font.render(str(coin_cnt), True, (0, 0, 0))

    if player_rect.colliderect(coin_rect):
        coin_cnt += 1
        respawn(coin_rect, enemy_rect)

    if player_rect.colliderect(enemy_rect):
        screen.fill((255, 0, 0))
        pygame.display.flip()
        time.sleep(2)
        sys.exit()

    spawn(coin_rect)
    move(player_rect)
    spawn(enemy_rect)


    screen.blit(player_image, player_rect)
    screen.blit(enemy_image, enemy_rect)
    screen.blit(coin_image, coin_rect)
    screen.blit(coin_text, (10, 10))

    FPS.tick(60)
    pygame.display.flip()