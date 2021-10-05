#a = 4
#b = 6
#if (a>b):
    #print('gia tri cua a nho hon b')
#print('no result')

#x=15
#y=15
#if (x>=y):
 #   print("x lon hon y")
#else:
 #   print("x nho hon y")


#a=10
#if (a==10):
 #   if (a<15):
  #      print("a nho hon 15")
   # if (a<12):
    #    print("a nho hon 12")
     #   if(a%2==0):
      #      print("a la so chan nho hon 12")

#a = int(input("nhap so"))
#if(a%2==0):
 #   print("so chan")
  #  if(a>=20):
   #     print("so chan lon hon 20")
    #else:
     #   print("so chan nho hon 20")
#else:
 #   print("so le")

#import math
#a = int(input("nhap a"))      
#b = int(input("nhap b"))
#c = int(input("nhap c"))
#delta = b**2 - 4*a*c
#if(a==0):
 #   if (b==0):
  #      if (c==0):
   #         print("phuong trinh vo so nghiem")
    #    else:
     #       print("phuong trinh vo nghiem")
    #else:
     #   print(-c/b)
    
#else:
 #   if(delta<0):
  #      print("phuong trinh vo nghiem")
   # elif("delta=0"):
    #    print("phuong trinh co nghiem",int(-b/2*a))
    #else:
     #   print((int(-b+ math.sqrt(delta))/2*a, (-b- math.sqrt(delta))/2*a))


#x=7
#if(x%2==0):
 #   s= "x la so chan"
#else:
 #   s="x la so le"

#cu phap toan tu 3 ngoi:
#(true_value) if (condition) else (false_value);
#x = 7
#s= "x la so chan" if(x%2==0) else s="x la so le"
#print(s)


#a,b = 2,5
#max= a if (a>b) else b
#print(max)

x=7
s="x la so chan" if(x%2==0) else "x la so le"
print(s)