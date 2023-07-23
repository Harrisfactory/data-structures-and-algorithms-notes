#example
#  4,3,2,1
#  (4),3,2,1
#  4,(3),2,1 meets requirements, swap
#  3,4,(2),1 meets requirements, swap
#  3,(2),4,1 meets requirements, swap
#  2,3,4,(1) meets requirements, swap
#  2,3,(1),4 meets requirments, swap
#  2,(1),3,4 meets requirements, swap
#  1,2,3,4   complete


# compares the current num with all nums to its left, 
# if it can be swapped to its left it will be, this will continue until 
# j - 1 is less than j or reached beginning of array
def insertionSort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j-=1
    return nums


nums = [4,3,6,2,7,1,0]

result = insertionSort(nums)

print(result)

#time is O(n^2) because at worst you are cycling through n with a nested loop