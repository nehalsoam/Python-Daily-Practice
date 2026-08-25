#Q1->check number is even or odd
# num=int(input("enter a num: "))
# result="Even"*(num%2==0)+"Odd"*(num%2==1)
# print(result)45

#Q2->find total,average,percentage of 5subjects
# s1=float(input("enter marks of s1: "))
# s2=float(input("enter marks of s2: "))
# s3=float(input("enter marks of s3: ")) 
# s4=float(input("enter marks of s4: "))
# s5=float(input("enter marks of s5: "))
# total=s1+s2+s3+s4+s5
# average=total/5
# percentage=total/500*100
# print("total marks= ",total)
# print("average= ",average)
# print("percentage= ",percentage,"%")

#Q3->find Simple Interest
# P=float(input("enter principle: "))
# R=float(input("enter rate of interest: "))
# T=float(input("enter time: "))
# SI=P*R*T/100
# print("Simple interest: ",SI)

#Q4->find last digit 
# num=int(input("enter a digit: "))
# last_digit=num%10
# print("last digit is: ",last_digit) 

#Q5->swap two number without using third 
# a=5
# b=10
# a=a+b
# b=a-b
# a=a-b
# print(a)
# print(b)

#Q6->convert total seconds into hours,minutes,seconds 
total_sec=int(input("enter total sec: "))
hours=total_sec//3600
remain_sec=total_sec%3600
minutes=remain_sec//60
sec=remain_sec%60
print(f"{total_sec}={hours}hr{minutes}min{sec}sec")