weight=float(input("Please enter your weight: "))
height=float(input("Please enter your height: "))
bmi=round(weight/height**2)
print(bmi)
if bmi<18.5:
    print("Underweight")
elif bmi>18.25 and bmi<25:
    print("Normal weight")
elif bmi>25 and bmi<30:
    print("Overweight")
elif bmi>30 and bmi<35:
    print("Obese")
elif bmi>35:
    print("Clincally obese")
    