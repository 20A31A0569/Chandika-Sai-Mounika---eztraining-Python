#sample function 
def sample():   #fun definition
    print("GOOD DAY")
    print("HAPPY TIME")
sample()        #fun call
print("TODAY")
sample()

#without arg, without return value
def prod():
    n1=int(input("Enter a number:"))
    n2=int(input("Enter a number:"))
    n3=int(input("Enter a number:"))
    m=n1*n2*n3
    print(m)
prod()


#without arg, with return value
def prod():
    n1=int(input("Enter a number:"))
    n2=int(input("Enter a number:"))
    n3=int(input("Enter a number:"))
    m=n1*n2*n3
    return m
multi=prod()
print(multi)


#with arg, without return value
def prod(a,b,c):
    m=a*b*c
    print(m)
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
n3=int(input("Enter a number:"))
prod(n1,n2,n3)


#with arg, with return value
def prod(a,b,c):
    m=a*b*c
    return m
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
n3=int(input("Enter a number:"))
multi=prod(n1,n2,n3)
print(multi)

#lemons prog using fun type 1
def lemon():
    l=int(input("Enter the number of lemons:"))
    if(l>21):
        print("Excess lemons are:",(l-21))
    elif(l<21):
        print("Need",(21-l),"more lemons to be offered")
    else:
        print("All the lemons are offered equally")
lemon()


#prog to find the factors of a given num
def factors():
    n=int(input("Enter the number:"))
    factors_list=[]
    for i in range(1,n+1):
        if n%i==0:
            factors_list.append(i)
    return factors_list
fac=factors()
print(fac,end=" ")


#prog to find the multiplication table of a given number
def table(n):
    if n>0:
        for i in range(1,11):
            prod=n*i
            print(n,"*",i,"=",prod)
num=int(input("Enter the number:"))
table(num)


#prog to find the sum of digits
def sum_digits(n):
    sum1=0
    while n>0:
         temp=n%10
         sum1=sum1+temp
         n=n//10
    return sum1
num=int(input("Enter the number:"))
final_sum=sum_digits(num)
print("Sum of the digits:",final_sum)


def add(l):
    s=0
    for i in l:
        s=s+i
    return s
lst=list(map(int,input("Enter the list numbers:").split(",")))
l_sum=add(lst)
print(l_sum)


#sample prog for recursion
def display():
    n=int(input("Enter a number:"))
    if (n==1):
        display()
    else:
        print("OVER")
display()


#factorial of given number using recursion
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter a number:"))
factorial=fact(num)
print("Factorial of ",num," is ",factorial)


#fibinocci series using recursion
def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the terms:"))
if n<=0:
    print("Positive number")
else:
    print("Fibonacci series of first ",n,"terms is:")
    for i in range(n):
        f=fibonacci(i)
        print(f)

#function returns more values
def add_sub(a,b):
    add=a+b
    sub=a-b
    return add,sub
a,b=list(map(int,input("Enter two numbers:").split(",")))
print(add_sub(a,b))




    


        
        



    
        



