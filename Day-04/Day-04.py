# login credential
username = input("Enter username: ")
password = input("Enter password: ")

if username == "Nehalsoam":
    if password == "1234":
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Invalid username")
    
# # ATM withdrawal
Balance=int(input("enter your balance: "))
withdrawal_amt=int(input("enter your withdrawal_amt: "))
if withdrawal_amt<=0:
    print("positive amt")
elif withdrawal_amt<=Balance:
     print("withdrawal successfully")
else:
    print("invalid amount")