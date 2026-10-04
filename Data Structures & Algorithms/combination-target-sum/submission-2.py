class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        builder = []
        
        def helper(builder, cur, index):
            if (cur > target):
                return
            elif (cur == target):
                output.append(builder.copy())
                return
            else:
                for i in range(index, len(nums)):
                    builder.append(nums[i])
                    helper(builder, cur+nums[i], i)
                    builder.pop()
        
       
        helper(builder, 0, 0)
        return output
            
