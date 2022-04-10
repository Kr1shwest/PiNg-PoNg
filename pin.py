from pygame import *

win = display.set_mode((1280, 720))
display.set_caption("Ping-pong")
back = transform.scale(image.load("back.jpg"), (1280, 720))

clock = time.Clock()

game = True
while game:
    win.blit(back, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False

    
    display.update()
    clock.tick()