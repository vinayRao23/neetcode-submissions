class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        matrix = []

        for i in range(len(nums)):
            slow = i + 1
            fast = len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while slow < fast:
                if nums[i] + nums[slow] + nums[fast] == 0:
                    matrix.append([nums[i], nums[slow], nums[fast]])
                    slow += 1
                    fast -= 1
                    while slow < fast and nums[slow] == nums[slow-1]:
                        slow += 1
                elif nums[i] + nums[slow] + nums[fast] > 0:
                    fast -= 1
                else:
                    slow += 1

        return matrix