def findRotation(nums,n):
    index = 0
    while index<n:
        if index>0 and nums[index-1]>nums[index]:
           return index
        index+=1   
    return 0



def findRotation_optimised(nums,n):
    #We take the low and high points
    low = 0
    high=n-1
    mid = (low +high)//2
    while low <= high:
        #case 1 the segment we are looking is already sorted
        if nums[low]< nums[high]:
            return low
        next= (mid+1)%n
        prev= (mid-1+n)%n
        #case 2 , when we found the smallest point in athe array
        if nums[mid] <= nums[next] and nums[mid]<= nums[prev]:
            return mid
        #case3
        elif nums[mid]<= nums[high]: high= high=1
        #case4
        elif nums[mid]>=nums[low]: low=low+1
    return -1    

def binarySearch(nums,low,high,key):
    #base cases
    if high<low:
        return -1
    #defining middle of the array
    mid= (low+high)//2
    # aNother base case, if middle is the key
    if nums[mid]==key:
        return mid
     #Otherwise   
    if key > nums[mid]:
        return binarySearch(nums,mid+1,high,key)
    return binarySearch(nums,low,mid-1,key)


def pivotedBinarySearch(nums,n,key):

    pivot = findRotation_optimised(nums,n)

    #If there is no pivot, then the list is not sorted
    if pivot == -1 :
        return binarySearch(nums,0,len(nums)-1,key)
    
    # If we found a pivot. Compare the pivot and then search in both parts
    if nums[pivot] == key:
        return pivot
    if nums[0]<=key:
        return binarySearch(nums,0,pivot-1,key)
    return binarySearch(nums,pivot +1,len(nums)-1,key)



nums=[5, 6, 7, 1, 2, 3, 4]
n=len(nums)
