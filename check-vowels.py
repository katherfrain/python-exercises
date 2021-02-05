def is_vowel(letter):
    letter = letter.lower()
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        return True
    return False

def vowel_counter():
    
    vowelcount = 0
    word = input('Please enter a word, and I will count the vowels inside it: ')
    
    for letter in range(0, len(word)):
        if is_vowel(word[letter]):
            vowelcount = vowelcount + 1
    return vowelcount


print(vowel_counter())

