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


clock = time.Clock()

game = True
while game:
    win.blit(back, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    
    display.update()
    clock.tick()
