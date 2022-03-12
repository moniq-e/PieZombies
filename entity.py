import pygame
import functions


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
        self.score = 0

    def draw(self, screen, player):
        pos = functions.kb(player, self, -2)
        self.x = pos['x']
        self.y = pos['y']
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)
