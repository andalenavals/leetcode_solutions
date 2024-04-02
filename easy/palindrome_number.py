'''
Given an integer x, return true if x is a palindrome, and false otherwise.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0: 
            return False
        reversed=0
        temp=x
        while temp>0:
            temp,d=divmod(temp,10)
            reversed=reversed*10+d
        return reversed==x
        
    '''
    def isPalindrome(self, x):
        return str(x)==str(x)[::-1]
    '''
