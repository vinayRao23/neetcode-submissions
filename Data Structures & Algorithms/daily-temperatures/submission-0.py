class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        differences = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackIdx = stack.pop()
                differences[stackIdx] = (i - stackIdx)
            stack.append([temp, i])
        
        return differences

        