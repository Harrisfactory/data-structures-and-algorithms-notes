#benefits of iterative is that you retain the original index

#Time complexity: O(log(n)) each iteration the elements being iterated on drop

def binarySearch(nums, target):
    
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        #found, return index
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1
    
    #not found
    return -1


    

    






nums = [0,4,5,9,11,27,46,55,42]

print(binarySearch(nums, 46))