#Q1->check number is positive,negative or zero
num=int(input("enter a number: "))
if num>0:
    print("positive")
elif num<0:
    print("Negative")
else:
    print("Zero")
    
#Q2->check even or odd
num=int(input("enter a num"))
if num%2==0:
    print("even")
else:
    print("odd")
    
#Q3->check voter age for voting
user_age=int(input("enter your age: "))
if user_age>18:
    print("eligible")
else:
    print("Not eligible")
    
#Q4->check that you are pass or fail
marks=int(input("enter your marks: "))
if marks>=40:
    print("Pass")
else:
    print("Fail")

#Q5->check that your num is divisible by 5 or not
number=int(input("enter a number: "))
if number%5==0:
    print("Divisible")
else:
    print("Not divisible")

#Q6-> student Grade calculator
marks=int(input("enter your marks:  "))
if marks<90>100:
    print("A")
elif marks<80>89:
    print("B")
elif marks<70>79:
    print("C")
elif marks<60>69:
    print("D")
else:
    print("F")
    
#Q7->Temperature Category
temp=int(input("Enter temperature: "))
if temp>=40:
    print("Very hot")
elif temp<30>39:
    print("Hot")
elif temp<20>29:
    print("Normal")
elif temp<10>19:
    print("Cold")
else:
    print("Very cold")
    
#Q8->Number comparison
Fnum=int(input("Enter firstnum: "))
Snum=int(input("Enter Secondnum: "))
if Fnum>Snum:
    print("Fnum is greater")
elif Fnum<Snum:
    print("Snum is greater")
else:
    print("Both are equal")

#Q9->Menu Driven Calculator
fnum=int(input("Enter firstnum: "))
snum=int(input("Enter Secondnum: "))
op=input("enter a operation: ")

if op=='+':
    print(fnum+snum)
elif op=='-':
    print(fnum-snum)
elif op=='*':
    print(fnum*snum)
else:
    print(fnum/snum)

#10->Day Number
Day=int(input("enter a day: "))
if Day==1:
    print("Monday")
elif Day==2:
    print("Tuesday")
elif Day==3:
    print("Wednesday")
elif Day==4:
    print("Thursday")
elif Day==5:
    print("Friday")
elif Day==6:
    print("Saturday")
elif Day==7:
    print("Sunday")
else:
    print("Invalid Day")
    