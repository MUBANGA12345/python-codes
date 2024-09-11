# categorize_age.py

# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Categorize the user based on their age
if age <= 12:
    print("You are a Child.")
elif age <= 19:
    print("You are a Teenager.")
elif age <= 59:
    print("You are an Adult.")
else:
    print("You are a Senior.")