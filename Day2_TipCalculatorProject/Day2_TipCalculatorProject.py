print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $\n"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))

total_cost = (bill / people) * (1+ tip/100)
bill_per_person = round(total_cost, 2)

print(f"Each person should pay ${bill_per_person}")

