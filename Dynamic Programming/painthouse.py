def minCost(self, costs):   # input type: List[List[int]], return type: int

# Recursive approach using memoization
        # def paint_cost(n, color):
        #     total_cost = costs[n][color]
        #     if (n, color) in self.memo:
        #         return self.memo[(n, color)]
        #     if len(costs)-1 == n:
        #         pass
        #     elif color==0:
        #         total_cost+=min(paint_cost(n+1, 1), paint_cost(n+1, 2))
        #     elif color==1:
        #         total_cost+=min(paint_cost(n+1, 0), paint_cost(n+1, 2))
        #     elif color==2:
        #         total_cost+=min(paint_cost(n+1, 1), paint_cost(n+1, 0))
        #     self.memo[(n, color)] = total_cost
        #     return total_cost
        # self.memo = {}
        # if costs==[]:
        #     return 0
        # return min(paint_cost(0, 0), paint_cost(0,1), paint_cost(0,2))

# Using dynamic programming
        if len(costs)==0:
            return 0
        prev_row = costs[0]
        for n in range(1, len(costs)):
            current_row = costs[n]
            current_row[0] += min(prev_row[1], prev_row[2])
            current_row[1] += min(prev_row[0], prev_row[2])
            current_row[2] += min(prev_row[0], prev_row[1])
            prev_row = current_row
        return min(prev_row)