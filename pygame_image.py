import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img2, True, False)
    bg_img3 = pg.image.load("fig/pg_bg.jpg")
    kok_img = pg.image.load("fig/3.png")
    kok_img = pg.transform.flip(kok_img, True, False)
    kok_rct = kok_img.get_rect()
    kok_rct.center = 300, 200
    tmr = 0
    # way_lst = [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT]
    # move_lst = [(0, -1), (0, 1), (-1, 0), (1, 0), ]
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img2, [-tmr+1600, 0])
        screen.blit(bg_img3, [-tmr+3200, 0])

        key_lst = pg.key.get_pressed()
    
        if key_lst[pg.K_UP]:
            x = -1
            y = -1
        elif key_lst[pg.K_DOWN]:
            x = -1
            y = 1
        elif key_lst[pg.K_LEFT]:
            x = -1
            y = 0
        elif key_lst[pg.K_RIGHT]:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        kok_rct.move_ip((x,y))

        screen.blit(kok_img, kok_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()