
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)
if bmi < 18.5:
  print("Your bmi is:", bmi, "you are underweight.")
elif bmi < 25:
  print("Your mbi is:", bmi, "your have a normal weight.")
elif bmi < 30:
  print("Your bmi is:", bmi, "you are overweight.")
elif bmi < 35:
  print("Your bmi is:",  bmi, "you are obese.")
else: 
  print("Your bmi is", bmi, "you are clinically obese.")
