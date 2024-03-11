def bmi(weight, height):
    bmi = weight / (height**2)

    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "overweight"
    else:
        return "Obese"


print(bmi(17.5, 87.2))
