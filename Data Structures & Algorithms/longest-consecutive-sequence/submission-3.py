class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visit = {}
        for i in nums:
            visit[i] = 0
        
        tallestChain = 0

        print(visit.items())
        for n in range(len(nums)):
            temp = nums[n]
            counter = 0
            if visit[temp] == 1:
                continue
            while(visit.get(temp) == 0):
                visit[temp] = 1
                counter += 1
                temp = temp+1
            temp = nums[n]-1
            while(visit.get(temp) == 0):
                visit[temp] = 1
                counter += 1
                temp = temp-1
            print(visit.items())
            tallestChain = max(tallestChain,counter)
        return tallestChain
