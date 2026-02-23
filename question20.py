def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def reverse_number(n):
    return int(str(n)[::-1])

def is_armstrong(n):
    power = len(str(n))
    return n == sum(int(digit) ** power for digit in str(n))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def is_perfect_number(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def math_menu():
    while True:
        print("\n===NUMBER SYSTEM MENU ===")
        print("1. Factorial")
        print("2. Check Prime")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Check Armstrong")
        print("7. GCD")
        print("8. LCM")
        print("9. Check Perfect Number")
        print("10. Exit")

        choice = int(input("Enter number:"))

        if choice == 1:
            n = int(input("Enter number: "))
            print("Factorial:", factorial(n))
                  
        elif choice == 2:
            n = int(input("Enter number: "))
            print("Prime:" if is_prime(n) else "Not Prime")

        elif choice == 3:
            n = int(input("Enter number: "))
            print("Fibonacci:", fibonacci(n))

        elif choice == 4:
            n = int(input("Enter number: "))
            print("Sum of Digits:", sum_of_digits(n))

        elif choice == 5:
            n = int(input("Enter number: "))
            print("Reverse Number:", reverse_number(n))

        elif choice == 6:
            n = int(input("Enter number: "))
            print("Armstrong:" if is_armstrong(n) else "Not Armstrong")

        elif choice == 7:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", gcd(a, b))

        elif choice == 8:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("LCM:", lcm(a, b))

        elif choice == 9:
            n = int(input("Enter number: "))
            print("Perfect Number:" if is_perfect_number(n) else "Not Perfect Number")

        elif choice == 10:
            print("Exiting menu. Goodbye!")
            break
            
        else:
            print("Invalid choice!")

math_menu()
