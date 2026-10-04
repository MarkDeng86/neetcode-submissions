class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i in range(len(nums)):
            if check.get(nums[i]) != None:
                return [check.get(nums[i]), i]
            else:
                check[target - nums[i]] = i
        return None
