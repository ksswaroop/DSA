def bubble_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    for i in range(len(arr)-1):
        for red in range(len(arr)-1,i,-1):
            if arr[red-1]>arr[red]:
                temp=arr[red]
                arr[red]=arr[red-1]
                arr[red-1]=temp
    return arr
