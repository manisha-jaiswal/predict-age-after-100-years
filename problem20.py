"""Your Age In 2090
Take age or year or birth as an input from the user and tell them when they will turn 100 years old.(5 points) Don’t use any type of module like datetime or dateutils(-5 points).

They can then optionally provide a year and your program must tell their age in that particular year. (3 points) You should be handling all sorts of errors like (2 points):
You are not yet born
You seem to be the oldest person alive
You can also handle any other error if possible!
"""
yearAge = int(input("What is your Age/Year of birth\n"))
isAge = False
isYear = False

if len(str(yearAge)) == 4:
    isYear = True

else:
    isAge = True

if(yearAge<1900 and isYear):
    print("You seem to be the oldest person alive")
    exit()

if(yearAge>2019):
    print("You are not yet born")
    exit()

if isAge:
    yearAge = 2019 - yearAge

print(f"You will be 100 years old in {yearAge + 100}")

interestedYear = int(input("Enter the year you want to know your age in\n"))

print(f"You will be {interestedYear - yearAge} years old in {interestedYear}")

