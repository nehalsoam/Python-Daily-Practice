# E-commerce discount using statements
purchase_amount=int(input("enter amt: "))
is_member=input("Enter Yes/No: ")
if purchase_amount>=5000:
    if is_member=="Member":
        discount=20
    else:
        discount=10
else:
    purchase_amount<5000
    if is_member=="Not Member":
        discount=10
    else:
        discount=5
discount_amount = purchase_amount * discount / 100
final_amount = purchase_amount - discount_amount

print("Discount:", discount, "%")
print("Discount Amount:", discount_amount)
print("Final Amount:", final_amount)
        
        
        