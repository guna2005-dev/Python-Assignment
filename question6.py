def question6():
    print(" Enter marks for 5 subjects (out of 100):")

    s1 = float(input("Subject 1: "))
    s2 = float(input("Subject 2: "))
    s3 = float(input("Subject 3: "))
    s4 = float(input("Subject 4: "))
    s5 = float(input("Subject 5: "))

    total = s1 + s2 + s3 + s4 + s5
    percentage = total / 5

    # Grade calculation
    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Average)"
    elif percentage >= 50:
        grade = "D (Passing)"
    else:
        grade = "F (Failing)"

    # Pass/Fail condition
    if s1 >= 40 and s2 >= 40 and s3 >= 40 and s4 >= 40 and s5 >= 40:
        result = "Pass"
    else:
        result = "Fail"
        
    print("\n=== RESULT ===")
    print("Marks:", s1, s2, s3, s4, s5)
    print("Total Marks:", total, "/500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
    print("Result:", result)

question6()