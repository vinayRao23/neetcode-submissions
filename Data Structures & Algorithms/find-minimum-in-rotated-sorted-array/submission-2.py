class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        middle = 0

        while left < right:
            middle = left + ((right-left) // 2)

            if middle > 0 and nums[middle] < nums[middle - 1]:
                return nums[middle]

            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        
        return nums[left]