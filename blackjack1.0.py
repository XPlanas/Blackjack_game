import random
cartas = [1,2,3,4,5,6,7,8,9,10,10,10,10,
          1,2,3,4,5,6,7,8,9,10,10,10,10,
          1,2,3,4,5,6,7,8,9,10,10,10,10,
          1,2,3,4,5,6,7,8,9,10,10,10,10]
mazo = ["A ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ","Q ","K ",
        "A ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ","Q ","K ",
        "A ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ","Q ","K ",
        "A ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 ","10","J ","Q ","K "] 
simbol = ['♠', '♠', '♠', '♠', '♠', '♠', '♠', '♠', '♠', '♠', '♠', '♠', '♠',
          '♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦', '♦',
          '♥', '♥', '♥', '♥', '♥', '♥', '♥', '♥', '♥', '♥', '♥', '♥', '♥',
          '♣', '♣', '♣', '♣', '♣', '♣', '♣', '♣', '♣', '♣', '♣', '♣', '♣'] 
fichas=1000
cart_cpu = list
cart_cpum = list
cart_cpus = list
tu_cart = list
tu_cartm= list
tu_carts= list
tu_cart_split = list
tu_cartm_split= list
tu_carts_split= list
game_on = True
def tucart(n,nc):
    match nc:
       case 2 :
           print(f"""
                ┌─────────┐         ┌─────────┐
                │{tu_cartm[n]}       │         │{tu_cartm[n+1]}       │
                │         │         │         │
                │         │         │         │
                │    {tu_carts[n]}    │         │    {tu_carts[n+1]}    │
                │         │         │         │
                │         │         │         │
                │       {tu_cartm[n]}│         │       {tu_cartm[n+1]}│
                └─────────┘         └─────────┘""") 
       case 1:
            print (f"""
                ┌─────────┐        
                │{tu_cartm[n]}       │  
                │         │         
                │         │         
                │    {tu_carts[n]}    │    
                │         │         
                │         │        
                │       {tu_cartm[n]}│        
                └─────────┘         """)
def tucartsplit(n,nc):
    match nc:
       case 2 :
           print(f"""
                ┌─────────┐         ┌─────────┐
                │{tu_cartm_split[n]}       │         │{tu_cartm_split[n+1]}       │
                │         │         │         │
                │         │         │         │
                │    {tu_carts_split[n]}    │         │    {tu_carts_split[n+1]}    │
                │         │         │         │
                │         │         │         │
                │       {tu_cartm_split[n]}│         │       {tu_cartm_split[n+1]}│
                └─────────┘         └─────────┘""") 
       case 1:
            print (f"""
                ┌─────────┐        
                │{tu_cartm_split[n]}       │  
                │         │         
                │         │         
                │    {tu_carts_split[n]}    │    
                │         │         
                │         │        
                │       {tu_cartm_split[n]}│        
                └─────────┘         """)
def cpucart(n,nc):
    match nc:
       case 2 :
           print(f"""
                ┌─────────┐         ┌─────────┐
                │{cart_cpum[n]}       │         │{cart_cpum[n+1]}       │
                │         │         │         │
                │         │         │         │
                │    {cart_cpus[n]}    │         │    {cart_cpus[n+1]}    │
                │         │         │         │
                │         │         │         │
                │       {cart_cpum[n]}│         │       {cart_cpum[n+1]}│
                └─────────┘         └─────────┘""") 
       case 1:
            print (f"""
                ┌─────────┐        
                │{cart_cpum[n]}       │  
                │         │         
                │         │         
                │    {cart_cpus[n]}    │    
                │         │         
                │         │        
                │       {cart_cpum[n]}│        
                └─────────┘         """)           
def show(s):
       match s:
        case 1:
            print("tus cartas: ",tu_cart," = ",sum(tu_cart) )
            tucart(0,2)
            if len(tu_cart)==3:
                tucart(2,1)
            if len(tu_cart)>3:
                tucart(2,2)
            if len(tu_cart)==5:
                tucart(4,1)   
            if len(tu_cart)>5:
                tucart(4,2)
            if len(tu_cart)==7:
                tucart(6,1)
            if len(tu_cart)==8:
                tucart(6,2)
            print("cartas del crupier: ""[",cart_cpu[0],", ?]") 
            print( f"""
                ┌─────────┐         ┌─────────┐
                │{mazo[ri3]}       │         │░░░░░░░░░│
                │         │         │░░░░░░░░░│
                │         │         │░░░░░░░░░│
                │    {simbol[ri3]}    │         │░░░░░░░░░│
                │         │         │░░░░░░░░░│
                │         │         │░░░░░░░░░│
                │      {mazo[ri3]} │         │░░░░░░░░░│
                └─────────┘         └─────────┘""")
            if len(cart_cpu)==3:
                cpucart(2,1)
            if len(cart_cpu)==4:
                cpucart(2,2)
            if len(cart_cpu)==5:
                cpucart(2,2)
                cpucart(4,1)
            if len(cart_cpu)==6:
                cpucart(2,2)
                cpucart(4,2)
        case 2:
            print("tus cartas: ",tu_cart," = ",sum(tu_cart) )
            tucart(0,2)
            if len(tu_cart)==3:
                tucart(2,1)
            if len(tu_cart)==4:
                tucart(2,2)
            if len(tu_cart)==5:
                tucart(2,2)
                tucart(4,1)
            if len(tu_cart)==6:
                tucart(2,2)
                tucart(4,2) 
            print("cartas del crupier: ",cart_cpu," = ",sum(cart_cpu)) 
            cpucart(0,2)
            if len(cart_cpu)==3:
                cpucart(2,1)
            if len(cart_cpu)==4:
                cpucart(2,2)
            if len(cart_cpu)==5:
                cpucart(2,2)
                cpucart(4,1)
            if len(cart_cpu)==6:
                cpucart(2,2)
                cpucart(4,2)
def split():
            print("tu mazo 1: ",tu_cart," = ",sum(tu_cart) )
            tucart(0,2)
            if len(tu_cart)==3:
                tucart(2,1)
            if len(tu_cart)>3:
                tucart(2,2)
            if len(tu_cart)==5:
                tucart(4,1)   
            if len(tu_cart)>5:
                tucart(4,2)
            if len(tu_cart)==7:
                tucart(6,1)
            if len(tu_cart)==8:
                tucart(6,2)
def doble():
    print("doblas")
    tu_cart.append(cartas[r1])
    tu_cartm.append(mazo[r1])
    tu_carts.append(simbol[r1])
def hit(p):
    match p:
     case 1:
        print("pides")
        tu_cart.append(cartas[r1])
        tu_cartm.append(mazo[r1])
        tu_carts.append(simbol[r1])
       
     case 2:
       print("el crupier pide")
       cart_cpu.append(cartas[r2])
       cart_cpum.append(mazo[r2])
       cart_cpus.append(simbol[r2])
def compara():
 if sum(tu_cart)<sum(cart_cpu):
    print("pierdes")
    return(False,0)
 elif sum(tu_cart)>sum(cart_cpu):
    print("ganas")
    return(False,1)
 elif sum(tu_cart)==sum(cart_cpu):
    print("empate")
    return(False,2)
 return(False)
def over(p):
 match p:
      case 1:
       if sum(tu_cart) >21:
           print("te has pasado, pierdes")
           return(False,0)
       else:
           return(True,0)
      case 2:
        if sum(cart_cpu) >21:
            print("el crupier se ha pasado, ganas")
            cash(1)
            return(False,1)
        else:
           return(True,0)
def ace(p):
    match p:
      case 1:
       if tu_cart.__contains__(1) and sum(tu_cart)<=21:
           tu_cart.insert(tu_cart.index(1),11)
           tu_cart.remove(1) 
           if sum(tu_cart)>21:
             tu_cart.insert(tu_cart.index(11),1)
             tu_cart.remove(11)  
       elif tu_cart.__contains__(11) and sum(tu_cart)>21:
          tu_cart.insert(tu_cart.index(11),1)
          tu_cart.remove(11)
      case 2:
        if cart_cpu.__contains__(1) and sum(cart_cpu)<=21:
           cart_cpu.insert(cart_cpu.index(1),11)
           cart_cpu.remove(1)
           if sum(cart_cpu)>21:
             cart_cpu.insert(cart_cpu.index(11),1)
             cart_cpu.remove(11)   
        elif cart_cpu.__contains__(11) and sum(cart_cpu)>21:
           cart_cpu.insert(cart_cpu.index(11),1)
           cart_cpu.remove(11)
def bjack(p):
    match p:
     case 1:
         if tu_cart.__contains__(11) and tu_cart.__contains__(10):
            return(True)
         else:
            return(False)
     case 2:
        if cart_cpu.__contains__(11) and cart_cpu.__contains__(10):
            return(True)
        else:
            return(False)
def cash(x):
    match x:
        case 0:
            print(f"has recuperado tus fichas")
            return(apuesta)
        case 1:
            print(f"has ganado {apuesta}fichas")
            return(apuesta*2)
        case 2:
            print(f"has ganado {apuesta*1.5}fichas")
            return(apuesta*2.5)
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
  apuesta= int(input(f"""
Tus fichas:{fichas}
Tu apuesta:"""))
  fichas-=apuesta
  ri1 =random.randint(0,51)
  ri2 =random.randint(0,51)
  ri3 =random.randint(0,51)
  ri4 =random.randint(0,51)  
  tu_cart=[cartas[ri1],cartas[ri2]]
  tu_cartm=[mazo[ri1],mazo[ri2]]
  tu_carts=[simbol[ri1],simbol[ri2]]
  #tu_cart=[10,10] #para pruebas
  ace(1)
  cart_cpu=[cartas[ri3],cartas[ri4]]
  cart_cpum=[mazo[ri3],mazo[ri3]]
  cart_cpus=[simbol[ri3],simbol[ri3]]
  ace(2)
  show(1)
  while True:
    while game_on == True:
        print(f"Tus fichas:{fichas}")
        if bjack(1)==True and bjack(2)==False:
            print("tienes BLACKJACK!, ganas")
            fichas+=cash(2)
            game_on = False
        if bjack(2)==True and bjack(1)==False:
            print("el crupier tiene BLACKJACK, pierdes")  
            game_on = False
        if bjack(2)==True and bjack(1)==True:
            print("ambos teneis BLACKJACK, Empate")  
            fichas+=cash(0)
            game_on = False
        if game_on == True:
            print("""
            1. STAND
            2. HIT""")
            if fichas>=apuesta:
             print("""            3. DOUBLE""")
            if tu_cart[0]==tu_cart[1]:
             print("""            4. SPLIT""")
            move= int(input())  
        else:
            move=0
        match move:
         case 1: 
            show(2)
            print("te plantas")
            r2=random.randint(0,51)
            if sum(cart_cpu)>=17 :
                state=compara()
                wstate=state[1]
                gstate=state[0]
                if wstate==1:
                    fichas+=cash(1)
                game_on =gstate
            else:
             while sum(cart_cpu) <17:
              hit(2)
              ace(2)
              show(2)
              state=over(2)
              wstate=state[1]
              gstate=state[0]
              if wstate==1:
                fichas+=cash(1)
              game_on =gstate
              if 21>=sum(cart_cpu)>=17:
                 state=compara()
                 wstate=state[1]
                 gstate=state[0]
                 if wstate==1:
                    fichas+=cash(1)
                 game_on =gstate
         case 2:
            r1=random.randint(0,51)
            hit(1)
            ace(1)
            show(1)
            state=over(1)
            wstate=state[1]
            gstate=state[0]
            if wstate==1:
                fichas+=cash(1)
            game_on =gstate
         case 3:
           if fichas>=apuesta:
             r1=random.randint(0,51)
             doble()
             ace(1)
             show(2)
             fichas-=apuesta
             apuesta=2*apuesta
             print("te plantas")
             r2=random.randint(0,51)
             if sum(cart_cpu)>=17 :
                 state=compara()
                 wstate=state[1]
                 gstate=state[0]
                 if wstate==1:
                    fichas+=cash(1)
                 game_on =gstate
             else:
              while sum(cart_cpu) <17:
               hit(2)
               ace(2)
               show(2)
               state=over(2)
               wstate=state[1]
               gstate=state[0]
               if wstate==1:
                fichas+=cash(1)
               game_on =gstate
               if 21>=sum(cart_cpu)>=17:
                  game_on=compara()
           else:
               print("no")
         case 4:
             if tu_cart[0]==tu_cart[1]:
                 rs1=random.randint[0,51]
                 rs2=random.randint[0,51]
                 tu_cart=(tu_cart[0],cartas[rs1])
                 tu_cart_split=[tu_cart[1],cartas[rs2]]
                 tu_cartm_split=[tu_cart[1],mazo[rs2]]
                 tu_carts_split=[tu_cart[1],simbol[rs2]]
                 print("Separas tu mazo")
                 
             else:
                 print("no")
         case 0:
             game_on = False
    print(f"Tus fichas:{fichas}")
    if fichas==0:
        print("te has quedado sin fichas, eres pobre :(")
        break
    print("""play again?:
    any key = yes
          N = no""")
    i=input()
    if i ==("n") or i==("N"):
      print("gracias por jugar")
      break   
    elif i == str or int:
      print("New Game")
      apuesta= int(input(f"""
        Tus fichas:{fichas}
        Tu apuesta:"""))
      if apuesta>fichas:
        print("no tienes suficientes fichas")   
      else:  
        fichas-=apuesta
        ri1 =random.randint(0,51)
        ri2 =random.randint(0,51)
        ri3 =random.randint(0,51)
        ri4 =random.randint(0,51) 
        tu_cart=[cartas[ri1],cartas[ri2]]
        tu_cartm=[mazo[ri1],mazo[ri2]]
        tu_carts=[simbol[ri1],simbol[ri2]]
        ace(1)
        cart_cpu=[cartas[ri3],cartas[ri4]]
        cart_cpum=[mazo[ri3],mazo[ri3]]
        cart_cpus=[simbol[ri3],simbol[ri3]]      
        ace(2)
        show(1)
        game_on = True 
