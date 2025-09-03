def prefix(word_1, word_2):
    prefix = ""

    for l1, l2 in zip(word_1, word_2):
        if l1 == l2:
            prefix += l1

    return prefix

print(prefix("vedant", "vedvani"))
print(prefix("car", "carpet"))