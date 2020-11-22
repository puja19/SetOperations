#Task 4 - Now that we have learnt the basics of Python programming language,
#let's get our hands dirty and create a new python program. Write a Python Program to Illustrate Different Set Operations.
#Here we have to define two set variables and we have to perform different set operations: union, intersection, difference and symmetric difference.
#Your Output should look something like this
#Union of E and N is {0, 1, 2, 3, 4, 5, 6, 8} Intersection of E and N is {2, 4} Difference of E and N is {8, 0, 6} Symmetric difference of E and N is {0, 1, 3, 5, 6, 8}

#Taking input from user

#set N
s1=[]
#Number of elements as input 
d=int(input("Enter number of elements for E "))
#Iterating till the range
for i in range(0,d):
    ele=int(input())
    s1.append(ele)
s11=s1.copy()

#set N
s2=[]
#Number of elements as input
d=int(input("Enter number of elements for N "))
#Iterating till the range
for i in range(0,d):
    ele=int(input())
    s2.append(ele)
s21=s2.copy()

print()
print('Input string N ')
print(s11)
print('Input string M ')
print(s21)
print()

#UNION

s5=s1+s2
#removing repeation
s5.sort()
f=0
s8=[s5[f]]

for w1 in s5:
    if w1==s8[f]:
        continue
    else:
        s8.append(w1)
        f=f+1
            
print('The Union of set E and N without repitation are ')
print(s8)

#INTERSECTION

s3=[]
for i in s1:
    flag=1
    for j in s2:
        if i==j and flag==1:
            s3.append(i)
            s2.remove(j)
            flag=2
#removing repeation
s3.sort()
f=0
s4=[s3[f]]

for w1 in s3:
    if w1==s4[f]:
        continue
    else:
        s4.append(w1)
        f=f+1
            
print('The Intersection of set E and N without repitation are ')
print(s4)

#DIFFERENCE
s61=s11.copy()
for i in s1:
    flag=1
    for j in s3:
        if i==j and flag==1:
            s61.remove(j)
            flag=2

print('The Difference set N-E without repitation is ')
print(s61)

s62=s21.copy()
for i in s21:
    flag=1
    for j in s3:
        if i==j and flag==1:
            s62.remove(j)
            flag=2

print('The Difference set E-N without repitation is ')
print(s62)

#SYMMETRIC DIFFERENCE
s71=s5.copy() #N union M
s7=s5.copy() #N union M
s72=s4.copy() #N intersection M

for i in s71:
    flag=1
    for j in s72:
        if i==j and flag==1:
            s7.remove(j)
            flag=2

print('The Symmetric Difference set N-E without repitation is ')
print(s7)
