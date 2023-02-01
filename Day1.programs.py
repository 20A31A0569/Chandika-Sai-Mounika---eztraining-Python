i1=int(input("Enter First integer:"))
i2=int(input("Enter Second integer:"))
i3=int(input("Enter Third integer:"))
print("First integer :",i1)
print("Second integer :",i2)
print("Third integer :",i3)


f1=float(input("Enter First float number:"))
f2=float(input("Enter Second float number:"))
f3=float(input("Enter Third float number:"))
print("First float number :",f1)
print("Second float number :",f2)
print("Third float number :",f3)


s1=str(input("Enter the first string:"))
s2=str(input("Enter the second string:"))
print("First String :",s1)
print("Second String :",s2)


c=complex(input("Enter complex number:"))
print("Complex number :",c)


kcandy=75
scandy=kcandy/2 #kumar gave half of it to sam
kcandy1=scandy/2 #sam gave half to kumar
kcandy=scandy+kcandy1 #remaining half plus sam's candy
print(kcandy)
print(scandy/2)


print((3*36.32)+56.19-10)


print(5*(-9.1))


#swap using temp
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
print(n1,n2)
temp=n1
n1=n2
n2=temp
print(n1,n2)


#swap without temp
n1=int(input("Enter n1:"))#10
n2=int(input("Enter n2:"))#5
print(n1,n2)
n1=n1+n2#15
n2=n1-n2#10
n1=n1-n2
print(n1,n2)


#area of a rectangle
length=float(input("Enter length :"))
breadth=float(input("Enter breadth :"))
print("Area of a rectangle :",(length*breadth))


#perimeter of a rectangle
length=float(input("Enter length :"))
breadth=float(input("Enter breadth :"))
print("Perimeter of a rectangle :",(2*(length+breadth)))
