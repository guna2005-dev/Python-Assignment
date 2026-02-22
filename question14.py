def question14():
    n = int(input("Enter a number:"))

    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return
    elif n == 0:
        print("0! = 1")
        return 
    factorial = 1
    steps = []

    for i in range (n, 0, -1):
        factorial *= i
        steps.append(str(i))

    step_str = " x ".join(steps)
    print(f"{n}! = {step_str} = {factorial}")

question14()
