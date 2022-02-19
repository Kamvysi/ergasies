import random, time

game=[ [ [0 ,0, 0],[0 ,0 ,0],[0 ,0 ,0],],
       [ [0 ,0 ,0],[0 ,0 ,0],[0 ,0 ,0],],
       [ [0 ,0 ,0],[0 ,0 ,0],[0 ,0 ,0],],
        ]
#game=[ [ [1 ,3, 0],[0 ,1 ,0],[0 ,0 ,2],],
#       [ [0 ,0 ,0],[0 ,2 ,0],[0 ,3,0],],
#       [ [0 ,0 ,0],[0 ,0 ,0],[0 ,3 ,0],], 
#       ]
     


NoCircles=[9,9,9]

player=[ 1 , 2 , 3]

W=False
loops=0
while W==False  :

  value = random.choice(player)
  

  ran1=random.randrange(3)
  ran2=random.randrange(3)
 # ran3=random.randrange(3)



  print(value)
  print(ran1,ran2)
  k=0
  if  (game[ran1][ran2][0]==0) and((game[ran1][ran2][1] != value) and (game[ran1][ran2][2] !=value) ):
    game[ran1][ran2][0]=value
    k=1
    if value==1:
         NoCircles[0]=NoCircles[0]-1
         print(NoCircles)
    elif value==2:
         NoCircles[1]=NoCircles[1]-1
         print(NoCircles)
    elif value==3:
        NoCircles[2]=NoCircles[2]-1
        print(NoCircles)

    
   
        


    print(game[ran1][ran2][0])
    print(game[ran1][ran2][1])
    print(game[ran1][ran2][2])


  elif (game[ran1][ran2][1]==0)  and ((game[ran1][ran2][0] != value) and (game[ran1][ran2][2] !=value) ):
      game[ran1][ran2][1]=value
      k=1
      if value==1:
         NoCircles[0]=NoCircles[0]-1
         print(NoCircles)
      elif value==2:
         NoCircles[1]=NoCircles[1]-1
         print(NoCircles)
      elif value==3:
        NoCircles[2]=NoCircles[2]-1
        print(NoCircles)

      print(game[ran1][ran2][0])
      print(game[ran1][ran2][1])
      print(game[ran1][ran2][2])


  elif (game[ran1][ran2][2]==0) and ((game[ran1][ran2][0] != value) and (game[ran1][ran2][1] !=value) ):
      game[ran1][ran2][2]=value
      k=1
      if value==1:
         NoCircles[0]=NoCircles[0]-1
         print(NoCircles)
      elif value==2:
         NoCircles[1]=NoCircles[1]-1
         print(NoCircles)
      elif value==3:
        NoCircles[2]=NoCircles[2]-1
        print(NoCircles)

      print(game[ran1][ran2][0])
      print(game[ran1][ran2][1])
      print(game[ran1][ran2][2])
  else:
      print('den vrika thesh')


  if k==1:
      x=y=z=g=0 
     
 #katheta
      for i in range (0,3):
        for j in range (0,3):
       
           if  game[ran1][i][j]== value:
             x=x+1
           if x==3:
             W=True
          
 #orizodia
      for k in range (0,3):
        for l in range (0,3):

           if game[k][ran2][l]==value:
            y=y+1
           if y==3:
             W=True

 #diagonia(1)
      if ran1==ran2==0 or ran1==ran2==1 or ran1==ran2==2:
           for i in range (0,3):
               if game[0][0][i]== value:  
                   z=z+1
                   for i in range (0,3):
                       if game[1][1][i]== value :
                          z=z+1
           
                          for i in range (0,3):
                             if game[2][2][i]== value:
                                z=z+1

                                if z==3:
                                  W=True


 #diagonia(2)
      if (ran1==0 and ran2==2) or ran1==ran2==1 or (ran1==2 and ran2==0):
             for i in range (0,3):
               if game[0][2][i]== value:  
                   g=g+1
                   for i in range (0,3):
                       if game[1][1][i]== value :
                          g=g+1

                          for i in range (0,3):
                             if game[2][0][i]== value:
                                g=g+1

                                if g==3:
                                  W=True


 #mikro pros megalo(apo panw prws ta katw)
      

     

 


  loops=loops+1


  
 

  for row in game:
     print(row)

     

  time.sleep(0.5)

print(loops)




 






