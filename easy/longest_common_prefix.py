'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string ""
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        strs.sort()
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans
        
    '''
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(set(strs))==1: return strs[0]
        mem=1
        i=1
        while mem==1:
            mem=len(set([s[:i] for s in strs]))
            i+=1
        return strs[0][:i-2]
    '''
