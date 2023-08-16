#GIST: 
    #splits list down the middle, swaps based on order, 
    #then merges the now swapped sub chunks
    #repeat until full list is in order

#DEFINITION
    #merge sort is a recursive algorithm that continuously splits the array in half until 
    #it cannot be further divided ie the array has only one element left (an array with one 
    #element is always sorted). Then the sorted subarrays are merged into one sorted array.

#example:
    #5,3,1,2,6,4,9
    #split array    5,3,1    2,6,4,9
    #split array left   5  3,1   
    #split array 

def mergeSort(nums):
    if len(nums) > 1:
        #find the middle of the array
        mid = len(nums) // 2
        ##divide array into two halves
        left = nums[:mid]
        right = nums[mid:]
        #sort left half
        print("left " + str(left))
        mergeSort(left)
        #sort right half
        print("right " + str(right))
        mergeSort(right)
        i, j, k = 0, 0, 0
        while i  < len(left) and j < len(right):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1
        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1


nums = [5,3,1,2,6,4,9]

temp = [3,1]

print("=====sorting array using merge sort=====")
print("Before sort: " + str(nums))
mergeSort(nums)
print("After sort: " + str(nums))
print("========================================")