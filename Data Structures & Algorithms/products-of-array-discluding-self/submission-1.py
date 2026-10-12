class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        newList = [0] * len(nums)
        if 0 in nums:
            if nums.count(0) > 1:
                return [0] * len(nums)
            
            for num in nums:
                if num != 0:
                    prod *= num
            
            for i in range(len(nums)):
                if nums[i] != 0:
                    newList[i] = 0
                else:
                    newList[i] = prod
            
            return newList
        
        else:
            for num in nums:
                prod *= num
            
            for i in range(len(nums)):
                newList[i] = prod // nums[i]
            
            return newList
        

        