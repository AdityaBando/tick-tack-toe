# variables:
matrix=[['a','b','c'],['d','e','f'],['g','h','i']]
turn="0"
#used functions:

def ingame(): #NT
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
        
def output_game(): #not working / REJECTED/ OLD VERSION
    for i in range(0,3):
        for j in range(0,3):
            print "|%s|"%matrix[i][j]
def output_gamev1(): #DONE 
    print "your game baby!"    
    for i in range(0,3):
        print "%s|%s|%s"%(matrix[i][0],matrix[i][1],matrix[i][2])

def game_brain(): #NT
    print "control given to game brain"
    if matrix[0][0]==matrix[1][1]==matrix[2][2]:
        print "You WIN! You're our new champion!!!"
        exit(0)
    elif matrix[0][2]==matrix[1][1]==matrix[2][0]:
        print "You WIN! I Thought You were fool, but you're Genius!"
        exit(0)
    elif matrix[0][0]==matrix[0][1]==matrix[0][2]:
        print "You WIN! I Thought You were fool, but you're Genius!"
        exit(0)
    elif matrix[1][0]==matrix[1][1]==matrix[1][2]:
        print "You WIN! I Thought You were fool, but you're Genius!"
        exit(0)
    elif matrix[2][0]==matrix[2][1]==matrix[2][2]:
        print "You WIN! I Thought You were fool, but you're Genius!"
        exit(0)
    elif matrix[0][0]==matrix[1][0]==matrix[2][0]:
        print "You WIN! I Thought You were fool, but you're Genius!"
        exit(0)
    elif matrix[0][1]==matrix[1][1]==matrix[2][1]:
        print "You WIN! I Thought You were fool, but you're Genius!"
        exit(0)
    elif matrix[0][2]==matrix[1][2]==matrix[2][2]:
        print "You WIN! I Thought You were fool, but you're Genius!"
        exit(0)
    else:
        print "Your Turn Dude!"
        output_gamev1()
        turn='X' #problem here <--- UNABLE TO UPDATE TURN!!!
        ingame()

        
#STARTS HERE:
   
a=raw_input("Enter Your name:")
b=raw_input("Your Opponent's name:")
print "Here we Go!"
turn="O"
output_gamev1()
ingame()
    
        
        
