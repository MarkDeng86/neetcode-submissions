import copy
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def helper(nums, target, result, builder, cur, index):
            if (cur > target):
                return
            elif (cur == target):
                result.append(copy.deepcopy(builder))
                return
            else:
                for i in range(index, len(nums)):
                    builder.append(nums[i])
                    helper(nums, target, result, builder, cur+nums[i], i)
                    builder.pop()
        
        output = []
        builder = []
        helper(nums, target, output, builder, 0, 0)
        return output
    
    
                