from T import *
import turtle

def winning_display():
    
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
    t = turtle.Pen() 
    turtle.bgcolor('black') 
    for x in range(153): 
        t.pencolor(colors[x%6]) 
        t.width(x/100 + 1) 
        t.forward(x) 
        t.left(59)
        
#==============================================================================
# SECRET QUEST (^_^):
# HAHAHA WHO SAID YOU CAN'T LOOK AT THE CODES?
# ADD THE SECRET MESSAGE: "NO GAME NO LIFE"
# TO YOUR PROOF OF COMPLETION FOR EXTRA REWARDS!
#==============================================================================


def destroyed():
    
    lag(2)
    p("\n....................")
    lag(2)
    p("\nHAHAHAHAHAHA WHAT ARE YOU SAYING??? \\(X_O)/")
    lag(2)
    p("\nTHERE IS NO WAY THAT WE ARE M..E.R.E...IM.G.IN.TIO.N.S....")
    lag(3)
    p("\n?????!!!!!!!!.!...!!...")
    lag(3)
    p("\n..W.AT..I.S...G.IN.G...O.N.??..??!.!.!.\\.(O_....).../....")
    lag(3)
    p("\n..W..Y...A.E....W.E..D.SA...P..EA..I..G...(>...._...<../...")
    lag(2)
    p("\n..w.AT..T.E...F..K..D.D...Y.U...D...O...(X_.....)....")
    lag(2)
    p("\n..ST..P..T.I..S...P..L..E..S.E....W.E...B.G...Y.OU...(X....X...)")
    lag(2)
    p("\n..N..O....O.OOO...O...$@%!$&!#&^@$^&^$&@(*^")
    lag(3)
    p("\n*THEY ARE GONE FOREVER*")
    lag(3)

def Congratulations():
    
    file = open("MISSION COMPLETED.txt", "w")
    file.write("This is your game master speaking\n")
    file.write("CONGRATULATIONS!\n")
    file.write("You've completed the challenge!\n")
    file.write("It was kinda tiring right?\n")
    file.write("You've done great\n\n")
    file.write("Anyways\n\n")
    file.write("Thank you very much for playing!\n")
    file.write("It's the first time I write something like this lol\n")
    file.write("I literally took my friend's assignment and transformed it :P\n")
    file.write("Full of plot holes and weird concepts right? XD\n")
    file.write("Thank you so much for bearing with it\n")
    file.write("Planning on creating a real, legit game with more people next time\n")
    file.write("Something big that covers the city (urbex? jk)\n\n")
    file.write("Now, the win condition:\n\n")
    file.write("Send a email to me in the following format:\n")
    file.write("title: Meshi kure\n")
    file.write("content: the colors that you saw in the last display\n")
    file.write("If you didn't see anything, then write the sentence you saw in the test file\n\n")
    file.write("Goodbye!")
    
    
def Grand_final():

    lag(5)
    p("*YoU WaKe Up In tHe DaRk RoOm*")
    lag(3)
    p("\n*ThE aIr StInKs oF bLoOd AnD rOtTeN MeAt*")
    lag(3)
    p("\n*ThE kIlLeRs sHoW uP wItH toOls*")
    lag(3)
    p("\nMUAHAHAHAHAHAHAHAHAHAHAHAHAHAHA! \\(X_O)/")
    lag(1)
    p("\nWELCOME BACK!!! \\(O_+)/")
    lag(1)
    p("\nI TOLD YOU!!! YOU WON'T GET AWAY FROM US!!! NEVER!! \\(>_<)/")
    lag(2)
    p("\nOUR NEW PLAYER2!! \\(^O^)/")
    lag(1)
    p("\nFROM NOW ON YOU WILL BE LOCKED UP\\(=_+)/")
    lag(1)
    p("\nAND WATCH PEOPLE DECIDE YOUR FATE \\(O_O)/")
    lag(1)
    p("\nTHEN GET CHOPPED INTO PIECES OVER AND OVER AGAIN!!!!!\\(^O^)/")
    lag(1)
    p("\nWHAT A FORTUNE!! WHAT A WONDER! ABSOLUTE UTOPIA!!! \\(X_O)/")
    lag(2)
    p("\nOH... LOOK AT THOSE EYES!! \\(>_<)/")
    lag(2)
    p("\nHOW FEROCIOUS!! FULL OF HATRED AND RAGE!!\\(O_<)/")
    lag(1)
    p("\nMAKE US WANT TO BREAK YOU EVEN MORE!\\(+_+)/")
    lag(1)
    p("\nMUHHAHAHAHAHAHAHHAHAHAHAHAHAHAHHAHAHAHHAHAHAHAHAHAHAHHAHAHAHAHAHAHA")
    p("\\(^o^)/\\(+_O)/\\(>_<)/\\(=_+)/\\(O_O)/\\(X_O)/\\(+_O)/")
    lag(3)
    p("\nSHHHHHUUUUUUUUUUUUT UPPPPPPPPPPPPPPPPPPPPPPPPPPPP!")
    lag(2)
    p("\n...........................................")
    p("........What's your problem? (X_O)")
    lag(3)
    p("\nI have a little something to tell you")
    lag(2)
    p("\n....What? (X_O)")
    lag(2)
    stop = False
    while not stop:
        terminate = input("\n*Inhale*: ")
        terminate = terminate.upper()
        if (terminate == "YOU ARE NOTHING BUT MY IMAGINATIONS"):
            destroyed()
            try:
                winning_display()
                turtle.bye()
            except:
                Congratulations()
            Congratulations()
            lag(2)
            stop = True
        else:
            lag(2)
            p("\n......")
            lag(2)
            p("\nDIE! \\(x_O)/")
            lag(2)
            p("\n*YOU GOT CHOPPED UP IN PIECES*")
            lag(2)
            stop = True

