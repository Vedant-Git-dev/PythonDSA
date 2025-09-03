def remove_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for ch in word:
        if ch in vowels:
            word = word.replace(ch, '')

    return word

print(remove_vowel('hello World'))