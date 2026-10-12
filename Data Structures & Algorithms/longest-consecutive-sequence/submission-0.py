class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        hashmap = {}

        for num in nums:
            if (num-1) in nums:
                continue
            hashmap[num] = 1
        
        for key in hashmap:
            curr = key
            temp = 1
            while (curr + 1) in nums:
                temp += 1
                curr += 1
            
            if temp > count:
                count = temp
        
        return count
        
        


    