import pygame
from functions import kb

class Entity:
    def __init__(self, x, y, width, height, color, life, damage):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.life = life
        self.damage = damage
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = 0.5

    def draw(self, screen, player, entities):
        if not self.rect.colliderect(player.rect):
            pos = kb(player, self, -1.5)
            self.x = pos.x
            self.y = pos.y
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)
