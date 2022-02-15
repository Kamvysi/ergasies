import random

xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]

k=0
p1=0
p2=0
draw=0
while k<101:
  for i in xarti:
     for j in color:
         xartia.append([i,j])
  random.shuffle(xartia)
 
  
  player1=[]
  sum1=0
  f1=0
  f2=0
  while sum1<16:
     sum1=0
     
     if f1==0:
       for i in xartia:
         if(str(i[0]) in ['K','Q','J','10'] ):
           player1.append(xartia.pop(xartia.index(i)))
           break
       f1=1
     else:
       player1.append(xartia.pop())
     # print (player1)
     for card in player1:
        if card[0] in figures:
            sum1=sum1+10
        else:
            sum1=sum1+card[0]
     print(sum1)
  if sum1>21:
    print("P2 wins!")
  else:
    print("P2 joins the game") #let me add one more player
    player2=[]
    sum2=0
    while sum2<16:
        sum2=0
        if f2==0:
          for i in xartia:
            if(str(i[0]) not in ['K','Q','J','10'] ):
              player2.append(xartia.pop(xartia.index(i)))
              break
          f2=1
        else:
          player2.append(xartia.pop())
        # print (player2)
        for card in player2:
            if card[0] in figures:
                sum2=sum2+10
            else:
                sum2=sum2+card[0]
        print(sum2)
    if sum2>21:
        sum2=0
    if sum1>sum2:
        print("P1 wins!")
        
        p1=p1+1
    elif sum2>sum1:
        print("P2 wins!")
        
        p2=p2+1
    else:
        print("draw!")
       
        draw=draw+1
    
    
        
  k=k+1


if p1 !=0: 
 print ("player 1 won ",p1, "times") 

if p2!= 0:
  print("player 2 won ",p2,"times" )

if draw!= 0:
    print("it was a draw",draw,"times")
   