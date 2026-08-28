#College Admission Eligibility
percentage=int(input("enter percentage"))
entance_exam_score=int(input("enter percentage"))
if percentage>=60:
    print("valid percentage")
    if entance_exam_score>=50:
        print("Eligible")
    else:
        print("Invalid")
else:
    print("Not Eligible")
    
#Employee Bonus calculator
salary = int(input("Enter salary: "))
experience = int(input("Enter experience in years: "))

if experience >= 5:

    if salary >= 50000:
        bonus_percent = 20
    else:
        bonus_percent = 15

else:

    if salary >= 50000:
        bonus_percent = 10
    else:
        bonus_percent = 5

bonus = salary * bonus_percent / 100
final_salary = salary + bonus

print("Bonus:", bonus)
print("Final Salary:", final_salary)