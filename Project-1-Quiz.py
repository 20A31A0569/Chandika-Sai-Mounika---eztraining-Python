q1="""What's the captial state of India?
a=Mumbai
b=Delhi
c=Hyderabad
d=TamilNadu"""

q2="""Who is the cheif minister of Andhar Pradesh?
a=Nara Chandra Babu
b=Dr Manik Shah
c=Jagan Mohan Reddy
d=M.K Stalin"""

q3="""Who is the founder of Instagram?
a=Ambaani
b=Bill Gates
c=Elon Musk
d=Mark Zukerberg"""

q4="""First programming language?
a=B
b=C
c=Python
d=Java"""

q5="""calculate the follwing: (2*15+20)
a=50
b=35
c=80
d=70"""

que={q1:"b",q2:"c",q3:"d",q4:"a",q5:"a"}
name=input("Enter your name:")
print("Hello",name,".Lets begin the Quiz")
score=0
for i in que:
    print()
    print(i)
    flag=input("Do you want to skip the question?(Yes/No):")
    if flag=="Yes":
        continue
    ans=input("Enter your answer:")
    if ans==que[i]:
        print("WOW Your answer is correct!")
        score=score+1
        print("Your current score:",score)
    else:
        print("Oops your answer is wrong!")
        score=score-1
        print("Your current score:",score)
    flagg=input("Do you want to quit the Quiz?(Yes/No):")
    if flag=="Yes":
            break
print()
print("Your final score is :",score)
print("Thankyou for participating:)")
        
        

