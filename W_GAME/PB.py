from T import *

def deadend(million, misfortune):
    
    lag(3)
    if not million:
        p("Since you didn't earn enough money to clear the game.....")
        lag(3)
        p("\nIT IS NOW PUNISHMENT TIME!!! YAY!!")
        if not misfortune:
            lag(2)
            p("\nYou are quite the MISFORTUNATE one HAHAHAHA")
        execution(1)
        
    elif million:

        p("JACKPOT!!!! You scored exactly 1000000$!!! \\($O$)/ \\(*O*)/")
        lag(2)
        p("\nCONGRATULATION!!! \\(^O^)/ YOU HAVE CLEAR....")
        lag(3)
        p("\n...CLEARLY FAILED THE GAME HAHAHAHAHAHA!! (X_^)")
        lag(3)
        p("\nSELFISH BASTARD... YOU'VE CONTACTED PLAYER2 DIDN'T YOU?")
        lag(2)
        p("\nLEAVING the MISFORTUNE one behind")
        lag(1)
        p("\nand trying to get away by yourself???")
        lag(3)
        p("\nNOT HAPPENING!! DIE! AHAHAHAHA \\(+_0)/")
        if not misfortune:
            lag(2)
            p("\nHoW mIsFoRtUnAtE YoU aRe (+_O)")
        execution(4)
    return 50

def multiend(million, win, misfortune, passed):
    
    lag(3)
    if not million:
        p("Man.... no one earned enough money to clear the game (=_=)")
        lag(2)
        p("\nGuess it is PUNISHMENT TIME!! YAY!! \\(^-^)/")
        if win:
            lag(2)
            p("\nHOWEVER, since you have higher balance")
            lag(2)
            p("\nYou get to watch player2's death before yours!!!")
            lag(2)
            p("\nENJOY YOUR VIEW HAHAHAHAHA")
            if not misfortune:
                lag(1)
                p("\nYOU ARE SO MISFORTUNATE!")
            execution(2)
        elif not win:
            p("Since you have lower balance... YOU ARE A BIG LOSER!! \\(^o^)/")
            lag(2)
            p("\nAND PLAYER2 GETS TO SEE YOU DIE!!")
            lag(2)
            p("\nHOW FUN!! HOW EXICITING!! HAHAHAHAHAHAHA!!!")
            if not misfortune:
                lag(1)
                p("\nYOU ARE SO MISFORTUNATE!")
            execution(3)
    elif million:
          p("JACKPOT!! One of you earned enough money to clear the game!!")
          if misfortune:
              if passed:
                  lag(2)
                  p("\nAnd both of you stay fortunate in great misfortune!(^0^)")
                  lag(3)
                  p("\nSuch tenacity.... MAKE US WANT TO BREAK YOU MORE!! \\(>_<)/")
                  lag(3)
                  p("\n*draw out weapons*(X_O)")
                  lag(2)
                  p("\nwhere do we start dis.em..b.er.ing..y.o..u..")
                  lag(2)
                  p("\n??.???..??..?")
                  p("wh.y...a.r.e...y.u..d..i.s.a...p..e..r...ng...")
                  lag(2)
                  p("\n..S.T...OP..TH.M...!!.!...%#$@#&^@&^#")
                  lag(1)
                  clear_screen()
                  return 100
              else:
                  lag(3)
                  p("\n...HOWEVER, ONE OF YOU IS NOT FORTUNATE ENOUGH!! \\(+0+)/")
                  lag(2)
                  p("\nIF ONE DIES, BOTH NEED TO DIE!! HAHAHAHAHA!! \\(>0<)/")
                  lag(2)
                  p("\nDIE! (X_O)")
                  execution(5)
                  
          elif not misfortune:
              
              lag(3)
              p("...HOWEVER, BOTH OF YOU ARE TOO FORTUNATE!! \\(+0+)/")
              lag(2)
              p("YOU NEED SOME MISFORTUNE!! HAHAHAHAHA!! \\(>0<)/")
              lag(2)
              p("DIE!")
              execution(5)
              
    return 50
          
def end_sequence(multiplayer, million, win, misfortune, passed):
          if not multiplayer:
              return deadend(million, misfortune)
          else:
              return multiend(million, win, misfortune, passed)

def execution(case):
    lag(2)
    clear_screen()
    p("*YoU wOkE uP In A DaRk RoOm*")
    lag(2)
    p("\n\n*yOu ArE tIeD tO a ChAiR*")
    lag(2)
    p("\n\n*WeIrD-LooKing MaScoTs ShOw Up WiTh tOOls*")
    lag(3)
    for i in range(2):
        p("")
        
    if case == 1:
        p("*VROOOOOOOOOOOOOM*")
        p("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
        lag(2)
        for i in range(2):
            p("")
        p("*YoUr LeGs ArE MiSsInG...*")
        lag(2)
        for i in range(2):
            p("")
        p("*BAM* *BAM* *BAM* *BAM* *BAM*")
        p("STOP!STOOOP!!AHHHHHHHHHHHHHHHHHHHHHHHHHH")
        for i in range(2):
            p("")
        lag(1)
        p("*YoUr ArMs ArE CrUsHeD AnD ToRn A p A r T*")
        lag(2)
        for i in range(2):
            p("")
        p("*SLASH*")
        lag(2)
        for i in range(2):
            p("")
        p("*YoU aRe LoSiNg CoNsCiOuSnEsS*")
        for i in range(3):
            lag(1)
            p(".")
        p("*someone picked up..yo.ur....hea.d*")
        for i in range(2):
            lag(1)
            p(".")
        p("*...e.ch..one..of.t.e..m.scots..a.re..pl.yi.g...*")
        for i in range(2):
            lag(1)
            p(".")
        p("*..w.th...o.e...o.f...y..ur..b.dy...p.rt....*")
        lag(3)
        p("\n*YOU ARE DEAD*\n")
        lag(2)
        p("REALLY should of say GOODBYE")
        lag(1)
        
    elif case == 2:

        p("*YoU SeE PlAyEr2 oN tHe ChAiR nExT tO yOu*")
        lag(3)
        p("\n\n*ThEy ApPrOaCh pLaYeR2*")
        lag(4)
        p("\n\nVROOOOOOOOOOOOOOOOOOOOM")
        lag(1)
        p("")
        p("STOP! STOOOPPP!!!! PLEASE!")
        lag(1)
        p("")
        p("VROOOOOOOOOOOOOOOOOMZIIIIZIIIIZIII")
        lag(1)
        p("")
        p("AHHHHHHHHHHHHHHHHHHHHHHHH!PLEASE STOP!!AHHHHHH!")
        lag(1)
        p("")
        p("BAM BAM BAM BAM BAM BAM BAM")
        lag(1)
        p("")
        p("AHH..PLE.ASE...ST.OP......AHHHHHHHHHHHHHHHHHHH")
        lag(1)
        p("")
        p("SLASH")
        lag(1)
        p("")
        p("*HeAd RollinG*........................")
        lag(3)
        p("\n\n*YoU'vE WaTcHeD PlAyEr2 gEtTiNg bRe Ak A p A r T*")
        lag(2)
        p("\n\n*FeAr AnD AnGeR OvErWhElM yOu*")
        lag(2)
        p("\n\n*EaCh OnE oF tHe MaScOtS iS hOldInG A bOdY PaRt*")
        lag(1)
        p("")
        p("*ArMs..LeGs...HeAd...ToRsO...ThEy ArE rEjOiCinG*")
        lag(4)
        p("\n\n*ThEY GoT BoReD wItH PlAyEr2s....tHeY aRe NoW LoOkInG aT yOu*")
        lag(2)
        p("\n\n*tHeY ArE aPpRoAcHiNg YoU....*")
        lag(4)
        p("\nVROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM")
        p("AHHHHHHHHHHHASDAHADGAFHHHHHHHHHHSDFHDF")
        p("BAM BAM BAM BAM BAM BAM BAM")
        p("AHHHHHHHHHHHAS!! STOP!! PLEAAAAAAAASSE")
        p("I BEG Y*SWOOSH*.......................")
        lag(4)
        p("\n*YOU ARE DEAD*\n")
        lag(1)
        p("REALLY should of say GOODBYE")
        lag(2)

    elif case == 3:
        
        p("*YoU SeE PlAyEr2 oN tHe ChAiR nExT tO yOu*")
        lag(1)
        p("")
        p("PlaYeR2 iS wAtChInG yOu")
        lag(2)
        p("")
        p("*ThEy ApPrOaCh YoU*")
        lag(4)
        p("\n\nVROOOOOOOOOOOOOOOOOOOOOOOOOOM")
        lag(1)
        p("")
        p("AHHHHH! STOOOPPP!!!! PLEASE!")
        p("")
        p("PlAyEr2 iS wAtChInG")
        lag(1)
        p("")
        p("VROOOOOOOOOOOOOOOOOMZIIIIZIIIIZIII")
        lag(1)
        p("")
        p("I BEG YOU!!!!PLEASE STOP!!AHHHHHH!")
        p("")
        p("PlAyEr2 iS wAtChInG")
        lag(1)
        p("")
        p("BAM BAM BAM BAM BAM BAM BAM")
        lag(1)
        p("")
        p("AHHH.ST..STOP...ST.OP......AHHHHH")
        p("")
        p("PlAyEr2 iS cRyInG")
        lag(1)
        p("")
        p("*SLASH*")
        lag(1)
        p("")
        p("*HeAd FlIeS oFf*.....")
        lag(1)
        p("")
        p("..Pl.A.yE.2..i.S..sT.i.l...w.A.t..h.I..n.G.......")
        lag(3)
        p("\n*YOU ARE DEAD*\n")
        lag(1)
        p("REALLY should of say GOODBYE")
        lag(2)

    elif case == 4:

        p("*You know what is coming*")
        lag(2)
        p("\n*You've realized your mistake*")
        lag(3)
        p("\n*Sigh*")
        lag(3)
        p("\nJust make it quic*SLASH*")
        lag(1)
        p("\n*Head off*")
        lag(1)
        p("\n*YOU ARE \"DEAD\"*\n")
        lag(3)

    elif case == 5:

        p("You look at Ayva")
        lag(3)
        p("\nAyva looks back at you")
        lag(3)
        p("\n\"Sorry... I failed again\"")
        lag(3)
        p("\n\"It's okay\"")
        lag(2)
        p("\n\"...I will definitely save yo*SLASH*")
        lag(2)
        p("\n*YOU ARE \"DEAD\"*\n")
        lag(3)
        
    clear_screen()
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
              
          
          

          
          
        


    
    
    
