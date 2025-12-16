age_of_oldboy = 56

age = int(input("your guess:"))
if age == age_of_oldboy:
    print("you r right")
elif age < age_of_oldboy:
    print("too small")
else:
    print("too big")