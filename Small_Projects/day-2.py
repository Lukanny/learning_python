print("Welcome to the tip calculator.")
bill_value = float(input("What was the total bill? $"))
people_amount = int(input("How many people t split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))/100
total_bill = bill_value * (1 + tip_percentage)
individual_bill = total_bill / people_amount
print(f"Each person should pay: ${round(individual_bill, 1)}")