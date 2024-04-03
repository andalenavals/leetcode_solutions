'''
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty subarray of nums, or return -1 if no special subarray exists.

A sub array cannot pop elements, i.e, you can move the partheses only but not the members
'''

'''
def minimumSubarrayLength(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort()
    
    # see if there is a size one solution
    if nums[-1]>=k: return 1
    
    # elements of subs array must be lower than k
    b=list(bin(k)[::-1][-2])
    keyvalues=[]
    for i,e in enumerate(b):
        if e=='1':keyvalues.append(2**i)
        
    if len(keyvalues)==2:
        flag=True
        for k in keyvalues:
            flag&=(k in nums)
        if flag: return 2
'''

def minimumSubarrayLength(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    
    i=1
    while i<=len(nums):
        for j in range(len(nums)-i+1):
            res=or_list(nums[j:i+j])
            #print(i, res)
            if res>=k: return i
        i+=1
    return -1
    

def or_list(arr):
    res=0
    for e in arr:
        res|=e
    return res   
            


def tests():
    assert minimumSubarrayLength([32,2,24,1],35)==3
    assert minimumSubarrayLength([1,2,3],1)==1
    assert minimumSubarrayLength([2,1,8],10)==3
    assert minimumSubarrayLength([1,2],0)==1

print(minimumSubarrayLength([16,1,2,20,32],45))
#tests()
