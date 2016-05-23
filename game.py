import pygame,time,random
from Tkinter import *
#Kenneth Koepcke, Parth Triviality
#Final Project
#Dodge the bullets
#Things could potentially do:
##Tkinter menu
##CPickle scores
##idk
#ANYTHING WITH INVINCIBILITY DOES NOT WORK AT ALL

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
heartImg = pygame.image.load("heart.jpg")
gameDisplay = pygame.display.set_mode((disp_width,disp_height))


#rogue functions I don't want to change
def crash(score):
    text = "Time: "
    text += str(score/60) + "s"
    crash_message_display(text)
    pygame.quit()
    quit()
#Dont ask, I can't tell...
def crash_message_display(text):
    display_text = pygame.font.Font("freesansbold.ttf", 50)
    textSurf, textRect = text_object(text, display_text)
    textRect.center = ((disp_width/2),(disp_height/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()
    time.sleep(3)

def message_display(text):
    display_text = pygame.font.Font("freesansbold.ttf", 50)
    textSurf, textRect = text_object(text, display_text)
    textRect.center = ((disp_width/2),(disp_height/2))
    gameDisplay.blit(textSurf, textRect)

        
def text_object(text, font):
    textSurface = font.render(text, True, blue)
    return textSurface, textSurface.get_rect()
#Something I might end up finishing
class Application(Frame):
    def __init__(self, master):
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.f_label = Label(self, text = "Super Slime Soccer Settings").grid(row = 0, column = 1, sticky = W)

class Block(object):
    """Block class, creates bullets. Has defaulted aspects"""
    def __init__(self, object_startx = -500, object_starty = random.randrange(0, disp_height),colour = red, speed = 5, hard = False):
        """Takes in Object start x, object star y, object speed"""
        #Could use indexing; could be less lazy
        self.hard = hard
        if self.hard == False:
            self.colour = colour
            self.speed = speed
            block_magic = random.randrange(0,1000)
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
        else:
            self.colour = red
            self.speed = 9
        self.x = object_startx
        self.y = object_starty
        self.width = 50
        self.height = 10
        
    def check_collide(self, y, score, Player):
        """Checks collision based on coords"""
        if (self.x > Player.x + 10 and self.x < Player.x + 40) or (self.x + 50 > Player.x + 10 and self.x + 50 < Player.x + 40):
            if (self.y < Player.y + 54 and self.y > Player.y) or (self.y + 10 > Player.y and self.y + 10 < Player.y + 54):
                self.damage(Player, score)

    def move(self):
        """Draws every tic, assumes that bullet will always move"""
        pygame.draw.rect(gameDisplay, self.colour, [self.x, self.y, self.width, self.height])
        self.x += self.speed

    def damage(self, Player, score):
        if self.colour == green:
            Player.health += 1
            Player.speed = 5
        if Player.invincibility == False:
            if self.colour == red:
                Player.health -= 30
            if self.colour == blue:
                Player.health -= 1
                if Player.speed >= 0.02:
                    Player.speed -= 0.5
            if self.colour == black:
                Player.health -= 10
                Player.speed += 1
            if self.colour == gold:
                #Doesn't work lol
                Player.invincibility = True
                Player.health += disp_height
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
    def toggleInvincibility(self):
        #LOTTA LOGIC, NOT MANY RESULTS
        if self.invincibility == False:
            self.invicibility = True
        else:
            self.invincibility = False
    def check_invinc(self):
        if self.invincibility == True:
            return True
        else:
            return False
            
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
    #I think some of these I use interchangably...
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
    def health_bar(self):
        if self.health > disp_height:
            health_color = gold
        else:
            health_color = green
        pygame.draw.rect(gameDisplay, health_color, [disp_width-10,0, 10, self.health/10])


class Game(object):
    def __init__(self, disp_width, disp_height):
        #Initialize Window
        hard = False
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
                message_display("Welcome to the program!")
            if score > 60 and score < 200:
                message_display("Now die!")
##            if score > 1200 and score < 1400:
##                message_display("You're not dead yet..?")
##            if score > 1400 and score < 1800:
##                message_display("RNG must really love you! <3 <3")
##            if score > 1800 and score < 3000:
##                gameDisplay.blit(heartImg, (0,0))
##                message_display("I think... I... Love you...")
##            if score > 3000 and score < 4000:
##                message_display("LOL, jk. die. :3")
##                hard = True
##            if score > 4000 and score < 4200:
##                message_display("Cheater")
##            if score > 4200:
##                Player.x = disp_height/2
##                Player.y = disp_width/2

            y = Player.return_y()
            Player.health_bar()
            health = Player.return_health()
            if time.time() - orgTime >= 5:
                Player.invincibility = False
                orgTime == time.time()
            invinc = Player.check_invinc()
            if Player.invincibility == True:
                print "invincible"
            print health
            Player.move(score)
            if score/60 == len(level):
                level += "dango",
                for i in range(len(level)):
                    kris_tup.append(Block(random.randrange(-1000, 0),random.randrange(0, disp_height), random.choice(colours), 5,hard))
                    
                    
            for dango in kris_tup:
                if dango.x < disp_width:
                    dango.move()
                    if invinc == False:
                        dango.check_collide(y, score, Player)
                    else:
                        pass
            pygame.display.update() #Flip
            clocl.tick(60)
            score += 1

Game = Game(disp_width, disp_height)
