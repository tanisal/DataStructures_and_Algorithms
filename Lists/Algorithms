
def merge_sort(arr): # Time Complexityt on O(nlogn)
    if len(arr)>1:
        #Middle of the array
        mid = len(arr)//2

        #Creating the two subarrays 
        left = arr[:mid]
        right = arr[mid:]

        #Recursing through both of them
        merge_sort(left)
        merge_sort(right)

        # Iteraters for traversing the two halfs
        i=0
        j=0

        #Iterator for traversing the main array
        k=0

        while i < len(left) and j < len(right):
            #If left side is smaller than the right then add it to the main list
            if left[i] < right[j]:
                arr[k]=left[i]
                #Iterate over
                i+=1

            else:
                arr[k]=right[j]
                j+=1
        #Iterate over the main list        
            k+=1

        #For tall the values we did not catch
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1

