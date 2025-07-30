# Reverse an array

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

left = 0
right = len(nums) - 1

print("original array :", nums)

while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1

print("reversed array :", nums)