
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
        helper(arr,l,p-1)
        helper(arr,p+1,h)
    return arr


# def LPartition(arr,l,h):
#     pivot=arr[l]
#     i=l-1

#     #h=high
#     for j in range(l+1,h+1):
#         if arr[j]<pivot:
#             i=i+1
#             arr[i],arr[j]=arr[j],arr[i]
#             #i=i+1
#     arr[i+1],arr[h]=arr[h],arr[i+1]
#     return i+1

def HPartition(arr,low,high):
    pivot=arr[low]
    i=low-1
    j=high+1
    
    while True:
        i=i+1
        while arr[i]<=pivot:
            i=i+1
        j=j-1
        while arr[j]>pivot:
            j=j-1
        if i>=j:
            return j
        arr[i],arr[j]= arr[j],arr[i]
    

#a=[10,8,30,25,70,50,60,40,20]

#a= [1, 2, 1, 3, 5]
a=  [5, 8, 3, 9, 4, 1, 7]

print(quick_sort(a))