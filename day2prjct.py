print("welcome to the tip calculator!")
bill=float(input("what was the total billl? $"))
tip=int(input("what percentage tip would you lie to give? 10 12 15"))
people=int(input("how many people to split the bill? "))
# bill_with_tip=bill*(1+tip/100)
# print(bill_with_tip)
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")