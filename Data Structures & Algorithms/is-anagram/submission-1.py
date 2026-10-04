class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = {}
        for i in s:
            if i in check:
                check[i] +=1
            else:
                check[i] = 1
        for j in t:
            if check.get(j) != None:
                check[j] -=1
                if check[j] == 0:
                    check.pop(j)
            else:
                return False
        if bool(check):
            return False
        else:
            return True
