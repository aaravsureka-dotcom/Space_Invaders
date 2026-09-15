import pygame
import random
import math
import gif_pygame
import random
import time
import sys

pygame.init()

SCREEN_HIGHT = 650
SCREEN_WIDTH = 950
screen = pygame.display.set_mode((SCREEN_HIGHT, SCREEN_WIDTH))
pygame.display.set_caption("Space Invaders")

bgimage = pygame.image.load("0_R7cRRMTKCEVsa5s6.png")
bg_image = pygame.transform.scale(bgimage, (SCREEN_WIDTH, SCREEN_HIGHT))


clock = pygame.time.Clock()
running = True

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        ogimage = pygame.image.load("thatimage-removebg-preview.png").convert_alpha()


        self.image = pygame.transform.scale(ogimage,(50, 50))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.is_visible = True

    def draw(self, surface):
        if self.is_visible:
            surface.blit(self.image, self.rect)
    def letsgo(self):
        self.is_visible = False

        self.respawn_time = pygame.time.get_ticks() + 5000
        self.rect.x = 300

    def update(self):

        if not self.is_visible:
            if pygame.time.get_ticks() >= self.respawn_time:
                self.is_visible = True


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        ogimage = pygame.image.load("that.png-removebg-preview.png").convert_alpha()

        self.image = pygame.transform.scale(ogimage,(20, 20))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.is_shooting = False

        self.visible = False


    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def move(self,speed,x,y):
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.is_shooting = True
        self.visible = True
    def update(self):
        if self.is_shooting:
            self.rect.y -= self.speed
            if self.rect.y < 5:
                self.is_shooting = False
        else:
            self.visible = False



class Enemey(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        og_image = pygame.image.load("yeayeayeay-removebg-preview.png").convert_alpha()


        self.image = pygame.transform.scale(og_image, (35, 35))


        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = -1
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self,speed):
        if self.rect.x < 5:
            self.direction *= -1
        if self.rect.x > 600:
            self.direction *= -1
        self.rect.x += speed * self.direction
    def right(self,speed):
        self.rect.x += speed * 1
    def left(self,speed):
        self.rect.x += speed * -1


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        ogimage = pygame.image.load("that.png-removebg-preview.png").convert_alpha()

        self.image = pygame.transform.scale(ogimage,(20, 20))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.is_shooting = False

        self.visible = False


    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def move(self,speed,x,y):
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.is_shooting = True
        self.visible = True

    def update(self):
        if self.is_shooting:
            self.rect.y += self.speed
            if self.rect.y > SCREEN_WIDTH:
                self.is_shooting = False
                self.visible = False

class Hearts(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        image = pygame.image.load("yess-removebg-preview.png").convert_alpha()

        self.image = pygame.transform.scale(image,(50,50))

        self.rect = self.image.get_rect()

        self.rect.x = x

        self.rect.y = y

        self.is_visible = True
    def draw(self,surface):
        if self.is_visible:
            surface.blit(self.image, self.rect)


class GameOVARtext(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        image = pygame.image.load("gameova-removebg-preview.png").convert_alpha()

        self.image = pygame.transform.scale(image, (200, 200))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.is_visible = False
    def draw(self,surface):
        if self.is_visible:
            surface.blit(self.image,self.rect)
SCREEN_HIGHT = 650
SCREEN_WIDTH = 950
game = GameOVARtext(x=250,y=450)


heart_list = []

start_y = 800
start_x = 0

for item in range(1,4):
    hart = Hearts(x=start_x,y=start_y)
    start_x += 60
    heart_list.append(hart)



enemy_list = []
xx = 100
yy = 67
for item in range(35):
    enasdas = Enemey(x=xx, y=yy)
    enemy_list.append(enasdas)


    xx += 60
    if xx > 500:
        yy += 60
        xx = 100



player = Player(300, 800)
bullet = Bullet(300, 700)
enemy_bullet = EnemyBullet(x=300,y=700)
direction = "right"
lives = 3
game_over = False

while running:




    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bgimage, (0, 0))
    if enemy_bullet.visible:
        enemy_bullet.draw(screen)
    for item in enemy_list[:]:
        random_number = random.randint(0,2551)
        if random_number == 42 and enemy_bullet.is_shooting == False and game_over == False:
            enemy_bullet.move(speed=7,x=item.rect.x,y=item.rect.y)
            print("YEA")

        if item.rect.x > 590:
            direction = "left"
        if item.rect.x < 5:
            direction = "right"

        if direction == "right" and game_over == False:
            item.right(speed=5)
        elif direction == "left" and game_over == False:
            item.left(speed=5)
        item.draw(screen)
        if bullet.rect.colliderect(item.rect) and bullet.is_shooting and game_over == False:
            enemy_list.remove(item)
            item.kill()
            bullet.kill()
            bullet.is_shooting = False

    if enemy_bullet.rect.colliderect(player.rect) and enemy_bullet.is_shooting and game_over == False:
        lives -= 1
        this = -1 if len(heart_list) > 1 else 0
        heart_list.pop(this)
        enemy_bullet.is_shooting = False
        enemy_bullet.visible = False
        enemy_bullet.rect.y = -100
    if len(heart_list) <= 0:
        game_over = True
        game.is_visible = True


    for thingimagigs in heart_list[:]:
        thingimagigs.draw(screen)
    player.update()
    bullet.update()
    enemy_bullet.update()




    player.draw(screen)
    game.draw(screen)
    if bullet.visible:
        bullet.draw(screen)

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.rect.x > 0 and player.is_visible and game_over == False:
        player.rect.x -= 3
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.rect.x < 600 and player.is_visible and game_over == False:
        player.rect.x += 3
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and bullet.is_shooting == False and player.is_visible and game_over == False:
        bullet.move(4.67,player.rect.x,player.rect.y)




    pygame.display.flip()

    pygame.display.update()

    clock.tick(60)

pygame.quit()