def check_age(age):
    if age < 18:
        raise ValueError("You must be at least 18 years old.")
    else:
        print("You are eligible.")

try:
    check_age(17)
except ValueError as e:
    print("Caught Exception:", e)