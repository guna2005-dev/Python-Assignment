def count_words(text):
    return len(text.split())

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def count_consonants(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char.isalpha() and char not in vowels)

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in text if char not in vowels)

def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq


def longest_word(text):
    words = text.split()
    longest = max(words, key=len)
    return longest

def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))
    print("Palindrome:", "Yes" if is_palindrome(text) else "No")
    print("Without vowels:", remove_vowels(text))

    lw = longest_word(text)
    print("Longest word:", lw, f"({len(lw)} letters)")
    
    freq = word_frequency(text)
    print("Word frequency:")
    for word, count in freq.items():
        print(f"  {word}: {count}")

# main Program
text = input("Enter text: ")
analyze_text(text)
