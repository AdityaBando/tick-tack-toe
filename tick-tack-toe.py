# tick-tack-toe project in python
# variables:
matrix=[['a','b','c'],['d','e','f'],['g','h','i']]
turn="0"
p1="NA"
p2="NA"
#used functions:

def ingame(): #get input from user and update matrix
    location=raw_input("Enter location\n>")
    if location=='a' and matrix[0][0]=="a":
        matrix[0][0]=turn 
        game_brain()
        
    elif location=='b' and matrix[0][1]=="b":
        matrix[0][1]=turn
        game_brain()
    elif location=='c' and matrix[0][2]=="c":
        matrix[0][2]=turn
        game_brain()
    elif location=='d' and matrix[1][0]=="d":
        matrix[1][0]=turn
        game_brain()
    elif location=='e' and matrix[1][1]=="e":
        matrix[1][1]=turn
        game_brain()
    elif location=='f' and matrix[1][2]=="f":
        matrix[1][2]=turn
        game_brain()
    elif location=='g' and matrix[2][0]=="g":
        matrix[2][0]=turn
        game_brain()
    elif location=='h' and matrix[2][1]=="h":
        matrix[2][1]=turn
        game_brain()
    elif location=='i' and matrix[2][2]=="i":
        matrix[2][2]=turn
        game_brain()
    else :
        print "Learn to type from a to i."
        
        
def output_gamev1(): 
    print "your turn baby!"    
    for i in range(0,3):
        print "%s|%s|%s"%(matrix[i][0],matrix[i][1],matrix[i][2])

def game_brain(): 
    print "control given to game brain"
    if matrix[0][0]==matrix[1][1]==matrix[2][2]:
        print "You WIN! You're our new champion!!!"
        exit(0)
    elif matrix[0][2]==matrix[1][1]==matrix[2][0]:
        print "You WIN! Congrats!"
        exit(0)
    elif matrix[0][0]==matrix[0][1]==matrix[0][2]:
        print "You WIN! Congrats!!"
        exit(0)
    elif matrix[1][0]==matrix[1][1]==matrix[1][2]:
        print "You WIN! You are the best!"
        exit(0)
    elif matrix[2][0]==matrix[2][1]==matrix[2][2]:
        print "You WIN! You're Genius!"
        exit(0)
    elif matrix[0][0]==matrix[1][0]==matrix[2][0]:
        print "You WIN! I mean how can this happen?"
        exit(0)
    elif matrix[0][1]==matrix[1][1]==matrix[2][1]:
        print "You WIN! The game was thrilling!"
        exit(0)
    elif matrix[0][2]==matrix[1][2]==matrix[2][2]:
        print "You WIN! WE HAVE FOUND OUR NEW CHAMPION!"
        exit(0)
    else:
        #this segment will check if game is draw by checking if all
        #the 9 "spaces are filled"
        count=0
        for i in range(0,3):
            for j in range(0,3):
                if matrix[i][j]=="O" or matrix[i][j]=="X":
                    count+=1
                    if count==9:
                        print "The game is draw!!!"
                        exit(0)
        
        #for next turn
        print "Your Turn Dude!"
        global turn #so that global variable changes
        print "turn: %s"%turn_p()
        output_gamev1()
        if turn=="X": 
            turn="O"
        else :
            turn="X"
        ingame()

def turn_p():
    #player's turn
    global turn,p1,p2
    if turn=="O":
        return "%s (%s)"%(p1,turn)
    elif turn=="X":
        return "%s (%s)"%(p2,turn)
    else:
        return "ERROR:NO_NAME_FOUND"

        
#STARTS HERE:
def start():
    while True:
        print "\t***TICK TACK TOE***"
        select=raw_input("1. START A NEW GAME / CONTINUE \n2. PRESS ANY OTHER KEY TO QUIT\n>>")
        global p1,p2
        if select=="1":
            p1=raw_input("Enter Your name:")
            p2=raw_input("Your Opponent's name:")
            print "Here we Go!"
            global turn
            turn="O"
            output_gamev1()
            ingame()
        else :
            exit(0)
    
        
start()   

    
        
        
