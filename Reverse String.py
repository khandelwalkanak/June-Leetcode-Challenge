# time: O(n)
# extra-space: O(1)

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(0, n//2):
            s[i], s[n-1-i] = s[n-1-i], s[i]
            
        
