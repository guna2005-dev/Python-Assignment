def question8():
    year = int (input("Enter a year:"))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"\n{year} is a leap year.")
        print("reason: Divisible by 4 and not divisible by 100, or divisible by 400.")

    else:
        print(f"\n{year} is NOT a leap year.")
        print("Reason: Does not satisfy leap year conditions.")
question8()