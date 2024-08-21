def threeSum(nums): # -> List[List[int]]:
    nums.sort()
    aux=[]
    n=len(nums)
    for i in range(n):
        low=i+1
        high=n-1
        while high>=0 and low<high:
            csum=nums[i]+nums[low]+nums[high]
            if csum==0:
                aux1=[]
                aux1.extend([nums[i],nums[low],nums[high]])
                if aux1 not in aux:
                    aux.append(aux1)
                low=low+1
                high=high-1
            elif csum<0:
                low=low+1
            else:
                high=high-1

    return aux


nums=[3,0,-2,-1,1,2]

print(threeSum(nums))