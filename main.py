import os,  pygame,  random,  time,  datetime, random

from Alien import *
from Ship import *
from Bullet import *
from AlienBullet import *
from MotherShip import *
from Shield import *
from Explosion import *

def setupAliens():
    list = [[], [], [], [], [], [], [], [], [], [],[] ]
    startingX =6
    startingY=120
    i=0
    j=0
    alienImage=""
    alienType=0

    while i < 11:
        while j< 5:
            if j==0:
                alienType=1
            if j==1 or j==2:
                alienType=2
            if j==3 or j==4:
                alienType=3
            list[i].append(Alien(startingX + (i*36), startingY+(j*36), alienType))
            j=j+1
        i = i+1
        j=0
    return list

def moveAliens():
    global lastMoved
    global direction
    global lastDirection
    global explosionList
    global alienSpeed
    
    #see if we need to change direction
    for row in alienList:
        for a in row:
            if a.imageRect.right>=595 :
                if lastDirection == "Down":
                    direction="Left"
                else:
                    direction = "Down"
                break
            if a.imageRect.left<=5:
                if lastDirection == "Down":
                    direction="Right"
                else:
                    direction = "Down"
                break

    #see if we need to move
    if (time.time() - lastMoved) >= (1/alienSpeed):
        explosionList=[]
        lastMoved= time.time()    
        for column in alienList:
            for a in column:
                if direction == "Left":
                        a.moveAlien(-5, 0)
                        lastDirection = "Left"
                if direction == "Right":
                        a.moveAlien(5, 0)
                        lastDirection = "Right"
                if direction == "Down":
                        a.moveAlien(0, 20)
                        lastDirection = "Down"
        if lastDirection =="Down":
            alienSpeed=alienSpeed+0.5

    #need to always blit it
    for column in alienList:
        for a in column:
            screen.blit(a.image, a.imageRect)
            
def moveBullet(bullet):
        bullet.move()
        screen.blit(bullet.image, bullet.imageRect)

def moveAlientBullet(alienBullet):
    alienBullet.move()
    screen.blit(alienBullet.image, alienBullet.imageRect )

def moveShip():
    ship.move()
    screen.blit(ship.image, ship.imageRect)

def checkForCollisions(bulletList,alienBulletList, ship):
    global gameMode
    global alienList
    global motherShip
    global shieldList
    global score
    global explosionList
    
    for b in bulletList:
        #hit the mothership
        if motherShip !="":
            if b.imageRect.colliderect(motherShip.imageRect):
                explosionList.append(Explosion(motherShip.imageRect.left,  motherShip.imageRect.top))
                bulletList.remove(b)
                score = score + 100
                motherShip =""
                alienExplodeSound.play()
                
        #if the player missed
        if b.imageRect.bottom < 0:
            bulletList.remove(b)
        for s in shieldList:
            if(s.checkForCollision(b.imageRect)==1):
                bulletList.remove(b)
    
    for ab in alienBulletList:
        #if the alien missed
        if ab.imageRect.bottom > 600:
            alienBulletList.remove(ab)
        #if the aliens got the player
        if (ab.imageRect.colliderect(ship.imageRect)):
            gameMode="GAMEOVER"
        for s in shieldList:
            if (s.checkForCollision(ab.imageRect)==1):
                alienBulletList.remove(ab)
            

    noAliens = 1
    for column in alienList:
        if (len(column)!=0):
            noAliens=0
        for a in column:
            for b in bulletList:
                #if the player hit an alien with a bullet
                if (a.imageRect.colliderect(b.imageRect)):
                    bulletList.remove(b)
                    explosionList.append(Explosion(a.imageRect.left,  a.imageRect.top))
                    if a.alienType==1:
                        score = score+40
                    if a.alienType==2:
                        score = score+20
                    if a.alienType==3:
                        score = score +10
                    column.remove(a)
                    alienExplodeSound.play()
            #if an alien crashed into the ship
            for s in shieldList:
                s.checkForCollision(a.imageRect)
    
            if (a.imageRect.colliderect(ship.imageRect)):
                gameMode="GAMEOVER"
    if noAliens == 1:
    #reset aliens
        alienList = setupAliens()
        
def getAliensWhoCanShoot():
    list = []
    for column in alienList:
        size = len(column)
        if size != 0:
            list.append(column [size-1])
    return list

def alienShoot():
    global alienBulletList
    global alienList
    
    aliensWhoCanShoot=getAliensWhoCanShoot()
    

    size = len(aliensWhoCanShoot)
    if size >0:
        if (size > 3):
            numToShoot = random.randrange(0, 3)
        else:
            numToShoot = random.randrange(0, size)
        random.shuffle(aliensWhoCanShoot)
        count = 0 
        while count < numToShoot:
            alienBulletList.append(AlienBullet(aliensWhoCanShoot[count].getLocationX()+(aliensWhoCanShoot[count].imageRect.width/2), aliensWhoCanShoot[count].getLocationY(), "./img/missile_alien.png"))
            count=count + 1    
        
def moveMotherShip():
    global lastMotherShip
    global motherShipDirection
    global motherShip
    global lastMoved
    
    #todo: Play the sound?
    
    #move it in the right direction
    if motherShipDirection == "Left":
        motherShip.imageRect = motherShip.imageRect.move(-1, 0)
    else:
        motherShip.imageRect = motherShip.imageRect.move(1, 0)
        
    screen.blit(motherShip.image, motherShip.imageRect)
    
    #destroy it if it goes off screen and change next ones direction
    if motherShip.imageRect.left > 850 or motherShip.imageRect.right < -50:
        motherShip = ""
        if motherShipDirection == "Left":
            motherShipDirection = "Right"
        else:
            motherShipDirection = "Left"

def setupShields():
    list=[]
    list.append(Shield(86, 400))
    list.append(Shield(214, 400))
    list.append(Shield(342, 400))
    list.append(Shield(470, 400))
    return list

def drawShields():
    global shieldList
    
    for s in shieldList:
        if s.topLeftImage!="":
            screen.blit(s.topLeftImage,  s.topLeftImageRect)
        if s.topRightImage!="":
            screen.blit(s.topRightImage,  s.topRightImageRect)
        if s.bottomLeftImage!="":
            screen.blit(s.bottomLeftImage,   s.bottomLeftImageRect)
        if s.bottomRightImage !="":
            screen.blit(s.bottomRightImage,  s.bottomRightImageRect)
    
def drawExplosions():
    global explosionList
    
    for e in explosionList:
        screen.blit(e.image, e.imageRect)
                   
def playGame():
    global lastMotherShip
    global motherShip
    global motherShipDirection
    global score
    
    screen.fill(black)
    
    # Display some text
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    text = font.render("Score: "+str(score), 1, (0, 252, 0))
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    screen.blit(text, textpos)
    
    drawShields()
    
    if motherShip =="":
        if (time.time() - lastMotherShip) >= 25:
                if motherShipDirection == "Left":
                    
                    motherShip = MotherShip(810, 50)
                else:
                    motherShip = MotherShip(-30, 50)
                lastMotherShip = time.time()
    else:
        moveMotherShip()
        
    drawExplosions()
    moveAliens()
    
    size = len(alienBulletList)
    if size == 0:
        alienShoot()
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                quit()
            if event.key==pygame.K_UP:
                size = len(bulletList)
                if size == 0:
                    shootSound.play()
                    bulletList.append(Bullet(ship.getLocationX()+(ship.imageRect.width/2),  500, "./img/missile_player.png"))
            if event.key==pygame.K_LEFT:
                ship.changeDirection("left")
            if event.key==pygame.K_RIGHT:
                ship.changeDirection("right")
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                ship.changeDirection("stop")
    
    for b in bulletList:
        moveBullet(b)
    
    for ab in alienBulletList:
        moveAlientBullet(ab)
        
    checkForCollisions(bulletList,alienBulletList , ship)
            
    moveShip()
    
    pygame.display.flip()

#---------------------------------------------------------------------------Variables--------------------------------------------------------------------

# # set up music
pygame.mixer.init()
shootSound = pygame.mixer.Sound('./sounds/shoot.wav')
alienExplodeSound = pygame.mixer.Sound('./sounds/invaderkilled.wav')

musicPlaying = True



#set screen
size=width,  height,=600, 600
black=0, 0, 0
speed=[2, 0]

screen=pygame.display.set_mode(size)

#set players
ship = ""
bullet = ""
direction = "Right"
bulletList=[]
alienBulletList=[]
lastMoved = time.time()
lastDirection="Right"

lastMotherShip = time.time()
motherShipDirection = "Left"
motherShip=""

alienList = ""
explosionList=""

shieldList=setupShields()

score = 0
alienSpeed=1

gameMode ="MENU"
    
while 1:
    if gameMode=="MENU":
        screen.fill(black)
        image = pygame.image.load("./img/title.png")
        imageRect = image.get_rect()
        screen.blit(image, imageRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    quit()
                if event.key==pygame.K_UP:
                    #reset the game
                    alienSpeed=1
                    alienList = setupAliens()
                    shieldList = setupShields()
                    bulletList = []
                    explosionList=[]
                    mothership=""
                    ship =Ship(0,  500, "./img/player.png")
                    score = 0 
                    direction = "Right"
                    lastMoved = time.time()
                    lastDirection="Right"
                    lastMotherShip = time.time()
                    motherShipDirection = "Left"
                    gameMode="PLAYING"

    if gameMode=="PLAYING":
        playGame()
    
    if gameMode=="GAMEOVER":
        screen.fill(black)
        image = pygame.image.load("./img/gameover.png")
        imageRect = image.get_rect()
        screen.blit(image, imageRect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    quit()
                if event.key==pygame.K_UP:
                    gameMode="MENU"
        
    
  
