from collections import defaultdict

def two_sum(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    dict1=defaultdict(list)
    for i in range(len(numbers)):
        dict1[numbers[i]].append(i)
    #print(dict1)
    #print(numbers)
    Quicksort(numbers)
    low=0
    high=len(numbers)-1
    
    while low<high:
        if numbers[low]+numbers[high]==target:
            #aux.extend([numbers[low],numbers[high]])
            if numbers[low]==numbers[high]:
                if len(dict1[numbers[low]])>1:
                    return [dict1[numbers[low]][0],dict1[numbers[high]][1]]
            else:
                return [dict1[numbers[low]],dict1[numbers[high]]]
        elif numbers[low]+numbers[high]<target:
            low=low+1
        elif numbers[low]+numbers[high]>target:
            high=high-1
    return [-1,-1]

def Quicksort(arr):
    low=0
    high=len(arr)-1
    return helper(arr,low,high)


def helper(arr,low,high):
    if low<high:
        p=Partition(arr,low,high)
        helper(arr,low,p)
        helper(arr,p+1,high)

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
        arr[i],arr[j]=arr[j],arr[i]



dict1={5:1,5:2,5:3,5:4,6:2}
print(dict1[5])



from collections import defaultdict
numbers=[5,5,6,5,7,5,5]

dict1=defaultdict(list)
for i in range(len(numbers)):
    dict1[numbers[i]].append(i)
print(dict1)