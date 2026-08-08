class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow = 0
        fast = len(numbers) - 1

        for i in range(len(numbers)):
            if numbers[slow] + numbers[fast] > target:
                fast -= 1
            elif numbers[slow] + numbers[fast] < target:
                slow += 1
            else:
                return [slow + 1, fast + 1]