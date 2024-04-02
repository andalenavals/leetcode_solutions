'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''


class Solution(object):
    def threeSum(self, nums):

	res = set()

	#1. Split nums into three lists: negative numbers, positive numbers, and zeros
	n, p, z = [], [], []
	for num in nums:
		if num > 0:
			p.append(num)
		elif num < 0: 
			n.append(num)
		else:
			z.append(num)

	#2. Create a separate set for negatives and positives for O(1) look-up times
	N, P = set(n), set(p)

	#3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
	#   i.e. (-3, 0, 3) = 0
	if z:
		for num in P:
			if -1*num in N:
				res.add((-1*num, 0, num))

	#3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
	if len(z) >= 3:
		res.add((0,0,0))

	#4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
	#   exists in the positive number set
	for i in range(len(n)):
		for j in range(i+1,len(n)):
			target = -1*(n[i]+n[j])
			if target in P:
				res.add(tuple(sorted([n[i],n[j],target])))

	#5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
	#   exists in the negative number set
	for i in range(len(p)):
		for j in range(i+1,len(p)):
			target = -1*(p[i]+p[j])
			if target in N:
				res.add(tuple(sorted([p[i],p[j],target])))

	return res

    '''
    def threeSum(self, nums):
        nums.sort()
        target=0
        fsol=set()
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                s=nums[i]+nums[j]+nums[k]
                if s==target: 
                    fsol.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1 
                elif s<target: j+=1
                else: k-=1
                    
        return fsol
    '''


    '''
    def threeSum(self, nums):
        nums.sort()
        fsol=set()
        for i,d in enumerate(nums[:-2]):
            hmap=set()
            for e in nums[i+1:]:
                comp= -d - e
                if comp in hmap:
                    fsol.add((d,comp,e))   
                hmap.add(e)
        return fsol
    '''
