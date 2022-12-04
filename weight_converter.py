# prompt a user for their weight in pounds
weight_raw = input("How much do you weight (in pounds)?: ")
# convert user input from a string to a float
weight = float(weight_raw)
# convert their weight to kilograms
weight_in_kg = weight/2.205
# round weight to four decimal places
rounded_weight = round(weight_in_kg, 4)
# return the converted weight to the user
print(f"Your weight is {rounded_weight} kilograms")
