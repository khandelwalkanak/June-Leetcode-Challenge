from random import randint

class Solution(object):

    def __init__(self, w):
        """
	time: O(N)
	extra-space: O(N)
        :type w: List[int]
        """
        self.presum = [0]*len(w)
        
        for i, wi in enumerate(w[:-1]):
            self.presum[i+1] = self.presum[i] + wi
        
        self.totl = self.presum[len(w)-1] + w[len(w)-1]

    def pickIndex(self):
        """
	time: O(logN)
	extra-space: O(1)
        :rtype: int
        """
        rand = randint(0, self.totl-1)
        
        beg = 0
        end = len(self.presum)
        
        while True:
            mid = (beg + end)//2
            
            if self.presum[mid] == rand: 
                return mid
        
            if self.presum[mid] < rand:
                if beg == mid:
                    return beg
                
                beg = mid
            
            else:
                end = mid
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
