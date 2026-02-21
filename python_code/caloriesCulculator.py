name = input("Enter your name \n")
weight = float(input("Enter your weight  in kg \n"))
height = float(input("Enetr height in meter \n"))
age = int(input("Enter your age \n"))
steps = int(input("Enter your daily walk steps \n"))
bmi = weight/(height ** 2)
calories_burned = steps * 0.04
lower_ideal_weight = 18.5 * (height ** 2)
upper_ideal_weight = 24.9 * (height ** 2)

print(f"your lower ideal weight is {lower_ideal_weight} and hiher ideal weight is {upper_ideal_weight}.")