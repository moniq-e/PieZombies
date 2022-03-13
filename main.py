import math
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
HEAL = pygame.USEREVENT + 3
pygame.time.set_timer(BULLET, 250)
pygame.time.set_timer(ADDENEMY, 2000)
pygame.time.set_timer(HEAL, 1000)
player = playerClass.Player(screen, 20, 20, (255, 255, 255), 0.1)
entities = []
entities.append(player)
clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    fix = clock.tick(60)

    if pygame.event.get(pygame.QUIT):
        pygame.quit()
        exit()

    if pygame.event.get(ADDENEMY):
        entities.append(entity.Entity(randint(0, screen.get_width()), randint(0, screen.get_height()), 20, 20, (44, 190, 200), 10, 0.1))

    player.move(screen, fix)

    if pygame.event.get(BULLET):
        player.shoot(fix)

    if pygame.event.get(HEAL) and player.life < player.maxlife:
        player.life += player.heal

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
                    if b in player.bullets:
                        e.life -= b.damage
                        pos = kb(b.initial, e, 20)
                        e.x = pos.x
                        e.y = pos.y
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
            player.score += 1

    lifetxt = f'Life: {math.floor(player.life * 10) / 10}'
    life = font.render(lifetxt, True, (255, 255, 255))
    screen.blit(life, ((screen.get_width()/2) - (len(lifetxt)*5), 5))

    scoretxt = f'Score: {player.score}'
    score = font.render(scoretxt, True, (255, 255, 255))
    screen.blit(score, ((screen.get_width()/2) - (len(scoretxt) * 6), 30))

    pygame.display.update()
