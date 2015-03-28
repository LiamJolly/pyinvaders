import pygame

class AlienBullet:
    startingX=""
    startingY=""

    def __init__(self, startingX, startingY,  image):
        self.image = pygame.image.load(image)
        self.imageRect = self.image.get_rect()
        self.imageRect = self.imageRect.move(startingX, startingY)
        
    def getLocationX():
        return self.locationX

    def getLocationY():
        return self.locationY
        
    def image():
        return self.image
        
    def imageRect():
        return self.imageRect
        
    def move(self ):
        self.imageRect = self.imageRect.move(0,1)
