
def merge_sort(arr):
    helper(arr,0,len(arr)-1)
    
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    
    return arr

def helper(A,start,end):
    # Leaf Nodes
    if start==end:
        return A
    mid = (start+end)//2
    helper(A,start,mid)
    helper(A,mid+1,end)
    i=start
    j=mid+1
    aux=[]
    while i<=mid and j<=end:
        if A[i]<=A[j]:
            aux.append(A[i])
            i=i+1
        else:
            aux.append(A[j])
            j=j+1
    while i<=mid:
        aux.append(A[i])
        i=i+1
    while j<=end:
        aux.append(A[j])
        j=j+1
    A[start:end+1]=aux
    return A
        
