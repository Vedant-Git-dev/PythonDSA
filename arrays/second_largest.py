# Find the second-largest element

nums = [12, 32, 43, 12, 76, 55]

# initializing both with random small value
first_largest = float('-inf')
second_largest = float('-inf')

for num in nums:
    if num > first_largest:
        second_largest = first_largest # assigns first largest element as second largest element
        first_largest = num # updates first largest element

    # handling middle values between second and first largest numbers
    elif num > second_largest and num != first_largest:
        second_largest = num

