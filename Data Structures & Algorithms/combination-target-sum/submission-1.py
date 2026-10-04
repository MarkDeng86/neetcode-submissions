class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        builder = []
        def dfs(index, cur, total):
            if total == target:
                output.append(cur.copy())
                return
            elif index >= len(nums) or total > target:
                return
            else:
                cur.append(nums[index])
                dfs(index, cur, total+nums[index])
                cur.pop()
                dfs(index+1, cur, total)
        dfs(0,builder,0)
        return output
            
