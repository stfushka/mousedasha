from pygame import *

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
        if keys[K_RIGHT] and self.rect.x < w_width-80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < w_height-70:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= w_width-85:
            self.direction = 'left'

        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2 
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
w_width = 600
w_height = 400

window = display.set_mode((w_width, w_height))
display.set_caption('Maze')

background = transform.scale(image.load('background.jpg'), (w_width, w_height))

player = Player('hero.png', 5,w_height-80, 4)
monster = Enemy('cyborg.png', w_width-80, 280, 2)
final = GameSprite('treasure.png', w_width-120, w_height-80, 0)

w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 380)
w4 = Wall(154, 205, 50, 200, 250, 10, 230)
w5 = Wall(154, 205, 50, 300, 20, 10, 380)
w6 = Wall(154, 205, 50, 440, 100, 10, 130)
w7 = Wall(154, 205, 50, 440, 350, 10, 130)
w8 = Wall(154, 205, 50, 550, 20, 10, 250)

game = True
finish = False
clock = time.Clock()
FPS = 60

# mixer.init()
# mixer.music.load('jungles.ogg')
# mixer.music.play()

# money = mixer.Sound('money.ogg')
# kick = mixer.Sound('kick.ogg')

font.init()
font = font.SysFont('Arial', 70)
win = font.render('You win', True, (225, 215,0))
lose = font.render('You lose', True, (180, 215,0))

while game == True:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        window.blit(background, (0,0))
        player.update()
        monster.update()

        player.reset()
        monster.reset()
        final.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()
        w8.draw_wall()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) :
            finish = True
            window.blit(lose, (260,230))
            # kick.play()

        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (260,230))
            # money.play()

        display.update()
        clock.tick(FPS)






