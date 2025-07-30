# find maximum and minimum element in a list without min() and max()

nums = [42, 32, 43, 65, 87, 38, 76]

min_value = max_value = nums[0]

for num in nums:
    if num < min_value:
        min_value = num
    if num > max_value:
        max_value = num

print("Minimum value :", min_value)
print("Maximum value :", max_value)