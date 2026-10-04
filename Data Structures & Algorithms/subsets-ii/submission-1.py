class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        builder = []
        output  = []
        nums = sorted(nums)

        output.append([])
        def dfs(index,builder):
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    pass
                else:
                    builder.append(nums[i])
                    output.append(builder.copy())
                    dfs(i+1,builder)
                    builder.pop()
        dfs(0,builder)
        return output