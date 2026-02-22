def question9():
    age= int(input("Enter age:"))
    day = input("Enter day of week:").lower()
    tickets = int(input("Enter number of tickets:"))

    #Age-based pricing
    if age < 3:
        base_price = 0
        category = "Free"
    elif age <= 12:
        base_price = 150
        category = "Child"
    elif age <= 59:
        base_price = 300
        category = "Adult"
    else:
        base_price = 200
        category = "Senior"

    total_base = base_price * tickets

    #Day-based discount

    if day in ["friday", "saturday", "sunday"]:
        discount = 0.10 * total_base *0.20
    else:
        discount = 0

    final_amount = total_base - discount

    print("\n=== TICKET BILL ===")
    print("Category:", category)
    print("Base price per ticket: ₹", base_price)
    print("Total base amount: ₹", total_base)
    print("Discount: ₹", discount)
    print("Final amount: ₹", final_amount)

question9()
