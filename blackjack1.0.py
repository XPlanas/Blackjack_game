'''blackjack'''
import random
cartas = [1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10,1,2,3,4,5,6,7,8,9,10,10,10,10]
cart_cpu = list
tu_cart = list
game_on = True
def show(s):
    match s:
        case 1:
            print("tus cartas: ",tu_cart," = ",sum(tu_cart) )
            print("cartas del crupier: ""[",cart_cpu[0],", ?]") 
        case 2:
            print("tus cartas: ",tu_cart," = ",sum(tu_cart) )
            print("cartas del crupier: ",cart_cpu," = ",sum(cart_cpu) )     
def hit(p):
    match p:
     case 1:
       print("pides")
       tu_cart.append(cartas[random.randint(0,51)])
     case 2:
       print("el crupier pide")
       cart_cpu.append(cartas[random.randint(0,51)])
def compara():
 show(2)
 if sum(tu_cart)<sum(cart_cpu):
    print("pierdes")
 elif sum(tu_cart)>sum(cart_cpu):
    print("ganas")
 elif sum(tu_cart)==sum(cart_cpu):
    print("empate")
 return(False)
    
def over(p):
 match p:
      case 1:
       if sum(tu_cart) >21:
           print("te has pasado, pierdes")
           return(False)
       else:
           return(True)
      case 2:
        if sum(cart_cpu) >21:
            print("el crupier se ha pasado, ganas")
            return(False)
        else:
           return(True)
def ace(p):
    match p:
      case 1:
       if tu_cart.__contains__(1) and sum(tu_cart)<=21:
           tu_cart.insert
           return(False)
      case 2:
        if sum(cart_cpu) >21:
            print("el crupier se ha pasado, ganas")
            return(False)
print("""
 /$$$$$$$  /$$        /$$$$$$   /$$$$$$  /$$   /$$    /$$$$$  /$$$$$$   /$$$$$$  /$$   /$$
| $$__  $$| $$       /$$__  $$ /$$__  $$| $$  /$$/   |__  $$ /$$__  $$ /$$__  $$| $$  /$$/
| $$  \ $$| $$      | $$  \ $$| $$  \__/| $$ /$$/       | $$| $$  \ $$| $$  \__/| $$ /$$/ 
| $$$$$$$ | $$      | $$$$$$$$| $$      | $$$$$/        | $$| $$$$$$$$| $$      | $$$$$/  
| $$__  $$| $$      | $$__  $$| $$      | $$  $$   /$$  | $$| $$__  $$| $$      | $$  $$  
| $$  \ $$| $$      | $$  | $$| $$    $$| $$\  $$ | $$  | $$| $$  | $$| $$    $$| $$\  $$ 
| $$$$$$$/| $$$$$$$$| $$  | $$|  $$$$$$/| $$ \  $$|  $$$$$$/| $$  | $$|  $$$$$$/| $$ \  $$
|_______/ |________/|__/  |__/ \______/ |__/  \__/ \______/ |__/  |__/ \______/ |__/  \__/
                                                                                          
                                                                                          
                      PULSA ENTER PARA EMPEZAR                                                                                 
""")
 
if input()==int or str or float:
    tu_cart=[cartas[random.randint(0,51)],cartas[random.randint(0,51)]]
    cart_cpu=[cartas[random.randint(0,51)],cartas[random.randint(0,51)]]
    show(1)
    while game_on == True:
        move= int(input ("""
            1. STAND
            2. HIT
            """))
        
        match move:
        
         case 1: 
            show(2)
            print("te plantas")
            if sum(cart_cpu)>=17 :
                game_on = compara() 
            else:
             while sum(cart_cpu) <17:
              hit(2)
              show(2)
              game_on =over(2)
              if sum(cart_cpu)>=17:
                  game_on=compara()
         case 2:
            hit(1)
            show(1)
            game_on =over(1)