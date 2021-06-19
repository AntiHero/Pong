import sys, pygame as pg

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
TICK_RATE = 30

pg.init()

size = width, height = SCREEN_WIDTH, SCREEN_HEIGHT

screen = pg.display.set_mode(size)
clock = pg.time.Clock()

ball = pg.Rect(380, 280, 20, 20) 
ball_color = 54, 185, 255

paddle = pg.Rect(350, 580, 100, 20)
paddle_color = 255, 255, 255

directions = {pg.K_LEFT: (-5, 0), pg.K_RIGHT: (5, 0)}


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
   
    screen.fill((0, 0, 0))
    
    pg.draw.rect(screen, ball_color, ball)
    pg.draw.rect(screen, paddle_color, paddle)

    if event.type == pg.KEYDOWN:
        if event.key in directions:
            v = directions[event.key]
            paddle.move_ip(v)
    
    pg.display.update()
    clock.tick(TICK_RATE)