from pygame import *

win = display.set_mode((1280, 720))
display.set_caption("Ping-pong")
back = transform.scale(image.load("back.jpg"), (1280, 720))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))    
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
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed

class Right(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

left = Left("left.jpg", 50, 50, 75, 350, 5)
right = Right("right.jpg", 1155, 50, 75, 350, 5)
ball = GameSprite("ball.png", 640, 380, 350, 150, 5)


clock = time.Clock()

game = True
while game:
    win.blit(back, (0, 0))
    left.reset()
    left.update()
    right.reset()
    right.update()
    ball.reset()
    ball.update()
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    display.update()
    clock.tick()
