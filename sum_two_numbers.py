
def pair_sum_sorted_array(numbers, target):
    """
    Args:
     numbers(list_int32)
     target(int32)
    Returns:
     list_int32
    """
    # Write your code here.
    aux=[]
    n=len(numbers)
    for i in range(n):
        for j in range(i+1,n):
            if numbers[i]+numbers[j]==target:
                aux.extend([i,j])
                break
    if not aux:
        aux.extend([-1,-1])
    return aux


numbers= [1, 2, 3, 5, 10]
target= 7

print(pair_sum_sorted_array(numbers,target))