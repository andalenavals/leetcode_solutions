def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
        
    res=100000
    sol=0
    
    nums.sort()
    pos=[]
    neg=[]
    zer=[]
    for e in nums:
        if e>0: pos.append(e)
        elif e<0: neg.append(e) 
        zer.append(e)
        
    ## Solutions involving zeros
    if (len(zer)>=3)&(target==0): return target 
    if len(zer)>=2:
        ind,aux=closest(neg+pos, target)
        res=abs(target-aux)
        if res==0: return aux
        sol=aux
    
    if len(zer)>=1:
        # this is an implementation for the twosumclosest
        if target>0: 
            ## Two positives
            i,cp=closest(pos, target)
            for j in range(i):
                ind,aux=closest(pos[j+1:i+1], target-pos[j])
                if abs(target-aux-pos[j])<res:
                    res=abs(target-aux-pos[j])
                    sol=aux+pos[j]
                if res==0: return sol
            ## One positive and one negative
    
    return sol
    
    
       

def closest(nums, target):
    #return the closest 
    #assuming nums is already sorted
    k=len(nums)-1
    i=0
    left=target-nums[i]
    right=target-nums[k]
    if right>=0: 
        return k,nums[k]
    elif left<0:
        return i,nums[i]

    while i+1<k:
        left=target-nums[i]
        right=target-nums[k]
        if left==0: return i,target
        if right==0: return k,target
        if right>0: 
            i=k
            k=oldk
        elif left<0:
            k=i
            i=oldi
        if -right<left:
            oldi=i
            i+=int(0.5*(k-i))
            res=-right
            val=nums[k]
        else:
            oldk=k
            k-=int(0.5*(k-i))
            res=left
            val=nums[i]

    left=target-nums[i]
    right=target-nums[k]
    if left==0: return i,target
    if right==0: return k,target
    if -right<left:
        res=-right
        val=nums[k]
        ind=k
    else:
        res=left
        val=nums[i]
        ind=i
    return ind,val

    
print(threeSumClosest([-9,0,0,1,4,5,7,9,16], 15))
#print(closest([-9,1,4,5,7,8], -1))
