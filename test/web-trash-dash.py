import pygame as pg

pg.init()

disp = pg.display.set_mode((200, 200))

clock = pg.time.Clock()

while True:
    clock.tick(8)
    for e in pg.event.get():
        if e.type == pg.QUIT:
            pg.quit()
            break
    disp.fill(pg.Color("black"))
    pg.display.update()
