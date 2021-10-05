import math
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))
#input dau ra cua no la string nen khi nhap vao tu ban phim la so 3 thi ham tra ve la string "3". Nhung do la canh cua tam giac nen string 
#so "3" phai chuyen thanh kieu float 3
#de chuyen ta phai dung float ("3") ==> 3
p = (a+b+c)/2
area = math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Area of the triangle is: ", area)

