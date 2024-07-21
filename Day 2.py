print("Welcome to the tip calculator")
total_bill = float(input("what was the total bill ? \n$"))
percentage = float(input("What percentage would you like to give? 10,12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))
temp1 = total_bill*(percentage/100)
temp2 = total_bill + temp1
individual_bill = temp2/people
print(f"Each person should pay ${round(individual_bill,2)}")