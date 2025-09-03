def check_palindrome(str):
    i = 0
    j = len(str)-1
    while i < j:
        if str[i].lower() != str[j].lower():
            return "Not a palindrome"

        i += 1
        j -= 1

    return "Palindrome"

print(check_palindrome('hello'))

print(check_palindrome('abccba'))
