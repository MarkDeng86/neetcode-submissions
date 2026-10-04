class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        builder = []
        
        def dfs (index, builder):
            for i in range(index, len(nums)):
                builder.append(nums[i])
                output.append(builder.copy())
                dfs(i+1,builder)
                builder.pop()
            
        output.append([])
        dfs(0,[])
        return output
        
        