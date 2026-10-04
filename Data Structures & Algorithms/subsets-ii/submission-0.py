class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        builder = []
        output  = []
        nums = sorted(nums)
        unique = set()

        output.append([])
        def dfs(index,builder):
            for i in range(index, len(nums)):
                builder.append(nums[i])
                if tuple(builder) in unique:
                    pass
                else:
                    output.append(builder.copy())
                    unique.add(tuple(builder))
                dfs(i+1,builder)
                builder.pop()
        dfs(0,builder)
        return output