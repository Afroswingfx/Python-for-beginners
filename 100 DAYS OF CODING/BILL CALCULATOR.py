
#My manual solution
#total_bill=150
#tip_1=0.1
#tip_2=0.12
#tip_3=0.15
#print("Welcome to the tip calculator")
#print(input("what was the total bill? $"))
#print(input(f"How much tip would you like to give? {tip_1}, {tip_2},or {tip_3}"))
#each_person=(1.12*150)/5
#print(each_person)
#individual_bill=(round(each_person,2))
#print(input("How many people to split the bill?"))
#print(f"Each person should pay {individual_bill}")
#I have a solution though its manually generated





#Tutor solution-automated
print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
tip=(int(input("What percentage tip would you like to give? 10, 12, 20 ")))
people=int(input("How many people to split the bell?"))
total_tip=(tip/100)*bill
total_bill_plus_tip=float(total_tip+bill)
bill_per_person=total_bill_plus_tip/people
final_amount=round(bill_per_person,2)
print(f"Each person should pay ${final_amount}")