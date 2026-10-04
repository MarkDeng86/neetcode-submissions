class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for i in nums:
            numMap[i] = 1 + numMap.get(i,0)
        numMap = dict(sorted(numMap.items(), key=lambda item: item[1], reverse=True))
        return list(numMap.keys())[:k]
