class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        newList = []
        while k > 0:
            mostCommonKey = max(hashmap, key=hashmap.get)
            newList.append(mostCommonKey)
            del hashmap[mostCommonKey]
            k -= 1

        return newList