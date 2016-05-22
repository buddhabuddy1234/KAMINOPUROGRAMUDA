import pygame,time,random
#Kenneth Koepcke, Parth Triviality
#Final Project
#Dodge the bullets

disp_width = 800
disp_height = 600
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
colours = (black, red, green, blue)
personImg = pygame.image.load("woman.bmp")
gameDisplay = pygame.display.set_mode((disp_width,disp_height))

def crash(score):
    text = "Time: "
    text += str(score/60) + "s"
    message_display(text)
    pygame.quit()
    quit()

def message_display(text):
    display_text = pygame.font.Font("freesansbold.ttf", 100)
    textSurf, textRect = text_object(text, display_text)
    textRect.center = ((disp_width/2),(disp_height/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(3)

        
def text_object(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()

class Block(object):
    """Block class, creates bullets. Has defaulted aspects"""
    def __init__(self, object_startx = -500, object_starty = random.randrange(0, disp_height),colour = red, object_speed = 5):
        """Takes in Object start x, object star y, object speed"""

        self.x = object_startx
        self.y = object_starty
        self.speed = object_speed
        self.width = 50
        self.height = 10
        self.colour = colour        
    def check_collide(self, y, score):
        """Checks collision based on coords"""
        if self.x > disp_width - 90 and not self.x > disp_width:
            if (self.y < y and self.y > y + 54) or (self.y + 10 > y and self.y + 10 < y + 54):
                crash(score)

    def move(self):
        """Draws every tic, assumes that bullet will always move"""
        pygame.draw.rect(gameDisplay, self.colour, [self.x, self.y, self.width, self.height])
        self.x += self.speed


class Person(object):
    """Player object"""
    def __init__(self,x = disp_width-40,y=0):
        """creates player"""
        print "init"
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.createPerson()
    def createPerson(self):
        gameDisplay.blit(personImg, (self.x,self.y))
    def move(self):
        gameDisplay.blit(personImg, (self.x,self.y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                print "kdown"
                if event.key == pygame.K_UP:
                    self.y_change = -5
                elif event.key == pygame.K_DOWN:
                    self.y_change = 5

            if event.type == pygame.KEYUP:
                print "kup"
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    self.y_change = 0

        self.x += self.x_change

        if self.x > disp_width or self.x < 15 or self.x > 765:
            self.x_change = 0
        self.y += self.y_change

        if self.y > disp_width or self.y < 0 or self.y > 510:
            self.y_change = 0
    def return_y(self):
        return self.y

class Game(object):
    def __init__(self, disp_width, disp_height):
        #Initialize Window
        pygame.init()
        self.disp_width = disp_width
        self.disp_height = disp_height
        myfont = pygame.font.SysFont("monospace", 16)
        pygame.display.set_caption("Super Slime Soccer")
        #colors
        #Don't understand
        clocl = pygame.time.Clock()
        clock2 = pygame.time.Clock()
        #etc

        score = 0
        x_change = 0
        y_change = 0
        #wom 30, 54
        #rekt 50, 10
        level = ()
        kris_tup = []
        orgTime = time.time()
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            if score < 60:
                Player = Person()
            y = Player.return_y()
            Player.move()
            if score/60 == len(level):
                level += "dango",
                for i in range(len(level)):
                    colour = random.choice(colours)
                    if colour == red:
                        speed = 9
                    if colour == blue:
                        speed = 2
                    if colour == green:
                        speed = 3
                    if colour == black:
                        7
                    
                    kris_tup.append(Block(random.randrange(-1000, 0),random.randrange(0, disp_height), colour, speed))
                    
                    
            for dango in kris_tup:
                if dango.x < disp_width:
                    dango.move()
                    dango.check_collide(y, score)
            pygame.display.update() #Flip
            clocl.tick(60)
            score += 1
            


    


Game = Game(disp_width, disp_height)
