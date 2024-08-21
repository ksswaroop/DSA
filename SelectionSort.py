def selection_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    for i in range(0,len(arr)):
        minval=arr[i]
        minindex=i
        for j in range(i,len(arr)):
            if arr[j]<minval:
                minval=arr[j]
                in_val=arr[i]
                arr[i]=minval
                arr[j]=in_val
                minindex=j
    return arr
