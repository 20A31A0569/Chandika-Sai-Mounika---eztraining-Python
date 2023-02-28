#encapsulation protected
class encap:
    _a=10
    c=20
    def encapfunction(self):
        _b=200
        print("Function accessing the protected variables")
        print(self._a+10)
obj=encap()
print(obj._a)
obj.encapfunction()
print(obj.c)

#encapsulation private
class encap:
    __a=10
    print(__a)
    def encapfunction(self):
        print("Encap function")
        print(self.__a)
obj=encap()
obj.encapfunction()
print(obj.__a)    #will throw an error bcuz they cannot access outside the class


#Polymorphism-->overloading
#method overloading
class moverload:
    def display(self,a=None,b=None):
        print(a,b)
obj=moverload()
print("Without arguments")
obj.display()
print("With two arguments")
obj.display(10,20)

print("With one argument")
obj.display(10)

#Polymorphism-->overriding
class parent:
    def __init__(self):
        self.value="Inside parent"
        print(self.value)
class child(parent):
    def __init__(self):
        self.value="Inside child"
        print(self.value)
obj=parent()
obj=child()

#Polymorphism-->overriding
class Vijayawada:
    def placename(self):
        print("Vijayawada placenem is KLU")
    def student(self):
        print("Yes-Vijayawada")
    def which_year(self):
        print("3rd year-Vijayawada")
class Vizag:
    def placename(self):
        print("Vizag placenem is VZ-KLU")
    def student(self):
        print("Yes-Vizag")
    def which_year(self):
        print("3rd year-Vizag")
obj_vij=Vijayawada()
obj_vz=Vizag()
for details in (obj_vij,obj_vz):
    details.placename()
    details.student()
    details.which_year()


#prog to create a single linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head  #temp=first node
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next  #establishing link
obj=LinkedList()
#Node creation
n=Node(10)   #so n.data in node class will be assigned first node as head
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
obj.display()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp=self.head  #temp=first node
            while temp:
                print(temp.data,end=" ")
                temp=temp.next  #establishing link
obj=LinkedList()
#Node creation
n=Node("W")   #so n.data in node class will be assigned first node as head
obj.head=n
n1=Node("I")
n.next=n1
n2=Node("N")
n1.next=n2
n3=Node("N")
n2.next=n3
n4=Node("E")
n3.next=n4
n5=Node("R")
n4.next=n5
obj.display()


#insertion at begining 
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None
    def InsertBegining(self,data):
        nn=Node(data)
        nn.next=self.head
        self.head=nn
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
obj=SLinkedList()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("Before inserting")
obj.display()
print("")
obj.InsertBegining(100)
print("After inserting")
obj.display()


#insertion at end
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None
    def InsertEnd(self,data):
        nn=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=nn
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
obj=SLinkedList()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("Before inserting")
obj.display()
print("")
obj.InsertEnd(100)
print("After inserting")
obj.display()


#insertion at given position
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLinkedList:
    def __init__(self):
        self.head=None
    def InsertPosition(self,data,pos):
        nn=Node(data)
        temp=self.head
        for i in range (pos-1):
            temp=temp.next
        nn.next=temp.next
        temp.next=nn
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
obj=SLinkedList()
n=Node(10)
obj.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
print("Before inserting")
obj.display()
print("")
obj.InsertPosition(100,4)
print("After inserting")
obj.display()




        






        

        
