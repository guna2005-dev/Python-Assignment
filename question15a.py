def question15():
    # Part 1: Check a single number for primality
    num = int(input("Enter a number: "))

    if num <= 1:
        print(f"{num} is NOT a prime number")
    elif num == 2:
        print("2 is a PRIME number")
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} is a PRIME number")
        else:
            print(f"{num} is NOT a prime number")

    # Part 2: Find all prime numbers in a given range
    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    primes = []
    for n in range(max(2, start), end + 1):
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(str(n))

    print("Prime numbers:", ", ".join(primes))

# Call the function
question15()