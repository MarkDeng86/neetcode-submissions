class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        builder = []
        visited = [False] * len(nums)
        res = []
        def dfs(builder, visited):
            for i in range(len(nums)):
                if len(builder) == len(nums):
                    res.append(builder.copy())
                    return 
                if not visited[i]:
                    builder.append(nums[i])
                    print("append: {}".format(nums[i]))
                    visited[i] = True
                    dfs(builder, visited)
                    builder.pop()
                    visited[i] = False
        
        dfs(builder,visited)
        return res
            