import pygame
import random
pygame.init()
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rock.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 400
        self.image = pygame.transform.scale(self.image, (30, 30))

    def update(self):
        self.rect.x += 1
        self.rect.y += 1
class Paper(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("paper.png")
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 100
        self.image = pygame.transform.scale(self.image, (30, 30))
    def update(self):
        self.rect.x += 1
        self.rect.y += 1
class Scissor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("scissor.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        #resize the image
        self.image = pygame.transform.scale(self.image, (30, 30))
    def update(self):
        self.rect.x += 1
        self.rect.y += 1
#create 10 scissors
scissor_list = []
for i in range(10):
    scissor_list.append(Scissor())
#create 10 rock
rock_list = []
for i in range(10):
    rock_list.append(Rock())
#create 10 paper
paper_list = []
for i in range(10):
    paper_list.append(Paper())


scissor = pygame.sprite.Group()
scissor.add(scissor_list)
rock = pygame.sprite.Group()
rock.add(rock_list)
paper = pygame.sprite.Group()
paper.add(paper_list)

screen = pygame.display.set_mode((500, 500))
while True:
    pygame.time.delay(300)
    screen.fill((255, 255, 255))
    #move all scissors randomly
    for scissor in scissor_list:
        # scissor.rect.x += random.randint(-10, 50)
        #subscarat or add randomly
        if random.randint(0, 1) == 0:
            scissor.rect.x += random.randint(-5, 40)
            scissor.rect.y += random.randint(-5, 40)
        else:
            scissor.rect.x -= random.randint(-5, 40)
            scissor.rect.y -= random.randint(-5, 40)
    for rock in rock_list:
        # scissor.rect.x += random.randint(-10, 50)
        #subscarat or add randomly
        if random.randint(0, 1) == 0:
            rock.rect.x += random.randint(-5, 40)
            rock.rect.y += random.randint(-5, 40)
        else:
            rock.rect.x -= random.randint(-5, 40)
            rock.rect.y -= random.randint(-5, 40)
    for paper in paper_list:
        # scissor.rect.x += random.randint(-10, 50)
        #subscarat or add randomly
        if random.randint(0, 1) == 0:
            paper.rect.x += random.randint(-5, 40)
            paper.rect.y += random.randint(-5, 40)
        else:
            paper.rect.x -= random.randint(-5, 40)
            paper.rect.y -= random.randint(-5, 40)
    #keep all scissors on the screen
    for scissor in scissor_list:
        if scissor.rect.x < 0:
            scissor.rect.x = 0
        if scissor.rect.x > 500:
            scissor.rect.x = 500
        if scissor.rect.y < 0:
            scissor.rect.y = 0
        if scissor.rect.y > 500:
            scissor.rect.y = 500
    for scissor in rock_list:
        if scissor.rect.x < 0:
            scissor.rect.x = 0
        if scissor.rect.x > 500:
            scissor.rect.x = 500
        if scissor.rect.y < 0:
            scissor.rect.y = 0
        if scissor.rect.y > 500:
            scissor.rect.y = 500
    for scissor in paper_list:
        if scissor.rect.x < 0:
            scissor.rect.x = 0
        if scissor.rect.x > 500:
            scissor.rect.x = 500
        if scissor.rect.y < 0:
            scissor.rect.y = 0
        if scissor.rect.y > 500:
            scissor.rect.y = 500
    #draw all scissors
    for scissor in scissor_list:
        screen.blit(scissor.image, scissor.rect)
    for rock in rock_list:
        screen.blit(rock.image, rock.rect)
    for paper in paper_list:
        screen.blit(paper.image, paper.rect)
    #detect collision between rock and scissor and change the scissor to rock
    for scissor in scissor_list:
        for rock in rock_list:
            if scissor.rect.colliderect(rock.rect):
                scissor.image = rock.image
                scissor.rect = rock.rect

    pygame.display.update()
