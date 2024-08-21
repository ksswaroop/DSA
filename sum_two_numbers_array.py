"""Given an array and a target number, find the indices of the two values from the array that sum up to the given target number.
"""
numbers= [5, 3, 10, 45, 1]
target=6

def two_sum(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    #numbers=quick_sort(numbers)
    print(numbers)
    left=0
    right=len(numbers)-1
    while left<right:
        sum1=numbers[left]+numbers[right]
        if sum1==target:
            return [left,right]
        elif sum1<target:
            left=left+1
        else:
            right=right-1
    return [-1,-1]
            

        
print(two_sum(numbers,target))
