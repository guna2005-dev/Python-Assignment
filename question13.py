def question13():
    count = int(input("How many numbers?"))

    total = 0
    numbers = []
     
    for i in range(1, count + 1):
        num = float(input(f"Enter number {i}:"))
        numbers.append(num)
        total += num

    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)

    print("\n=== RESULTS ===")
    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)

question13()
