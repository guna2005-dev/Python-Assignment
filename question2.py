def question2():
    # Taking input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nResults:")

    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")
    print(f"{num1} / {num2} = {round(num1 / num2, 2)}")
    print(f"{num1} % {num2} = {num1 % num2}")
    print(f"{num1} ^ {num2} = {num1 ** num2}")

question2()