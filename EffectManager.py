
from pico2d import *

class Effect:
    explosionImage = None
    beamHitImage = None
    beamImage = None
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

    def __init__(self):
        print('effect Ready')
        self.explosionIndex = 0
        self.beamHitIndex = 0
        self.projectileIndex = 0

        self.effectPosition=set([])

        if Effect.explosionImage == None:
            Effect.explosionImage = load_image(r'resource\effect\e1.png'),load_image(r'resource\effect\e2.png')
            Effect.beamHitImage = load_image(r'resource\effect\r1.png'),load_image(r'resource\effect\r2.png'),load_image(r'resource\effect\r3.png')
            Effect.beamImage = (load_image(r'resource\effect\l3.png'), load_image(r'resource\effect\l4.png')),(load_image(r'resource\effect\l3.png'), load_image(r'resource\effect\l4.png')),(load_image(r'resource\effect\l5.png'), load_image(r'resource\effect\l6.png'))

    def Draw(self,frameTime):
        self.DrawExplosion(100,100,1)
        self.DrawBeamHit(200,200,2)
        self.DrawProjectile(300,300,1)
    def Update(self,elapsedTime,effectType, effectPosition):
        self.explosionIndex = (self.explosionIndex +elapsedTime*5)%5
        self.beamHitIndex = (self.beamHitIndex + elapsedTime*5)%7
        self.projectileIndex = (self.projectileIndex + elapsedTime)%2

    def DrawExplosion(self,x,y,choose):
        Effect.explosionImage[choose].clip_draw(60*int(self.explosionIndex),0,60,60,x,y)
    def DrawBeamHit(self,x,y,choose):
        Effect.beamHitImage[choose].clip_draw(34 * int(self.beamHitIndex), 0, 33, 31, x, y)
    def DrawProjectile(self,x,y,choose):
        if self.projectileIndex<1:
            Effect.beamImage[choose][0].draw(x,y)
        else:
            Effect.beamImage[choose][1].draw(x, y)



