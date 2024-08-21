
def quick_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    l=0
    h=len(arr)-1
    return helper(arr,l,h)

def helper(arr,l,h):
    if l<h:
        p=HPartition(arr,l,h)
        helper(arr,l,p)
        helper(arr,p+1,h)
    return arr

def HPartition(arr,low,high):
    pivot=arr[low]
    i=low-1
    j=high+1
    
    while True:
        i=i+1
        while arr[i]<pivot:
            i=i+1
        j=j-1
        while arr[j]>pivot:
            j=j-1
        if i>=j:
            return j
        arr[i],arr[j]= arr[j],arr[i]
    
numbers= [5, 3, 10, 45, 1]

print(quick_sort(numbers))