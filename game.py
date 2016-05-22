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
gold = (250, 215, 0)
foolsgold = (197, 179, 88)
colours = (black, red, green, blue)
spec_colours = (foolsgold, gold)
personImg = pygame.image.load("woman.bmp")
gameDisplay = pygame.display.set_mode((disp_width,disp_height))

#rogue functions I don't want to change
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
    def __init__(self, object_startx = -500, object_starty = random.randrange(0, disp_height),colour = red, speed = 5):
        """Takes in Object start x, object star y, object speed"""
        #Could use indexing; could be less lazy
        self.colour = colour
        self.speed = speed
        block_magic = random.randrange(0,100)
        if block_magic == 50:
            self.colour = random.choice(spec_colours)
            if self.colour == gold:
                self.speed = 9
            if self.colour == foolsgold:
                self.speed = 8
    
        if self.colour == red:
            self.speed = 10
        if self.colour == blue:
            self.speed = 8
        if self.colour == green:
            self.speed = 3
        if self.colour == black:
            self.speed = 7
        self.x = object_startx
        self.y = object_starty
        self.width = 50
        self.height = 10
        
    def check_collide(self, y, score, Player):
        """Checks collision based on coords"""
        if self.x > Player.x and not self.x > Player.x + 30:
            if (self.y < y and self.y > y + 54) or (self.y + 10 > y and self.y + 10 < y + 54):
                self.damage(Player, score)

    def move(self):
        """Draws every tic, assumes that bullet will always move"""
        pygame.draw.rect(gameDisplay, self.colour, [self.x, self.y, self.width, self.height])
        self.x += self.speed

    def damage(self, Player, score):
        if self.colour == green:
            Player.health += 1
        if Player.invincibility == False:
            if self.colour == red:
                Player.health -= 30
            if self.colour == blue:
                Player.health -= 1
                if Player.speed >= 0.02:
                    Player.speed -= 0.02
            if self.colour == black:
                Player.health -= 10
                Player.speed += 0.05
            if self.colour == gold:
                Player.invincibility = True
            if self.colour == foolsgold:
                Player.speed = -Player.speed
            if Player.health < 0:
                crash(score)


            
                       
        

class Person(object):
    """Player object"""
    def __init__(self,x = disp_width-40,y=0):
        """creates player"""
        print "init"
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0
        self.speed = 5
        self.createPerson()
        self.health = 100
        self.invincibility = False
    def createPerson(self):
        gameDisplay.blit(personImg, (self.x,self.y))
    def move(self,score):
        gameDisplay.blit(personImg, (self.x,self.y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash(score)
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                print "kdown"
                if event.key == pygame.K_UP:
                    self.y_change = -self.speed
                if event.key == pygame.K_DOWN:
                    self.y_change = self.speed
                if event.key == pygame.K_LEFT:
                    self.x_change = -self.speed*0.75
                if event.key == pygame.K_RIGHT:
                    self.x_change = self.speed*0.75

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

        if self.y > disp_width or self.y < 0 or self.y > 550:
            self.y_change = 0
    
    def return_y(self):
        return self.y
    def return_x(self):
        return self.x
    def return_health(self):
        return self.health
    def take_damage(self):
        self.health -= 30
    def take_health(self):
        self.health += 5

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
            health = Player.return_health()
            if time.time() - orgTime >= 5:
                Player.invincibility = False
                orgTime == time.time()
            if Player.invincibility == True:
                print "invincible"
            print health
            Player.move(score)
            if score/60 == len(level):
                level += "dango",
                for i in range(len(level)):
                    kris_tup.append(Block(random.randrange(-1000, 0),random.randrange(0, disp_height), random.choice(colours)))
                    
                    
            for dango in kris_tup:
                if dango.x < disp_width:
                    dango.move()
                    dango.check_collide(y, score, Player)
            pygame.display.update() #Flip
            clocl.tick(60)
            score += 1
            


    


Game = Game(disp_width, disp_height)
