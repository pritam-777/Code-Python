def Max_min(arr,n):
    max = arr[0]
    min = arr[0]
    for i in range(1,n):
        if(arr[i]>max):
            max=arr[i]
        if(arr[i]<min):

            min=arr[i]
    return max,min

if __name__=='__main__':
    arr = [10, 25, 120, 1, 40, 82]
    n = len(arr)
    print(Max_min(arr, n))





