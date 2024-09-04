import pgzrun
import random
HEIGHT = 600
WIDTH = 1200
TITLE = 'Collect the paper bag'
items = []
animateditems = []
safelist = []
level = 1
score = 0
newlevel = False
gamesuccessful = False
gamefail = False
def draw():
    screen.clear()
    screen.blit('background',(0,0))
    for i in items:
        i.draw()
    if gamefail == True:
        screen.clear()
        screen.draw.text('Game Over\nYou scored: '+str(score),(400,100),fontsize= 100,color = 'orange')
       
    if gamesuccessful == True:
        screen.clear()
        screen.draw.text('You Win!\nYou scored: '+str(score),(400,100),fontsize= 100,color = 'orange')
        

        


def createactor(alist):#This function is the actual list that turns everything into actors
    actorlist =[]
    for i in alist:
        y = Actor(i)
        actorlist.append(y)
    return actorlist
#This callfunction function will call the function that will create actors for the images that we have selected for the game.m=level 
#This is the function that will take all of the funcitons and make them work together to create thelist, so then we don't have to bother with the confusion when writing it in the update function. 
def callfunction(aninteger):
    thelist = createactor(getimageslist(level))
    layout(thelist)
    animateitems(thelist)
    return thelist


def getimageslist(anumber):#this will creat the list of the images before they are actors, so that the items that fall are random besides for the paper bag. 
    thelist = ['paperbag']

    for i in range(anumber):
        additem  = random.choice(['battery','bottle','chips','plasticbag'])
        thelist.append(additem)
    random.shuffle(thelist)

    return thelist 


def update():#This is where we call all of our functions into action. The layout function will repostition the items logically so that
    #It shows perfect symmetry between all of them.

    global items
    
    if len(items) == 0:
        items = callfunction(level)#The items list is the final list, and it will become tehe result of the other call function, which is thelist. 
        for i in items:
            print(i.image)

    

#def layout():
def layout(alist):
    space = 1200/(len(alist)+1)#<-- The error here was that I made an order of operations mistake. How did I manage that?
    gaps = 1
    for i in alist:
        
        i.pos = space*gaps,0
        gaps = gaps+1
        print(i.pos)

def animateitems(lists):
    global animateditems
    for i in lists:
        duration = 11-level
        i.anchor = ('center','bottom')
        animateditem = animate(i,duration=duration,y=600,on_finished = gamefailed)
        animateditems.append(animateditem)


def nextlevel():
    global level,items,animateditems,newlevel,score
    if level == 4:
        gamecomplete()
        score = 4
    else:
        items,animateditems = [],[]
        level = level+1
        score = score+1

def on_mouse_down(pos):
    for i in items:
        if i.collidepoint(pos):
            if i.image =='paperbag':
                
                nextlevel()
            else:
                gamefailed()


def freezescreen(alist):
    for i in alist:
        if i.running:
            i.stop()



def gamefailed():
    global gamefail,score
    freezescreen(animateditems)
    gamefail = True

def outoftime():
    global gamefail,score
    gamefail = True


def gamecomplete():
    global gamesuccessful
    freezescreen(animateditems)
    gamesuccessful = True







#Layout function: 
#if you have n number of items, you will have n+1 number of gaps
#len(items)+1
#Has to have perfect symmetry
#1200/len(items)+1
#for i in items:
    #screen.blit(i,1200)
#This math is wrong

#i.pos = 1200/len(items)+1,0


pgzrun.go()