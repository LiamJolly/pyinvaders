import pygame

class Shield:

    def __init__(self, startingX, startingY):
        
        self.startingX=startingX
        self.startingY=startingY
        
        self.shieldPieceWidth=21
        self.shieldPieceHeight=16

        self.topLeftHits = 0
        self.topLeftImage=pygame.image.load("./img/Shields/TopLeft/1.png")
        self.topLeftImageRect = self.topLeftImage.get_rect()
        self.topLeftImageRect = self.topLeftImageRect.move(self.startingX, self.startingY)
        
        self.bottomLeftHits = 0
        self.bottomLeftImage=pygame.image.load("./img/Shields/BottomLeft/1.png")
        self.bottomLeftImageRect = self.bottomLeftImage.get_rect()
        self.bottomLeftImageRect = self.bottomLeftImageRect.move(self.startingX, self.startingY+self.shieldPieceHeight)
        
        self.topRightHits=0
        self.topRightImage=pygame.image.load("./img/Shields/TopRight/1.png")
        self.topRightImageRect = self.topRightImage.get_rect()
        self.topRightImageRect = self.topRightImageRect.move(self.startingX+self.shieldPieceWidth, self.startingY)
        
        self.bottomRightHits=0
        self.bottomRightImage=pygame.image.load("./img/Shields/BottomRight/1.png")
        self.bottomRightImageRect = self.bottomRightImage.get_rect()
        self.bottomRightImageRect = self.bottomRightImageRect.move(self.startingX+self.shieldPieceWidth,  self.startingY+self.shieldPieceHeight)        
        
    def checkForCollision(self,  rect):
        hit=0
        if self.topLeftImageRect !="":
            if self.topLeftImageRect.colliderect(rect):
                self.topLeftHits=self.topLeftHits+1
                hit=1
                self.damageTopLeft()
        if self.bottomLeftImageRect !="":
            if self.bottomLeftImageRect.colliderect(rect):
                self.bottomLeftHits=self.bottomLeftHits+1
                hit=1
                self.damageBottomLeft()
        if self.topRightImageRect !="":       
            if self.topRightImageRect.colliderect(rect):
                self.topRightHits=self.topRightHits+1
                hit=1
                self.damageTopRight()
        if self.bottomRightImageRect !="":   
            if self.bottomRightImageRect.colliderect(rect):
                self.bottomRightHits=self.bottomRightHits+1
                hit=1
                self.damageBottomRight()
        return hit
            
    def damageTopLeft(self):
        if self.topLeftHits==4:
            self.topLeftImage=""
            self.topLeftImage=pygame.image.load("./img/Shields/TopLeft/2.png")
            self.topLeftImageRect = self.topLeftImage.get_rect()
            self.topLeftImageRect = self.topLeftImageRect.move(self.startingX, self.startingY)
        if self.topLeftHits==8:
            self.topLeftImage=""
            self.topLeftImage=pygame.image.load("./img/Shields/TopLeft/3.png")
            self.topLeftImageRect = self.topLeftImage.get_rect()
            self.topLeftImageRect = self.topLeftImageRect.move(self.startingX, self.startingY)
        if self.topLeftHits==12:
            self.topLeftImage=""
            self.topLeftImageRect=""
    
    def damageTopRight(self):
        if self.topRightHits==4:
            self.topRightImage=""
            self.topRightImage=pygame.image.load("./img/Shields/TopRight/2.png")
            self.topRightImageRect = self.topRightImage.get_rect()
            self.topRightImageRect = self.topRightImageRect.move(self.startingX+self.shieldPieceWidth, self.startingY)
        if self.topRightHits==8:
            self.topRightImage=""
            self.topRightImage=pygame.image.load("./img/Shields/TopRight/3.png")
            self.topRightImageRect = self.topRightImage.get_rect()
            self.topRightImageRect = self.topRightImageRect.move(self.startingX+self.shieldPieceWidth, self.startingY)
        if self.topRightHits==12:
            self.topRightImage=""
            self.topRightImageRect=""
            
    def damageBottomRight(self):
        if self.bottomRightHits==4:
            self.bottomRightImage=""
            self.bottomRightImage=pygame.image.load("./img/Shields/BottomRight/2.png")
            self.bottomRightImageRect = self.bottomRightImage.get_rect()
            self.bottomRightImageRect = self.bottomRightImageRect.move(self.startingX+self.shieldPieceWidth,  self.startingY+self.shieldPieceHeight)        
        if self.bottomRightHits==8:
            self.bottomRightImage=""
            self.bottomRightImage=pygame.image.load("./img/Shields/BottomRight/3.png")
            self.bottomRightImageRect = self.bottomRightImage.get_rect()
            self.bottomRightImageRect = self.bottomRightImageRect.move(self.startingX+self.shieldPieceWidth,  self.startingY+self.shieldPieceHeight)        
        if self.bottomRightHits==12:
            self.bottomRightImage=""
            self.bottomRightImageRect=""
            
    def damageBottomLeft(self):
        if self.bottomLeftHits==4:
            self.bottomLeftImage=""
            self.bottomLeftImage=pygame.image.load("./img/Shields/BottomLeft/2.png")
            self.bottomLeftImageRect = self.bottomLeftImage.get_rect()
            self.bottomLeftImageRect = self.bottomLeftImageRect.move(self.startingX, self.startingY+self.shieldPieceHeight)
        if self.bottomLeftHits==8:
            self.bottomLeftImage=""
            self.bottomLeftImage=pygame.image.load("./img/Shields/BottomLeft/3.png")
            self.bottomLeftImageRect = self.bottomLeftImage.get_rect()
            self.bottomLeftImageRect = self.bottomLeftImageRect.move(self.startingX, self.startingY+self.shieldPieceHeight)
        if self.bottomLeftHits==12:
            self.bottomLeftImage=""
            self.bottomLeftImageRect=""
    
    def getLocationX(self):
        return self.imageRect.left

    def getLocationY(self):
        return self.imageRect.top
        
    def changeDirection(self,  direction):
        if  direction=="left":
            self.movement = -1
        if direction == "right":
            self.movement = 1
        if direction == "stop":
            self.movement = 0
            
    def move(self):
        if (self.movement == 1 and self.imageRect.right < 800) or (self.movement == -1 and self.imageRect.left > 0):
            self.imageRect= self.imageRect.move(self.movement, 0) 
        
    def image():
        return self.image
        
    def imageRect():
        return self.imageRect
    
    
