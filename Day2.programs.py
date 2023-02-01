#program on bitwise operators
n1,n2=map(int,input("Enter two numbers:").split())
if(n1<15 and n2<15):# or if n1 and n2 <15
    print(n1&n2)
    print(n1|n2)
    print(n1^n2)
else:
    print("Input exceeds 15")



#multiple inputs-->a=list(map(int,input().strip().split()))
n=int(input("Enter Size:"))
a=list(map(int,input("Enter the numbers:").strip().split()))[:n]
print(a)

n=int(input("Enter size as 10:"))
a=list(map(int,input("Enter the numbers:").strip().split()))[:n]
prod=1
for i in a:
    prod=prod*i
print(prod)


#printing using end delimiter
print("its","a","good","day",end="")
print("all","is","good")

print("its","a","good","day",end=" ")
print("all","is","good")

print("its","a","good","day",end="#")
print("all","is","good")

print("its","a","good","day",end=" *")
print("all","is","good")

#printing using seperator delimiter
print("its","a","good","day",sep="$")
print("all","is","good")

print("its","a","good","day",sep="$")
print("all","is","good",sep="$")

print("its","a","good","day",end=" ")
print("all","is","good",sep="***",end=" ")
print("joy")

#reverse triangle
print("* * * * *")
print(" * * * * ")
print("  * * *  ")
print("   * *   ")
print("    *    ")


#heart pattern
print("    *   *")
print("  *   *   *")
print("*           *")
print("  *       *")
print("    *   *")
print("      *")


#prog to find the temperature
temp=int(input("Enter the temperature:"))
if(temp>45):
    print("Hottest")
elif(temp>40 and temp<=45):
    print("Hot")
elif(temp>25 and temp<=40):
    print("Moderate")
elif(temp>10 and temp<=25):
    print("Cold")
else:
    print("Chill")


#prog to check whether the given number is 500 or not
num=int(input("Enter a number:"))
if(num==500):
    print("Entered number is 500")
else:
    print("Entered number is not 500")


#prog to find even-positive even-negative odd-positive and odd-negative
num=int(input("Enter the number:"))
if((num%2==0) and num>0):
    print("The given number is:",num ,"is even positive")
elif((num%2!=0) and num>0):
    print("The given number is:",num ,"is odd positive")
elif((num%2==0) and num<0):
    print("The given number is:",num ,"is even negative")
else:
    print("The given number is:",num ,"is odd negative")


#prog to check the greatest among two numbers
n1,n2=map(int,input("Enter two numbers:").split(","))
if(n1>n2):
    print(n1,"is the greatest number")
else:
    print(n2,"is the greatest number")


#prog to check whether it is float or integer
n1=26.9
n2=26
print(n1,"is a float number")
print(n2,"is an integer number")
num=input("Enter a number:")
if "." in num:
    print("Floating point number")
else:
    print("Integer number")
n=2
if isinstance(n,float)==True:
    print("Floating point number")
else:
    print("Integer number")
num=input("Enter a number:")
if(type(num)=="int"):
    print("Integer number")
else:
    print("Floating number")


#prog to check the greatest among three numbers
n1,n2,n3=map(int,input("Enter three numbers:").split(","))
if(n1>n2 and n1>n3):
    print(n1,"is the greatest number")
elif(n2>n1 and n2>n3):
    print(n2,"is the greatest number")
else:
    print(n3,"is the greatest number")


#prog to check whether it is divisible by 11
num=int(input("Enter a number:"))
if(num%11==0):
    print(num,"is divisible by 11")
else:
    print(num,"is not divisible by 11")


#prog to check whether it is divisible by both 2 and 5
num=int(input("Enter a number:"))
if(num%2==0 and num%5==0):
    print(num,"is divisible by both 2 and 5")
else:
    print(num,"is not divisible by both 2 and 5")


#printing numbers from 1 to 10 using while 
n=1
while n<=10:
    print(n,end=" ")
    n+=1


#print all even numbers b/w 2 to 20
n=2
while(n<=20):
    if(n%2==0):
        print(n,end=" ")
    n=n+1

#printing first 30 even numbers
count=30
i=0
while count!=0:
    i=i+1
    if(i%2==0):
        print(i,end=" ")
        count=count-1


#print all even numbers b/w 2 to 20
n=2
while(n<=20):
    if(n%2==0):
        print(n,end=" ")
    n=n+1


#printing first 30 even numbers
count=30
i=0
while count!=0:
    i=i+1
    if(i%2==0):
        print(i,end=" ")
        count=count-1


#print all the odd numbers b/w 1 to 30
n=1
while(n<=30):
    if(n%2!=0):
        print(n,end=" ")
    n=n+1

#prog to print the correctly guessed random number
import random
n=random.randrange(1,50)
guess=int(input("Enter a number:"))
while n!=guess:
    if(guess<n):
        print("Too low")
        guess=int(input("Enter the number again:"))
    elif guess > n:
        print("Too high")
        guess=int(input("Enter the number again:"))
    else:
        break
print("Your guess is right")


