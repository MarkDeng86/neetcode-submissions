class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxRob = nums[0]
        lst = nums
        counter = 0
        
        for i in range(2,len(nums)):
            if (i == 2):
                lst[i] += lst[i-2]
            else:
                lst[i] += max(lst[i-2],lst[i-3])
        return max(lst[len(nums)-1], lst[len(nums)-2])
            
        