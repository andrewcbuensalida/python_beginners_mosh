weight = float(input("Weight: "))
metric = input("(K)g or (L)bs: ").upper()
if metric == "L":
    print("Weight in kilograms is " + str(weight * 0.453592))
elif metric == "K":
    print("Weight in pounds is " + str(weight * 2.20462))