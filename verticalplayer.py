import pygame 
class player1:
    

    def __init__(self,x,y):
        self.image = pygame.image.load(f'car.png')
        self.image = pygame.transform.scale(self.image,(80,150))
        self.index = 0
        self.get_rect= self.image.get_rect(center=(x,y))
        self.rect = self.image.get_rect(center=(x,y))
        self.speed=3                                                       #movement by no. of spaces
        self.width= self.image.get_width()
        

    def update(self,moving_left,moving_right):

        if moving_left == True and self.rect.x>150 :
            self.rect.x -= self.speed
        if moving_right == True and self.rect.x + self.width < 435:
            self.rect.x += self.speed

        #self.counter += 1
        #if self.counter >= 2:
         #   self.index = (self.index +1)%(self.image)
          #  self.image = self.image(se)

    def draw(self, win):
        win.blit(self.image, self.rect)

    

    def get_recting(self,x,y):
        img= self.image
        return img.get_rect(center=(x,y))
