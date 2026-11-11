import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for i in range(len(points)):
            heapq.heappush(maxheap, [-(points[i][0]**2 + points[i][1]**2), i])
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        return [points[maxheap[i][1]] for i in range(len(maxheap))]
        