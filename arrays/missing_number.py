# Find missing number in a sequence

nums = [1, 2, 3, 4, 5, 7, 8, 9]

nums_2 = [i for i in range(32)]

sum_of_nums = sum(nums)
actual_sum = sum(i for i in range(1, 10))

missing_number = actual_sum - sum_of_nums

print(missing_number)