# time: O(N^2)
# extra-space: O(N)

class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        if n < 2:
            return nums
        
        nums.sort()
        
        dp = [1]*n
        links = [None]*n
        
        for i in range(1, n):
            dp_max = 0
            dp_max_i = None
            
            for j in range(0, i):
                if nums[i] % nums[j]:
                    continue
                
                if dp[j] > dp_max:
                    dp_max = dp[j]
                    dp_max_i = j
            
            dp[i] = dp_max + 1
            links[i] = dp_max_i
            
        i = dp.index(max(dp))
        ans = [nums[i]]
        
        while links[i] is not None:
            i = links[i]
            ans.append(nums[i])
            
        return ans
