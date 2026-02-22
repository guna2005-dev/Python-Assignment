def question4():
    current_year = 2026
    birth_year = int ( input ("Enter your birth year:"))

    age = current_year - birth_year

    print("\nYour Age Details:")
    print("Current Age:", age, "yeras")
    print("Age in Months:", age * 12)
    print("Age in Days:", age * 365)
    print("Age in Hours:", age * 365 * 24)
    print("Age in Minutes:", age * 365 * 24 * 60)
    print("Years until 100:", 100-age)
question4()
                    