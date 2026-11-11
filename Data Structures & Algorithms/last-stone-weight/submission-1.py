import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            if abs(a) == abs(b):
                heapq.heappush(stones, 0)
            elif abs(a) > abs(b):
                difference = abs(a) - abs(b)
                heapq.heappush(stones, -difference)
            else:
                difference = abs(b) - abs(a)
                heapq.heappush(stones, -difference)
        
        return -stones[0]