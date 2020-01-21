import random
a=random.randint(0,11)
i=0
while i<3:
  b=int(input("enter a number to check :"))
  if a==b:
    print("congratulations,you have guessed it correctly")
    break
  else:
    print("wrong")
    i+=1  
if i>2:
  print("game over,the correct number is:",a)