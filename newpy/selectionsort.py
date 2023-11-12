def sort(nums):
    for i in range(4):
        minpos = i
        for j in range(i,5):
            if nums[j] < nums[minpos]:
                minpos = j

            temp = nums[i]
            nums[i]=nums[minpos]
            nums[minpos]=temp
        # print(nums)

nums = [5,3,2,6,7]
sort(nums)

print(nums)