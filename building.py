import pygame as pg
from random  import randint
class Building:
    def __init__(self,scale_factor,move_speed) :
        self.img_up=pg.transform.scale_by(pg.image.load("pngegg.png").convert_alpha(), scale_factor )
        self.img_down=pg.transform.scale_by(pg.image.load("pngeggdown.png").convert_alpha(), scale_factor )
        self.rect_up=self.img_up.get_rect()
        self.rect_down=self.img_down.get_rect()
        self.building_distance=100
        self.rect_up.y=randint(250,520)
        self.rect_up.x=600
        self.rect_down.y=self.rect_up.y - self.building_distance -self.rect_up.height
        self.rect_down.x=600
        self.move_speed=move_speed

    def drawbuilding(self,win):
        win.blit(self.img_up,self.rect_up)
        win.blit(self.img_down,self.rect_down)

    def update(self,dt):
        self.rect_up.x-=self.move_speed*dt
        self.rect_down.x=self.move_speed*dt