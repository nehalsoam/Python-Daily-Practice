#Loops 
# Q1->print 1 to 10 numbers
# FOR LOOP
for i in range(1,11):
    print(i)
    
#Q2->Print 10 to 1 in reverse order

for i in range(10, 0, -1):
    print(i) 
    
#Q3->Print 1 to 20 even numbers
for i in range(2,20,2):
    print(i)    
    
#Q4->Print 1 to 20 odd numbers
for i in range(1,20,2):
    print(i)
    
#Q5->Print 1 to n numbers taking input from users
n=int(input("Enter a num:"))
for i in range(1,n+1):
    print(i)
    
#Q6-> Print 5 table 
num=int(input("Enter a num: "))
for i in range(1,11):
    print(num,"*",i,"=",num*i)
    
#Q7-> print sum of 1 to 100 numbers
total=0
for i in range(1,101):
    total=total+i
print(total)
#Q8-> Print sum from 1 to n taking input from user
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

#Q9->print sum of all divisible number from 1 to 100
for i in range(1,101):
    if i%5==0:
        print(i)
        
#Q10->print all even numbers from 1 to 100 if num is even increase one counter and print it
count=0
for i in range (1,101):
    if i % 2==0:
        count=count+1
print(count)

#Q11->Find Factorial
n=int(input("enter a num:"))
fact=1
i=1
while i<n:
    fact=fact*i
print(fact)