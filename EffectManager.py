
from pico2d import *

class Effect:
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    def __init__(self):
        print('effect Ready')
        self.explosionIndex = 0
        self.beamHitIndex = 0
        self.projectileIndex = 0


        self.explosionImage = load_image(r'resource\effect\e1.png'),load_image(r'resource\effect\e2.png')
        self.beamHitImage = load_image(r'resource\effect\r1.png'),load_image(r'resource\effect\r2.png'),load_image(r'resource\effect\r3.png')
        self.beamImage = (load_image(r'resource\effect\l3.png'), load_image(r'resource\effect\l4.png')),(load_image(r'resource\effect\l3.png'), load_image(r'resource\effect\l4.png')),(load_image(r'resource\effect\l5.png'), load_image(r'resource\effect\l6.png'))


    def Update(self,elapsedTime):
        self.explosionIndex = (self.explosionIndex +elapsedTime*5)%5
        self.beamHitIndex = (self.beamHitIndex + elapsedTime*5)%7
        self.projectileIndex = (self.projectileIndex + elapsedTime)%2
    def Draw(self,x,y,choose):
        if choose<3:
            self.DrawBeamHit(x, y, choose)
        elif choose<5:
            self.DrawExplosion(x,y,choose-3)


    def DrawExplosion(self,x,y,choose):
        self.explosionImage[choose].clip_draw(60*int(self.explosionIndex),0,60,60,x,y)
    def DrawBeamHit(self,x,y,choose):
        self.beamHitImage[choose].clip_draw(34 * int(self.beamHitIndex), 0, 33, 31, x, y)
    def DrawProjectile(self,x,y,choose):
        if self.projectileIndex<1:
            self.beamImage[choose][0].draw(x,y)
        else:
            self.beamImage[choose][1].draw(x, y)



