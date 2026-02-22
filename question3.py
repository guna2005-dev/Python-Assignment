def question3():
    sentence = input ("Enter a sentence:")

    print("\nOriginal:", sentence)
    print("Characters (with spaces):", len(sentence))
    print("Characters (without spaces):", len(sentence.replace(" ", "")))
    
    words = sentence.split()
    print("Words:", len(words))

    print ("UPPERCASE:", sentence.upper())
    print("lowercase:", sentence.lower())
    print("Title Case:", sentence.title())

    print("First word:", words[0])
    print("Last word:", words[-1])
          
    print("Reversed:", sentence[::-1])
question3()   
        