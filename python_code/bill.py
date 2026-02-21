cus_name = input("Enetr customer name : ")
cus_Id = int(input("Enter customer id : "))
prev_meter_read = float(input("Enter previos meter reading : "))
curr_meter_read = float(input("Enter current meter reading :"))
units_consumed = curr_meter_read - prev_meter_read
cost_per_unit = 16
basic_charges = units_consumed * cost_per_unit
gst_tax = basic_charges * 0.17
meter_rent = 150 
total_bill = basic_charges + gst_tax + meter_rent

print("====" * 8)
print(f"Customer ID               : {cus_Id}")
print(f"Customer name             : {cus_name}")
print(f"previous meter Reading    : {prev_meter_read}")
print(f"Current meter reading     : {curr_meter_read}")
print(f"Units Consumed            : {units_consumed}")
print(f"cost per unit             : {cost_per_unit}")
print(f"Basic charges             : {basic_charges}")
print(f"Gst tax                   : {gst_tax}")
print(f"Meter rent                : {meter_rent}")
print(f"Total Electriciyy Bill    : {total_bill}")