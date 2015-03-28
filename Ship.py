import pygame

class Ship:
    startingX=""
    startingY=""
    movement=0

    def __init__(self, startingX, startingY,  image):
        self.image = pygame.image.load(image)
        self.imageRect = self.image.get_rect()
        self.imageRect = self.imageRect.move(startingX, startingY)
        
    def getLocationX(self):
        return self.imageRect.left

    def getLocationY(self):
        return self.imageRect.top
        
    def changeDirection(self,  direction):
        if  direction=="left":
            self.movement = -2
        if direction == "right":
            self.movement = 2
        if direction == "stop":
            self.movement = 0
            
    def move(self):
        if (self.movement == 2 and self.imageRect.right < 600) or (self.movement == -2 and self.imageRect.left > 0):
            self.imageRect= self.imageRect.move(self.movement, 0) 
        
    def image():
        return self.image
        
    def imageRect():
        return self.imageRect
    
    
