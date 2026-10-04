class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        builder = ""

        def helper(left, right ,total, builder):
            if right > left or left > total or right > total:
                return 
            if left == total and right == total:
                res.append(builder)
            builder+="("
            helper(left+1, right, total, builder)
            builder= builder[:-1]
            builder+=")"
            helper(left, right+1, total, builder)
            builder= builder[:-1]

        builder+="("
        helper(1,0,n,builder)
        return res
