def LomutoPartition(arr):
    l=0
    h=len(arr)-1
    pivot=arr[h]
    i=l
    for j in range(l,h):
        if arr[j]<pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i=i+1
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return arr

arr=[10,80,30,90,40,50,70]
print(LomutoPartition(arr))