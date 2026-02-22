def question11():
    print("Choose Pattern")
    print("1. Pattern 1")
    print("2. Pattern 2")
    print("3. Pattern 3")
    print("4. Pattern 4")

    choice = int(input("Enter your choice (1-4): "))
    height = int(input("Enter height:"))

    print()

    if choice == 1:
        # Pattern 1
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end="")
            print()

    elif choice == 2:
        # Pattern 2
        for i in range(1, height + 1):
            for j in range(i):
                print(i , end="")
            print()

    elif choice == 3:
        # Pattern 3
        for i in range(height, 0, -1):
            for j in range(i, 0, -1):
                print(j, end="")
            print()

    elif choice == 4:
        # Pattern 4
        for i in range(1,height +1):
            #Increasing part
            for j in range(1, i+1):
                print(j, end="")
            #Decreasing part
            for j in range(i-1, 0, -1):
                print(j, end="")
            print()

    else:
        print("Invalid choice!")

question11()