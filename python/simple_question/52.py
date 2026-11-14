nums = [2, 7, 11, 15]
target = 9

seen = {}   

i = 0
while i < len(nums):
    complement = target - nums[i]

    if complement in seen:
        print([seen[complement], i])
        break

    seen[nums[i]] = i
    i += 1