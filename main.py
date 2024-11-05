import pygame as pg

window = pg.display.set_mode((600,400))
display = pg.Surface()
pg.display.set_caption("demo")
clock = pg.time.Clock()
pg.init()

def event_handler():
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    #self.dyNAMIC RES
    dynamic_res = pg.transform.scale(display, (config['width'], config['height']))
    window.blit(dynamic_res, (0,0))



    #calculate frames
    frames = clock.get_fps()
    
    ms = clock.tick(60)
    frames = frames * ms
    #print(frames)
    pg.display.flip()

while True:
    display.fill(0)


    eventHandler()