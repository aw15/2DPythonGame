

explosionImages = []
beamHitImage = []
beamImage = []


def SetEffectImage(explosion, beamHit,beam):
    global explosionImages, beamHitImage, beamImage
    explosionImages=explosion
    beamHitImage = beamHit
    beamImage = beam

def FireEffect():
    global effectIndex, fireEffect
    fireEffect.clip_draw(0, 128*effectIndex, 128, 128, 300, 300)
    effectIndex= (effectIndex+1)%8

explosionIndex = 0
def Explosion(elapsedTime,x,y):
    global explosion, explosionIndex
    explosionIndex= explosionIndex +elapsedTime
    explosion.clip_draw(60*int(explosionIndex),0,60,60,x,y)
    explosionIndex = (explosionIndex) % 5

projectileIndex = 0
def Projectile(index,elapsedTime,x,y):
    global projectileIndex
    projectileIndex = projectileIndex +elapsedTime
    if projectileIndex<1:
        beamImage[index][1].draw(x,y)
    else:
        beamImage[index][1].draw(x, y)
    projectileIndex = projectileIndex%2