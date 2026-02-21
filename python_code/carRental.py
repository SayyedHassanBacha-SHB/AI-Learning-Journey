name = input("Enter your name ")
car_type = input("Enter car type")
renting_days = int(input("Enter your renting days"))
daily_rate = int(input("Enter your daily rate for car renting"))
drive_car_inkm = float(input("Enter estimated kilomator of car drive"))
rental_cost = daily_rate * renting_days
fuel_cost = drive_car_inkm * 15
insurance = renting_days* 200
total_cost = rental_cost + fuel_cost + insurance

print("==="*6)
print(f"customer name   : {name}")
print(f"Car type        : {car_type}")
print(f"renting days    : {renting_days}")
print(f"daily rent      : {daily_rate}")
print(f"estimted car km : {drive_car_inkm}")
print(f"Rental cost     : {rental_cost}")
print(f"fuel cost       : {fuel_cost}")
print(f"insurance cost  : {insurance}")
print(f"Total cost      : {total_cost}")