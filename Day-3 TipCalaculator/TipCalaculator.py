print("Welcome to TipCalaculator!!")

totalBill = float(input("How much your total Bills ?\n$"))  # 120
percentageOfTip = float(input("How much % would like give for Tip? 10,12 or 15 ?\n%"))
headCount= int(input("How many people joined you for dinner?\n "))
print("Each person Bill Amount inc. Tip :")
total_Bill_withTip = totalBill+(totalBill * (percentageOfTip/100))
each_person_share = total_Bill_withTip / headCount
print(f"You Bill Amount :: ${each_person_share:.2f}")
print("Thanks for Tip .. Visit us Again!!!")
