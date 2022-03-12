import pygame

class Bullet:
    def __init__(self, face, x, y, width, height, color, speed, damage):
        self.face = face
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
        self.speed = 0.5
        self.score = 0
        self.life = 30
        self.face = 'right'

    def draw(self, screen, player):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, fix):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x -= self.speed * fix
            self.face = 'left'
        if keys[pygame.K_d]:
            self.x += self.speed * fix
            self.face = 'right'
        if keys[pygame.K_w]:
            self.y -= self.speed * fix
            self.face = 'up'
        if keys[pygame.K_s]:
            self.y += self.speed * fix
            self.face = 'down'
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def shoot(self, fix):
        self.bullets.append(Bullet(self.face, self.x + self.width/2, self.y + self.height/2, 2, 2, (255, 255, 255), 0.8 * fix, 5))
