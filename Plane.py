import pygame as pg
from pygame.sprite import Group


class Plane(pg.sprite.Sprite):
    def __init__(self,scal_factor):
        super(Plane,self).__init__()
        self.img_list=[pg.transform.scale_by(pg.image.load("United_747.png").convert_alpha(),scal_factor),
            pg.transform.scale_by(pg.image.load("United_747 copy.png").convert_alpha(),scal_factor)]
        self.image_index=0
        self.image=self.img_list[self.image_index]
        self.rect=self.image.get_rect(center=(100,100))
        self.y_velocity=0
        self.gravity=10
        self.flap_speed =250
        self.anim_counter=0
        self.update_on = True
        
    def update(self,dt):
        if self.update_on:
            self.playAnimation()
            self.applyGravity(dt)

            if self.rect.y <=0:
                self.rect.y=0
                self.flap_speed=0
            elif self.rect.y >=0 and self.flap_speed==0:
                self.flap_speed=0


    def applyGravity(self,dt):
        self.y_velocity += self.gravity*dt
        self.rect.y += self.y_velocity

    def fly(self,dt):
        self.y_velocity=-self.flap_speed*dt

    def playAnimation(self):
        if self.anim_counter ==5:
            self.image=self.img_list[self.image_index]
            if self.image_index==0 :
                self.image_index=1
            else:
                self.image_index=0
        
        self.anim_counter+=1


        
