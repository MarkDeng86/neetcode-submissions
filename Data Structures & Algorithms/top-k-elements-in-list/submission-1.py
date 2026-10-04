class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for i in nums:
            if numMap.get(i) is None:
                numMap[i] = 1
            else:
                numMap[i] += 1
        numMap = dict(sorted(numMap.items(), key=lambda item: item[1], reverse=True))
        return list(numMap.keys())[:k]
