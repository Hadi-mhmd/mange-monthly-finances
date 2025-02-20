def user_input():
    month=input("enter the month name: ")
    salary=float(input("enter your salary: "))

    percentage={
        "savings":float(input("enter the percentage for savings: ")),
        "rent": float(input("enter the percentage for rent: ")),
        "Electrecity": float(input("enter the percentage for electrecity: "))
    }
    return month,salary,percentage
month,salary,percentage=user_input()
# print(percentage)

def percentage_amount(salary,percentage):
    percamount={}
    for percent,percvalue in percentage.items():
        percamount[percent]=(percvalue/100)*salary
    return  percamount  
    
percamount=percentage_amount(salary,percentage)    
print(percamount)