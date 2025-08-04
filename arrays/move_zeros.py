# moving all zeros to the end

nums = [21, 0, 98, 0, 7, 9, 0]

for i in range(len(nums)):
    if nums[i] == 0:
        nums.append(nums[i])
        nums.remove(0)

print(nums)