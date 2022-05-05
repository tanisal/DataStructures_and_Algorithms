def findRotation(nums):
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





A=[6,7,8,9,1,2,3,4,5]

findRotation_optimised(A,9)