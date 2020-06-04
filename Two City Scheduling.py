# time: O(N)
# space: O(N)

class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        ans = 0
        
        # send all people to A
        for cost in costs:
            ans += cost[0]
            
        # find cost of each person of, shitfing from A to B
        # i.e. cost[i][1] - cost[i][0]
        
        shift_costs = []
        
        for cost in costs:
            shift_costs.append(cost[1]-cost[0])
            
        # find N people who have minimum shiftings costs
        shift_costs.sort()
        n = len(costs)//2
        
        n_min_shifts = sum(shift_costs[0:n])
        
        # shift cheapest N people to B
        ans += n_min_shifts
        return ans
        
