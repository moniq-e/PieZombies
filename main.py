import pygame
from sys import exit
from functions import kb
import playerClass
import entity
from random import randint

pygame.init()
screen = pygame.display.set_mode((900, 600))
font = pygame.font.SysFont('calibri', 20)
ADDENEMY = pygame.USEREVENT + 1
BULLET = pygame.USEREVENT + 2
pygame.time.set_timer(BULLET, 250)
pygame.time.set_timer(ADDENEMY, 2000)
player = playerClass.Player(screen, 20, 20, (255, 255, 255))
entities = []
entities.append(player)
clock = pygame.time.Clock()

while True:
    fix = clock.tick(60)

    screen.fill((0, 0, 0))
    if pygame.event.get(pygame.QUIT):
        pygame.quit()
        exit()

    if pygame.event.get(ADDENEMY):
        entities.append(entity.Entity(randint(0, screen.get_width()), randint(
            0, screen.get_height()), 20, 20, (44, 190, 200), 10, 0.1))

    player.move(screen, fix)
    if pygame.event.get(BULLET):
        player.shoot(fix)

    for e in entities:
        if not isinstance(e, playerClass.Player):
            if e.rect.colliderect(player.rect):
                player.life -= e.damage

    for b in player.bullets:
        if b.x > screen.get_width() or b.x < 0 or b.y > screen.get_height() or b.y < 0:
            player.bullets.remove(b)
        for e in entities:
            if not isinstance(e, playerClass.Player):
                if b.rect.colliderect(e.rect):
                    e.life -= b.damage
                    pos = kb(b.initial, e, 20)
                    e.x = pos['x']
                    e.y = pos['y']
                    player.bullets.remove(b)
        b.draw(screen)

    for i in entities:
        if isinstance(i, playerClass.Player) and i.life <= 0:
            pygame.quit()
            exit()
        if i.life > 0:
            i.draw(screen, player, entities)
        else:
            entities.remove(i)

    pygame.display.update()
