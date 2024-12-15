import pygame

import random

import sys

pygame.init()

sw,sh = 800,600

screen = pygame.display.set_mode((sw,sh))

pygame.display.set_caption('Welcome to color catching game')

white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)

class player:
    def __init__(self,x,y,size,speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed

    def move(self,keys):
        if keys[pygame.K_LEFT]:
            self.x = self.x - self.speed
        if keys[pygame.K_RIGHT]:
            self.x = self.x + self.speed
        if keys[pygame.K_UP]:
            self.y = self.y - self.speed
        if keys[pygame.K_DOWN]:
            self.y = self.y + self.speed

        self.x = max(0,min(sw - self.size,self.x))
        self.y = max(0,min(sh - self.size,self.y))

    def draw(self,screen):
        pygame.draw.rect(screen,red,(self.x,self.y,self.size,self.size))

    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.size,self.size)
        
class movingcircle:
    def __init__(self,size):
        self.size = size
        self.x = random.randint(size,sw - size)
        self.y = random.randint(size,sh - size)

    def respawn(self):
         self.x = random.randint(self.size,sw - self.size)
         self.y = random.randint(self.size,sh - self.size)

    def draw(self,screen):
         pygame.draw.circle(screen,blue,(self.x,self.y),self.size)
        
    def get_rect(self):
        return pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
    
    
class catching_game:
    def __init__(self):
        self.screen = pygame.display.set_mode((sw,sh))
        pygame.display.set_caption("square and circle catching game")
        self.clock = pygame.time.Clock()
        self.player = player(x = sw// 2, y = sh // 2, size = 50, speed = 5 )
        self.circle = movingcircle(size = 30)
        self.score = 0


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            keys = pygame.key.get_pressed()
            self.player.move(keys)
            if self.player.get_rect().colliderect(self.circle.get_rect()):
                self.score += 1
                
                self.circle.respawn()
            self.screen.fill(white)
            self.player.draw(self.screen)
            self.circle.draw(self.screen)
            font = pygame.font.Font(None,36)
            score_text = font.render(f"Score;{self.score}", True, (0,0,0))
            self.screen.blit(score_text,(10,10))
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
        sys.exit()
obj = catching_game()
obj.run()

