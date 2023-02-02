#Dictionary Comprehension
d={n:n*n for n in range(1,6)}
print(d)


#calculating product price for 5 units
old={"rice":60,"wheat":50,"dal":70}
new={product:price*5 for (product,price) in old.items()}
print(new)


#with checks
real={"Shaheer":35,"Dev":22,"Arjun":18}
now={name:age for (name,age) in real.items() if age>20}
print(now)


#printing random discounts
import random
cust=["Dev","Jay","Reethu","Aaradhya","Manasa"]
cust_dis={names:random.randint(1,10) for names in cust}
print(cust_dis)

#taking marks and displaying percentage 
names=list(map(str,input("Enter the students names:").split(",")))
marks=list(map(int,input("Enter the total marks for 5 subjects:").split(",")))
percent=[]
for i in range(len(marks)):
           p=round((marks[i]/500)*100,2)
           percent.append(p)
dis={st_names:st_percent for(st_names,st_percent) in zip(names,percent)}
print(dis)


s=str(input("Enter a string:"))
ch=str(input("Enter a character:"))
if ch in s:
    print("Yes")
else:
    print("No")


s=input("Enter a string:")
print(s[::-1])
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


s=str(input("Enter a string:"))
count=0
for i in s:
      if " " in i:
         count=count+1
      else:
          pass
if(count>=1):
    print(count)
else:
    print("No spaces in the string")


s=str(input("Enter a string:"))
for i in s:
    print(i)


l=['a','e','i','o','u','A','E','I','O','U']
s=str(input("Enter the string:"))
vowel=0
for i in s:
    if i in l:
        vowel=vowel+1
    else:
        pass
if(vowel>=1):
    print(vowel," vowels are present")
else:
    print("No vowels")
    


           

