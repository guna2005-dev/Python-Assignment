def question17():
    text = input("Enter word/number:")

    # Original and reversed versions
    original = text
    reversed_text = text[::-1] # reverese the string

    print("Original:", original)
    print("Reversed:", reversed_text)

    # For words, ignore case
    if original.lower() == reversed_text.lower():
        print("Result: PALINDROME")
    else:
        print("Result: NOT A PALINDROME")

#Call the function
question17()

