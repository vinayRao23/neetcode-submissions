class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        while left <= right:
            if heights[left] > heights[right]:
                temp = (right-left) * heights[right]
                if temp > max_area:
                    max_area = temp
                right -= 1
            else:
                temp = (right-left) * heights[left]
                if temp > max_area:
                    max_area = temp
                left += 1

        return max_area