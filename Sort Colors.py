class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums)-1
        i = 0
        
        while (p2 >= 0) and (nums[p2] == 2):
            p2 -= 1
        
        while p2-i+1 > 0:
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
                
            elif nums[i] == 2:
                nums[p2], nums[i] = nums[i], nums[p2]
                p2 -= 1
                
                while (p2 >= 0) and (nums[p2] == 2):
                    p2 -= 1
                    
                if nums[i] == 0:
                    nums[p0], nums[i] = nums[i], nums[p0]
                    p0 += 1 
            
            i += 1
                
        
