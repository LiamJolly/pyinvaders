import pygame

class Alien:
    startingX=""
    startingY=""
    alienType=0
    
    mode=0
    
    imageA=""
    imageARect=""
    imageB=""
    imageBRect=""
    
    image=""
    imageRect=""
    
    def __init__(self, startingX, startingY, alienType):
        #setup the two images for the alien
        if alienType==1:
            self.imageA=pygame.image.load("./img/alien1.png")
            self.imageARect = self.imageA.get_rect()
            self.imageARect = self.imageARect.move(startingX, startingY)
            self.imageB=pygame.image.load("./img/alien1-b.png")
            self.imageBRect= self.imageB.get_rect()
            self.imageBRect = self.imageBRect.move(startingX, startingY)
        if alienType==2:
            self.imageA=pygame.image.load("./img/alien2.png")
            self.imageARect = self.imageA.get_rect()
            self.imageARect = self.imageARect.move(startingX, startingY)
            self.imageB=pygame.image.load("./img/alien2-b.png")
            self.imageBRect= self.imageB.get_rect()       
            self.imageBRect = self.imageBRect.move(startingX, startingY)
        if alienType==3:
            self.imageA=pygame.image.load("./img/alien3.png")
            self.imageARect = self.imageA.get_rect()
            self.imageARect = self.imageARect.move(startingX, startingY)
            self.imageB=pygame.image.load("./img/alien3-b.png") 
            self.imageBRect= self.imageB.get_rect()     
            self.imageBRect = self.imageBRect.move(startingX, startingY)
   
        self.alienType = alienType
        #start with image a
        mode=0
        self.image = self.imageA
        self.imageRect = self.imageARect
     
        
    def getLocationX(self):
        return self.imageRect.left

    def getLocationY(self):
        return self.imageRect.bottom

    def getAlientType():
        return self.alienType
        
    def image():
        return self.image
        
    def imageRect():
        return self.imageRect
            
    def moveAlien(self, x, y):
        if self.mode==0:
            #move to where A was and where we are going to
            self.imageBRect.left = (self.imageARect.left+x)
            self.imageBRect.top = (self.imageARect.top+y)
            #assign to image
            self.image = self.imageB
            self.imageRect = self.imageBRect
            #flick mode
            self.mode=1
        else:
            #move to where B was and where we are going to
            self.imageARect.left = (self.imageBRect.left+x)
            self.imageARect.top = (self.imageBRect.top+y)
            #assign to image
            self.image = self.imageA
            self.imageRect = self.imageARect
            #flick mode
            self.mode=0
