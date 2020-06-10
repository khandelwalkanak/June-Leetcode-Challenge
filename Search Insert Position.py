# time: O(log N)
# extra-space: O(1)

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        beg = 0
        end = len(nums)
        
        while end - beg:
            mid = (beg + end)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                if beg == mid:
                    return beg + 1
                
                beg = mid
                
            else:
                end = mid
        
        return 0
        
        
