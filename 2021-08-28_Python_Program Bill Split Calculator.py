#Python program Bill Split Calculator
"Computer Programming Tutor, June 23, 2021"

print("Welcome To Ernies Bill Split Calculator")
print("=======================================")

totbill = float(input("What is The Total Bill?: "))

salespercent = int(input("What % Tip Would you Like o give?:"))

#Prompt The User For The Number of People Splitting The Bill
nopeople = int(input("How Many People Are Splitting The Bill?: "))
print("\n")

# Calculate The Value of Each Person Owes Based On The Bill

payment_per_person = ("%.2f" % round(float(((salespercent/100 + 1)*totbill)/nopeople),2))

salespayment = "%.2f" %float(salespercent/100*totbill)
print(f"Tip Amount: £{salespayment}")

totbillfloat = float(totbill)
salespayment_float = float(salespayment)
total = (totbillfloat + salespayment_float)

print(f"Total Bill Including Tip: £{total}")

print(f"Each Person Owes: £{payment_per_person}")
