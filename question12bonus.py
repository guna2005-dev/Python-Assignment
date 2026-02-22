def full_table():
    print("\n=== FULL MULTIPLICATION TABLE (1-10)===\n")

    for i in range(1, 11):
        for j in range(1, 11):
            print(f"{i*j:4}", end="")
        print()

full_table()
