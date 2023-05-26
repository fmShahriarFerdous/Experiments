def twoSum(nums, target):
    length = len(nums)
    outpt = []
    for i in range(0,length):
        for j in range(i+1,length):
            if(nums[i]+nums[j]==target):
                outpt.append(i)
                outpt.append(j)
    return outpt

nums = [3,2,4]
target = 6
outpt = twoSum(nums,target)
print(outpt)