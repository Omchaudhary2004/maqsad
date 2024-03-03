import pygame as pg
import sys,time
from Plane import Plane
from building import Building
pg.init()

class Game:
    def __init__(self) :
        self.width = 600
        self.height = 768
        self.scale_factor=0.05
        self.win = pg.display.set_mode((self.width,self.height))
        self.clock=pg.time.Clock()
        self.move_speed=250
        self.Plane=Plane(self.scale_factor)
        self.is_enter_pressed= False
        self.buildings=[]
        self.building_generator_counter=71
        self.setUpBgAndGround() 
        self.sound_sfx = pg.mixer.Sound("Allahu Akbar Sound Effect.mp3")
        
        self.gameLoop()

    def gameLoop(self):
        last_time = time.time()
        while True:
           #calculating delta time
            new_time=time.time()
            dt=new_time-last_time
            last_time=new_time
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type==pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.is_enter_pressed=True
                    
                    if event.key==pg.K_SPACE and self.is_enter_pressed:
                        self.Plane.fly(dt)


            self.updateEverything(dt)
            self.checkCollision()
            self.drawEverything()
            pg.display.update()
            self.clock.tick(60)

    def checkCollision(self):
        if len(self.buildings):
            if (self.Plane.rect.bottom>568 or self.Plane.rect.colliderect(self.buildings[0].rect_up)):
                self.Plane.update_on=False
                self.is_enter_pressed = False
                self.sound_sfx.play()

    
    def updateEverything(self, dt):
        if self.is_enter_pressed:
            self.ground1_rect.x -= self.move_speed*dt
            self.ground2_rect.x -= self.move_speed*dt

            if self.ground1_rect.right<0:
                self.ground1_rect.x=self.ground2_rect.right
            
            if self.ground2_rect.right<0:
                self.ground2_rect.x=self.ground1_rect.right
           
            if self.building_generator_counter>70:
                self.buildings.append(Building(self.scale_factor,self.move_speed))
                self.building_generator_counter=0
            
            self.building_generator_counter+=1



            for building in self.buildings:
            
                building.update(dt)



            self.Plane.update(dt)
 



    def drawEverything(self):
        self.win.blit(self.bg_img,(0,0))
        
        for building in self.buildings:
            building.drawbuilding(self.win)
        
        self.win.blit(self.ground1_img,self.ground1_rect)
        self.win.blit(self.ground2_img,self.ground2_rect)
        self.win.blit(self.Plane.image,self.Plane.rect)

    def setUpBgAndGround(self):
        self.bg_img =pg.transform.scale( pg.image.load("2544px-Twin_Towers-NYC (1).jpg").convert(),(600,768))
        self.ground1_img=pg.transform.scale( pg.image.load("37623 (1).jpg"),(600,768))
        self.ground2_img=pg.transform.scale( pg.image.load("37623 (1).jpg"),(600,768))

        self.ground1_rect = self.ground1_img.get_rect()
        self.ground2_rect = self.ground2_img.get_rect()        

        self.ground1_rect.x=0
        self.ground2_rect.x=self.ground1_rect.right
        self.ground1_rect.y=568
        self.ground2_rect.y=568

        

game=Game()