# prompt the user for the year they were born in\
birth_year_raw = input("What year were you born in?: ")
# print type of raw birth year input
print(type(birth_year_raw))
# convert birh year
birth_year = int(birth_year_raw)
# print type of converted birth year
print(type(birth_year))
# calculate & return user's age based on birth year input
age = 2022 - birth_year
print(f"You are {age} years old.")
# check and print boolean and float type
print(type(True), type(3.3))
