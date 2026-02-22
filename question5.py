def question5():
    total_bill = float(input("Enter total bill:"))
    people = int (input("Number of people:"))
    tax_percent = float(input("Tax percentage:"))
    tip_percent = float(input("Tip percentage:"))

    tax_amount = total_bill * (tax_percent / 100)
    after_tax = total_bill + tax_amount
    tip_amount = after_tax * (tip_percent / 100)
    final_total = after_tax + tip_amount
    per_person = final_total / people
    
    print("\n=== BILL BREAKDOWN ===")
    print(f"Subtotal:    ₹{total_bill:.2f}") 
    print(f"Tax ({tax_percent}%): ₹{tax_amount:.2f}")
    print(f"After Tax:   ₹{after_tax:.2f}")
    print(f"Tip ({tip_percent}%): ₹{tip_amount:.2f}")
    print(f"Final Total: ₹{final_total:.2f}")
    print(f"Per Person:  ₹{per_person:.2f}")

question5()

