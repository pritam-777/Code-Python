def BinarySearch(arr,first,last,SerachElement):
    while first<=last :
        mid = first + (last - first)/2
        if arr[mid] == SerachElement :
            return mid
        elif arr[mid]< SerachElement :
            first = mid +1

        else:
            last = mid -1
        return -1


arr  = [10,20,25,37,45,78,82,101]
x = 82
result = BinarySearch(arr,0,len(arr)-1,x)
print(result+1)