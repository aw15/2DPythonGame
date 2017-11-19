


class Effect:
    explosionImage = []
    beamHitImage = []
    beamImage = []

    def __init__(self):
        print('effect Ready')

        self.explosionIndex = 0
        self.beamHitIndex = 0
        self.projectileIndex = 0
        self.effectPosition=set([])
        self.effectIndex = set([])
        pass
    def ResisterPosition(self,position):
        self.effectPosition.add(position)

    def Render(self,elapsedTime):
        self.explosionIndex = self.explosionIndex + elapsedTime
        for pos in self.effectPosition:
            self.Explosion(elapsedTime,pos[0],pos[1],1)
        self.effectPosition.clear()
        self.effectIndex.clear()

    def SetEffectImage(self,explosion, beamHit,beam):

        Effect.explosionImage = explosion
        Effect.beamHitImage = beamHit
        Effect.beamImage = beam

    def Explosion(self,elapsedTime,x,y,choose):
        Effect.explosionImage[choose].clip_draw(60*int(self.explosionIndex),0,60,60,x,y)
        self.explosionIndex = (self.explosionIndex) % 5


    def Projectile(self,elapsedTime,x,y,choose):
        self.projectileIndex = self.projectileIndex +elapsedTime
        if self.projectileIndex<1:
            Effect.beamImage[choose][0].draw(x,y)
        else:
            Effect.beamImage[choose][1].draw(x, y)
        self.projectileIndex = Effect.projectileIndex%2


    def BeamHit(self,elapsedTime,x,y,choose):
        self.beamHitIndex= self.beamHitIndex +elapsedTime
        Effect.beamHitImage[choose].clip_draw(33*int( self.beamHitIndex),0,33,31,x,y)
        self.beamHitIndex = ( self.beamHitIndex) % 7


effectManager = Effect()