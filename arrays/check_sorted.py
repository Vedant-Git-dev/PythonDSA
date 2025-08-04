nums = [1, 2, 3, 4, 3, 5, 6, 7, 8, 9, 10]

def check_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False

    return True

print(check_sorted(nums))