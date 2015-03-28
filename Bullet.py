import pygame

class Bullet:
    startingX=""
    startingY=""

    def __init__(self, startingX, startingY,  image):
        self.image = pygame.image.load(image)
        self.imageRect = self.image.get_rect()
        self.imageRect = self.imageRect.move(startingX, startingY)
        
    def getLocationX():
        return self.imageRect.left

    def getLocationY():
        return self.imageRect.top
        
    def image():
        return self.image
        
    def imageRect():
        return self.imageRect
        
    def move(self ):
        self.imageRect = self.imageRect.move(0, -2)
