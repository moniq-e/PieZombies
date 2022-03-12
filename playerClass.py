import pygame

class Initial:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Bullet:
    def __init__(self, face, x, y, width, height, color, speed, damage):
        self.face = face
        self.initial = Initial(x, y)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.damage = damage
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.score = 0

    def draw(self, screen):
        if self.face == 'up':
            self.y -= self.speed
        elif self.face == 'down':
            self.y += self.speed
        elif self.face == 'left':
            self.x -= self.speed
        elif self.face == 'right':
            self.x += self.speed
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)

class Player:
    def __init__(self, screen, width, height, color):
        self.x = screen.get_width() / 2
        self.y = screen.get_height() / 2
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.bullets = []
        self.speed = 0.3
        self.score = 0
        self.life = 30
        self.face = 'right'

    def draw(self, screen, player, entities):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, screen, fix):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.x > 0:
            self.x -= self.speed * fix
            self.face = 'left'
        if keys[pygame.K_d] and self.x < screen.get_width() - self.width:
            self.x += self.speed * fix
            self.face = 'right'
        if keys[pygame.K_w] and self.y > 0:
            self.y -= self.speed * fix
            self.face = 'up'
        if keys[pygame.K_s] and self.y < screen.get_height() - self.height:
            self.y += self.speed * fix
            self.face = 'down'
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def shoot(self, fix):
        self.bullets.append(Bullet(self.face, self.x + self.width/2, self.y + self.height/2, 2, 2, (255, 255, 255), 0.8 * fix, 5))
