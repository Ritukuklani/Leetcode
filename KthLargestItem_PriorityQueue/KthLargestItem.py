class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.heap_s, self.k = [], k
        for num in nums:
            heapq.heappush(self.heap_s, num)
            if len(self.heap_s)>self.k: heapq.heappop(self.heap_s)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap_s, val)
        if len(self.heap_s)>self.k: heapq.heappop(self.heap_s)
        return self.heap_s[0]
        