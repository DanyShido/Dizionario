#pgzero
import random
WIDTH = 908 # Larghezza della finestra
HEIGHT = 589 # Altezza della finestra

TITLE = "BuisnessMountain" # Titolo del tuo progetto
FPS = 30 # Numero di frame per secondo
#oggetti
sfondo= Actor("background")
casa= Actor("house",(501,152))
forest1= Actor("forest",(758,281))
forest2= Actor("forest",(630,216))
forest3= Actor("forest",(711,371))
forest4= Actor("forest",(582,306))
mine= Actor("mine",(325,176))
grass1= Actor("grass",(453,240))
grass2= Actor("grass",(358,418))
river1= Actor("riverstart",(148,199))
river2= Actor("river",(277,264))
river3= Actor("river",(406,329))
river4= Actor("river",(535,394))
stone= Actor("stone",(229,353))
hill= Actor("hill",(102,288))
E1= Actor("E1",(501,232))
E2= Actor("E2",(325,260))
E3= Actor("E3",(150,290))
E4= Actor("E4",(630,293))
E8= Actor("E4",(758,355))
E9= Actor("E4",(582,380))
E11= Actor("E11",(229,440))
E12= Actor("E4",(715,447))
E14= Actor("E14",(358,508))
upcasa= Actor("upcasa")
upcaf= Actor("upcaf")
upsmelt= Actor("upsmelt")
up1= Actor("up",(726.5,90))
up2= Actor("up",(726.5,200))
up3= Actor("up",(726.5,90))
up4= Actor("SL",(726.5,90))
up5= Actor("SL",(726.5,400))
buy2= Actor("b",(726.5,220))
buy1= Actor("b",(726.5,110))
buy3= Actor("b",(726.5,110))
buy4= Actor("SB",(726.5,120))
buy5= Actor("SB",(726.5,420))
cross= Actor("cross",(565,22))
livmaxL= Actor("livmax",(726.5,90))
livmaxT= Actor("livmax",(726.5,200))
livmaxP= Actor("SLmax",(726.5,90))
livmaxA= Actor("SLmax",(726.5,400))
CAF= Actor("CAF",(148,199))
smelt= Actor("smelt",(358,418))
#d-cash
d_cash= Actor("d-cash",(880,15))
#picconi
pp= Actor("picconeS",(720,70))
pb= Actor("picconeB",(720,70))
po= Actor("picconeO",(720,70))
pf= Actor("picconeF",(720,70))
pa= Actor("picconeA",(720,70))
#asce
ap= Actor("asciaS",(720, 365))
ab= Actor("asciaB",(720, 365))
ao= Actor("asciaO",(720, 365))
af= Actor("asciaF",(720, 365))
aa= Actor("asciaA",(720, 365))
#variabili
mode= "game"
count= 100
#liv casa
livL= 0
#liv tempo
livT= 0
#liv casa fiume
liv= 0
#liv piccone
livP= 0
#liv ascia
livA= 0
#prezzo casa
cost1= 120
#prezzo casa fiume
cost2= 4000
#prezzo pick
cost3= 15000
#prezzo ascia
cost4= 15000
#prezzo tempo
tempo= 100
x= 30
y= 30
#per capire se il timer è attivo
cl = 0
#per attivarlo
ct= 0
def draw():
    if mode == "game":
        E11.draw()
        E1.draw()
        E2.draw()
        E4.draw()
        E8.draw()
        E9.draw()
        E12.draw()
        sfondo.draw()
        casa.draw()
        forest2.draw()
        forest1.draw()
        mine.draw()
        grass1.draw()
        forest4.draw()
        forest3.draw()
        river1.draw()
        river2.draw()
        river3.draw()
        river4.draw()
        hill.draw()
        stone.draw()
        grass2.draw()
        d_cash.draw()
        screen.draw.text(count, center=(820, 15), color = 'black', fontsize = 30)
        screen.draw.text(x, center=(150, 15), color = 'black', fontsize = 25)
        screen.draw.text("Time left:", center=(75, 15), color = 'black', fontsize = 25)
        if livL >= 3:
            E3.draw()
            mine.draw()
            grass1.draw()
            forest4.draw()
            forest3.draw()
            CAF.draw()
            river2.draw()
            river3.draw()
            river4.draw()
            hill.draw()
            stone.draw()
            grass2.draw()
            if liv >= 4:
                E14.draw()
                smelt.draw()
        elif livT == 25:
            livmaxT.draw()
    elif mode == "casa":
        upcasa.draw()
        up1.draw()
        buy1.draw()
        up2.draw()
        buy2.draw()
        cross.draw()
        #per bonus1
        screen.draw.text(cost1, center=(725, 110), color = 'black', fontsize = 15)
        screen.draw.text("Camera da letto", center=(712, 70), color = 'black', fontsize = 15)
        screen.draw.text("liv.", center=(795, 70), color = 'black', fontsize = 20)
        screen.draw.text(livL, center=(822, 70), color = 'black', fontsize = 20)
        #soldi
        screen.draw.text(count, center=(735, 15), color = 'black', fontsize = 30)
        #per bonus tempo
        screen.draw.text(tempo, center=(725, 220), color = 'black', fontsize = 15)
        screen.draw.text("-1s di tempo", center=(712, 180), color = 'black', fontsize = 15)
        screen.draw.text("liv.", center=(795, 180), color = 'black', fontsize = 20)
        screen.draw.text(livT, center=(822, 180), color = 'black', fontsize = 20)
        #time left
        screen.draw.text(x, center=(774, 550), color = 'black', fontsize = 25)
        screen.draw.text("Time left:", center=(699, 550), color = 'black', fontsize = 25)
        if livL == 10:
            livmaxL.draw()
        if livT == 25:
            livmaxT.draw()
        if cl == 1:
            up2.draw()
            screen.draw.text("Upgrade", center=(726.5,185), color = 'black', fontsize = 25)
            screen.draw.text(x, center=(726.5,220), color = 'black', fontsize = 25)
    elif mode == "caf":
        upcaf.draw()
        up3.draw()
        buy3.draw()
        up2.draw()
        buy2.draw()
        cross.draw()
        #per bonus 1 caf
        screen.draw.text(cost2, center=(725, 110), color = 'black', fontsize = 15)
        screen.draw.text("Casa sul fiume", center=(712, 70), color = 'black', fontsize = 15)
        screen.draw.text("liv.", center=(795, 70), color = 'black', fontsize = 20)
        screen.draw.text(liv, center=(822, 70), color = 'black', fontsize = 20)
        #soldi
        screen.draw.text(count, center=(735, 15), color = 'black', fontsize = 30)
        #per bonus tempo
        screen.draw.text(tempo, center=(725, 220), color = 'black', fontsize = 15)
        screen.draw.text("-1s di tempo", center=(712, 180), color = 'black', fontsize = 15)
        screen.draw.text("liv.", center=(795, 180), color = 'black', fontsize = 20)
        screen.draw.text(livT, center=(822, 180), color = 'black', fontsize = 20)
        #time left
        screen.draw.text(x, center=(774, 550), color = 'black', fontsize = 25)
        screen.draw.text("Time left:", center=(699, 550), color = 'black', fontsize = 25)
        if livT == 25:
            livmaxT.draw()
        if cl == 1:
            up2.draw()
            screen.draw.text("Upgrade", center=(726.5,185), color = 'black', fontsize = 25)
            screen.draw.text(x, center=(726.5,220), color = 'black', fontsize = 25)
        if liv == 10:
            livmaxL.draw()
    elif mode == "smelt":
        upsmelt.draw()
        up4.draw()
        pp.draw()
        buy4.draw()
        up5.draw()
        buy5.draw()
        cross.draw()
        ap.draw()
        #per piccone
        screen.draw.text(cost3, center=(725, 120), color = 'black', fontsize = 15)
        screen.draw.text("Piccone", center=(720, 20), color = 'black', fontsize = 15)
        screen.draw.text("liv.", center=(795, 30), color = 'black', fontsize = 20)
        screen.draw.text(livP, center=(822, 30), color = 'black', fontsize = 20)
        #per ascia
        screen.draw.text(cost4, center=(725, 420), color = 'black', fontsize = 15)
        screen.draw.text("Ascia", center=(720, 330), color = 'black', fontsize = 15)
        screen.draw.text("liv.", center=(795, 340), color = 'black', fontsize = 20)
        screen.draw.text(livA, center=(822, 340), color = 'black', fontsize = 20)
        #soldi
        screen.draw.text(count, center=(735, 250), color = 'black', fontsize = 30)
        #time left
        screen.draw.text(x, center=(774, 550), color = 'black', fontsize = 25)
        screen.draw.text("Time left:", center=(699, 550), color = 'black', fontsize = 25)
        if livP == 4:
            livmaxP.draw()
        if livA == 4:
            livmaxA.draw()

def for_bonus_1():
    global count
    global livL
    count += 30
    if livL == 1:
        count += 400
    elif livL == 2:
        count += 500
    elif livL == 3:
        count += 600
    elif livL == 4:
        count += 800
    elif livL == 5:
        count += 1000
    elif livL == 6:
        count += 1400
    elif livL == 7:
        count += 2000
    elif livL == 8:
        count += 2800
    elif livL == 9:
        count += 4000
    elif livL == 10:
        count += 6000
#def bonus caf
def for_bonus_2():
    global count
    global liv
    count += 2500
    if liv == 1:
        count += 2000
    elif liv == 2:
        count += 2800
    elif liv == 3:
        count += 3500
    elif liv == 4:
        count += 7000
    elif liv == 5:
        count += 12000
    elif liv == 6:
        count += 14000
    elif liv == 7:
        count += 20000
    elif liv == 8:
        count += 30000
    elif liv == 9:
        count += 40000
    elif liv == 10:
        count += 60000

#def time
def time():
    global x
    global y
    global cl
    global ct
    global liv
    if x == 30:
        ct += 1
        schedule_interval(time,1)
    if ct == 1:
        x -= 1
    if x == 0:
        schedule_unique(for_bonus_1, 1)
        x += y
        unschedule(time)
        if cl == 1:
            cl -= 1
        if liv >= 1:
            schedule_unique(for_bonus_2, 1)
    if x == y and cl == 0:
        #per tempo
        schedule_interval(time, 1)

#def pick
def for_pick():
    if livP == 1:
        pp.image = "picconeB"
    elif livP == 2:
        pp.image = "picconeO"
    elif livP == 3:
        pp.image = "picconeF"
    elif livP == 4:
        pp.image = "picconeA"
#def axe
def for_axe():
    if livA == 1:
        ap.image = "asciaB"
    elif livA == 2:
        ap.image = "asciaO"
    elif livA == 3:
        ap.image = "asciaF"
    elif livA == 4:
        ap.image = "asciaA"

def on_mouse_down(button,pos):
    global x
    global y
    global livL
    global livT
    global liv
    global livP
    global livA
    global cost1
    global cost2
    global cost3
    global cost4
    global mode
    global count
    global tempo
    global cl
    #cambio modalità
    if E1.collidepoint(pos):
        mode = "casa"
    elif cross.collidepoint(pos):
        mode = "game"
    elif E3.collidepoint(pos) and livL >= 3:
        mode = "caf"
    elif E14.collidepoint(pos) and liv >= 4:
        mode = "smelt"
    #buy casa
    elif buy1.collidepoint(pos) and mode == "casa":
        buy1.y = 115
        #animazione
        animate(buy1, tween= "bounce_end", duration= 0.5, y=110)
        if count >= cost1:
            count -= cost1
            cost1 *= 2
            livL += 1
    #buy tempo
    elif buy2.collidepoint(pos) and cl == 0:
        buy2.y = 225
        #animazione
        animate(buy2, tween= "bounce_end", duration= 0.5, y=220)
        if count >= tempo and cl == 0:
            count -= tempo
            tempo *= 2
            livT += 1
            y -= 1
            cl += 1
            if x == 30:
                schedule_unique(time, 1)
    if buy3.collidepoint(pos) and mode == "caf":
        buy3.y = 115
        #animazione
        animate(buy3, tween= "bounce_end", duration= 0.5, y=110)
        if count >= cost2:
            count -= cost2
            cost2 *= 2
            liv += 1
    #buy pick
    elif buy4.collidepoint(pos) and mode == "smelt" and livP <= 4:
        buy4.y = 125
        #animazione
        animate(buy4, tween= "bounce_end", duration= 0.5, y=120)
        if count >= cost3:
            schedule_interval(for_pick,1)
            count -= cost3
            cost3 *= 2
            livP += 1
    #buy axe
    elif buy5.collidepoint(pos)and mode == "smelt" and livA <= 4:
        buy5.y= 425
        #animazione
        animate(buy5, tween= "bounce_end", duration= 0.5, y=420)
        if count >= cost4:
            schedule_interval(for_axe,1)
            count -= cost4
            cost4 *= 2
            livA += 1
