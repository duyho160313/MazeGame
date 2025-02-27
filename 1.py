import pygame.display
from pygame import *

' ' 'Required classes' ' '


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()

        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.y >= 400:
            self.direction = "left"
        if self.rect.y <= 60:
            self.direction = "right"
        if self.direction == "left":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))

        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

mixer.init()
mixer.music.load("jungles.ogg")
mixer.music.play()
#window size
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background2.png"), (win_width, win_height))
FPS = 60
clock = time.Clock()
treasure = GameSprite("treasure_chest_sprite-removebg-preview.png", 500, 300, 0)
player = Player("player_sprite-removebg-preview.png", 140, 300, 4)
enemy = Enemy("Enemy_sprite-removebg-preview.png", 400, 100, 3)


wall1 = Wall(247, 254, 155, 100, 20, 450, 10)
wall2 = Wall(154, 205, 50, 100, 480, 350, 10)
wall3 = Wall(154, 205, 50, 100, 20 , 10, 380)
game = True
finish = False
font.init()
font = font.SysFont("Arial", 70)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        player.update()
        enemy.update()
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3):
            finish = True
            lose = font.render("You lose", True, (255,215, 0))
            window.blit(lose, (200,200))
        if sprite.collide_rect(player, treasure):
            finish = True
            win = font.render("You win", True, (255,215,0))
            window.blit(win, (200, 200))
        player.reset()
        enemy.reset()
        treasure.reset()
        wall1.draw_wall()
        wall3.draw_wall()
        wall2.draw_wall()
    pygame.display.update()
    clock.tick(FPS)