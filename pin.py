from pygame import *

win = display.set_mode((1280, 720))
display.set_caption("Ping-pong")
back = transform.scale(image.load("back.jpg"), (1280, 720))

class GameSpriteL(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(left), (size_x, size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
        self.direction = "left"
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class GameSpriteR(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(right), (size_x, size_y))    
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
        self.direction = "left"
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Left(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < 650:
            self.rect.x += self.speed

class Right(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_DOWN] and self.rect.x < 650:
            self.rect.x += self.speed

clock = time.Clock()

game = True
while game:
    win.blit(back, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    
    display.update()
    clock.tick()
