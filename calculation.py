def user_input():
    month=input("enter the month name: ")
    if month.lower() == "stop":
        return None  
    salary=float(input("enter your salary: "))
    
    percentage={
        "savings":float(input("enter the percentage for savings: ")),
        "rent": float(input("enter the percentage for rent: ")),
        "Electrecity": float(input("enter the percentage for electrecity: "))
    }

    bonus_input=input("enter extra saving or press enter to take 50 as default: ")
    bonus_saving=float(bonus_input) if bonus_input.strip() else 50

    return month,salary,percentage,bonus_saving
# month,salary,percentage,bonus_saving=user_input()
# print(percentage)

def percentage_amount(salary,percentage):
    percamount={}
    for percent,percvalue in percentage.items():
        percamount[percent]=(percvalue/100)*salary
    return  percamount  

# percamount=percentage_amount(salary,percentage)    
# print(percamount)

def calculate_financial(salary,percamount,bonus):
    total_spent=percamount["savings"]+percamount["rent"]+percamount["Electrecity"]
    remainder_salary=salary-total_spent
    rent_per_year=percamount["rent"]*12
    Electrecity_per_year=percamount["Electrecity"]*12
    squared_salary=salary*salary

    saving=percamount["savings"]
    remainder_extra=bonus%saving if saving>0 else bonus

    return {
        "Salary":salary,
        "percamount":percamount,
        "Total spent":total_spent,
        "remaining":remainder_salary,
        "yearly rent":rent_per_year,
        "yearly elect":Electrecity_per_year,
        "bonus":bonus,
        "remainder extra":remainder_extra,
    }    

months_data={} 
   
while True:
    user_input_data = user_input()
    if user_input_data is None:  
        break
    month,salary,percentage,bonus_saving=user_input_data
    percamount=percentage_amount(salary,percentage)  
    months_data[month]=calculate_financial(salary,percamount,bonus_saving)


for month,data in months_data.items():
    print("\nMonth:", month)
    for key,value in data.items():
        print(f"{key}:{value}")
    


