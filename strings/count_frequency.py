def count_occurance(str, ch):
    count = 0
    for char in str:
        if ch == char:
            count += 1

    return count


print(count_occurance('hello world', "l"))