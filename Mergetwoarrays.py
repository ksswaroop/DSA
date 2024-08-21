
def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    n=len(second)
    s_n=len(first)
    i=0
    while i<s_n:
        second[s_n+i]=first[i]
        i=i+1
    print(second)
    return QuickSort(second)


def QuickSort(arr):
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
        p=Partition(arr,l,h)
        helper(arr,l,p)
        helper(arr,p+1,h)
    return arr

def Partition(arr,low,high):
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


first= [1, 3, 5]
second=[2, 4, 6, 0, 0, 0]

print(merge_one_into_another(first, second))