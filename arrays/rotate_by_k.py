# left rotating array by kth position

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

nums = [1, 2, 3, 4, 5]
k = 3

reverse(nums, 0, k - 1) # reversing first k elements
reverse(nums, k, len(nums) - 1) #revsersing remaining elements
reverse(nums, 0, len(nums) - 1) #reversing entire array

print("Left rotation :", nums)

# right rotating array by kth position

nums = [1, 2, 3, 4, 5]
reverse(nums, 0, len(nums) - 1) #reversing entire array
reverse(nums, 0, k - 1) # reversing first k elements
reverse(nums, k, len(nums) - 1) #revsersing remaining elements

print("Right rotation :", nums)