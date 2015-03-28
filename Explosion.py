import pygame

class Explosion:
    startingX=""
    startingY=""

    def __init__(self, startingX, startingY):
        self.image = pygame.image.load("./img/explosion.png")
        self.imageRect = self.image.get_rect()
        self.imageRect = self.imageRect.move(startingX, startingY)
        
    def getLocationX(self):
        return self.imageRect.left

    def getLocationY(self):
        return self.imageRect.top
        
    def image():
        return self.image
        
    def imageRect():
        return self.imageRect
    
    
