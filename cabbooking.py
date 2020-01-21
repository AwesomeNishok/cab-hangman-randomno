a=input("enter s to continue")
i1=0
i2=0
i3=0
i4=0
while a!="q":
  print("select car type")
  print("1.mini,2.macro,3.share,4.prime")
  ct=int(input())
  if ct==1:
    while i1<3:
     print("mini is available")
     s1=int(input("enter starting value"))
     e1=int(input("enter destination value"))
     d1=e1-s1
     p1=d1*10
     print("fare cost :",p1)
     i1+=1
     break
  elif ct==2:
     while i2<3:
       print("macro is available")
       s2=int(input("enter starting value"))
       e2=int(input("enter destination value"))
       d2=e2-s2
       p2=d2*20
       print("fare cost :",p2)
       i2+=1
       break 
  elif ct==3:
     while i3<3:
       print("share is available")
       s3=int(input("enter starting value"))
       e3=int(input("enter destination value"))
       d3=e3-s3
       p3=d3*30
       print("fare cost :",p3)
       i3+=1
       break   
  elif ct==4:
     while i4<3:
       print("mini is available")
       s4=int(input("enter starting value"))
       e4=int(input("enter destination value"))
       d4=e4-s4
       p4=d4*40
       print("fare cost :",p4)
       i4+=1
       break  
  a=input("enter s to continue or q to quit")     