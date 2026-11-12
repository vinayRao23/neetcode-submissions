import heapq
from collections import Counter
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = dict(Counter(tasks))
        time = 0
        queue = deque()
        maxheap = []
        for val in frequencies.values():
            heapq.heappush(maxheap, -val)
        heapq.heapify(maxheap)

        while maxheap or queue:
            time += 1

            if maxheap:
                num = heapq.heappop(maxheap) + 1
                if num != 0:
                    queue.append((num, time+n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(maxheap, queue.popleft()[0])
        
        return time

            
        
        
        