
#runtime O(log(n)) for each recursive iteration the number of elements to search drops
def binarySearch(nums, target):
    
    left = 0

    right = len(nums) - 1

    mid = (left + right) // 2

    if nums[mid] == target:
        return nums[mid]
    elif nums[mid] < target:
        return binarySearch(nums[mid+1:], target)
    else:
        return binarySearch(nums[:mid-1], target)


nums = [0,4,5,9,11,27,46,55,42]

found_target = binarySearch(nums, 46)
print(found_target)