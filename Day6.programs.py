#exception prog number 1
a=100
b=0
try:#u r telling this may have error
    print(a/b)
#except Exception:#u r saying if error there i'll handle
except Exception as e:
    print("Please note , number can't be divided by zero",e)#this will print error also
#to check your prog execution goes till end or not
print("End of the code")


#exception prog number 2
#whenever you open a file make sure you close it
a=100
b=0
try:
    print("Resorce open")
    print(a/b)
except Exception as e: #except zerodivision as e
    print("Please note , number can't be divided by zero",e)
finally:
    print("Resource closed")


#multiple exceptions in try block
a=100
try:
    b=int(input("Enter a number:"))
    d=a/b
except ZeroDivisionError as e:
    print("Number can't be divided with zero",e)
except ValueError as e:
    print("Invalid input",e)
except Exception as e:
    print("Other error",e)
finally:
    print("End of the code")

#user defined exception
x=int(input("Enter a number:"))
try:
    if x%2==0:
        raise Exception("x is an even number")
except Exception as e:
    print(e)
finally:
    print("End")


#class creation
class computer():   #class definition  
    def config(self):  #method definition
        print("Yes")
lenova=computer()    #object1 creation
lenova.config()     #method call using object 1
hp=computer()     #object2 creation
hp.config()     #method call using object 2


#class creation using constructor
class Employee():
    def __init__(self,emp_id,name):  #construction
        self.emp_id= emp_id
        self.name=name
    def display(self):
        print("ID:%d \nName:%s" %(self.emp_id,self.name))
emp1=Employee(101,"DEV")
emp2=Employee(102,"JAY")
emp1.display()
emp2.display()


#checking the scope of the variable
class computer():
    a=10
    b=20
    print("Class variables:",a)
    def config(self):
        c=30
        print("Method variable:",c)
        print("Instance variables:",self.b)
lenova=computer()
print(lenova.a)
dell=computer()
print(dell.config())
print(dell.c)












