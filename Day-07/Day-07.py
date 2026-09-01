# Q1->API Response Status Code
status_code=int(input("enter code: "))
if status_code==200:
    print("Success")
elif status_code==201:
    print("Created")
elif status_code==400:
    print("Bad request")
elif status_code==401:
    print("Unauthorized")
elif status_code==403:
    print("Forbidden")
elif status_code==404:
    print("Not found")
elif status_code==500:
    print("Server error")
else:
    print("Unkown Status code")
    
# Q2->Password Strength Checker
password=input("enter your password")
if len(password)>=8:
    print("Strong password")
else:
    print("Weak password: ")  
    
#Q3-> Employee Login + Role
username=input("Enter your name: ")
password=input("Enter your password: ")
role=input("Enter your role: ")
if username=="NehalSoam":
    print("Username correct")
    if password=="1234":
        print("password correct")
        if role=="Admin":
            print("Full Access")
        elif role=="Manager":
            print("Limited Admin access")
        elif role=="Employee":
            print("Employee Dashboard")
        else:
            print("Acess denied")
    else:
        print("Invalid password")
else:
    print("Invalid username")
    
#Q4->Online shopping Eligiblity
cart_amount=int(input("Enter amount: "))
stock_available=input("enter Y/N: ")
user_logged_in=input("enter Y/N: ")
if user_logged_in=="Yes":
    print("login")
    if stock_available=="Yes":
       print("available")
       if cart_amount>=499:
           print("free delivery")
       else:
           print("Not free delivery")
    else:
        print("not available")
else:
    print("not login")
#Q4->Internship Eligibility Checker
python_score=int(input("Enter py_score: "))
sql_score=int(input("Enter sql_score: "))
projects=int(input("Enter project_score: "))
CGPA=int(input("Enter CGPA: "))
if python_score>=60 and sql_score>=1 and projects>=1 and CGPA>=6:
    print("Eligible for Python Internship")
else:
    print("not eligible")