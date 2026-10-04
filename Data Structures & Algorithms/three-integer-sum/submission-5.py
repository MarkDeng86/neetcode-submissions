class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = sorted(nums)
        print(lst)
        output = []
        skipFlag = False
        for target in range(len(lst)-2):
            if target > 0 and lst[target] == lst[target-1]:
                continue
            indx1 = target+1
            indx2 = len(lst)-1
            check = lst[target] * -1
            while (indx1 < indx2):
                if (lst[indx1] + lst[indx2] == check):
                    output.append([lst[target],lst[indx1],lst[indx2]])
                    while(indx1 < indx2 and lst[indx1+1] == lst[indx1]):
                        indx1+=1
                    indx1 +=1
                elif (lst[indx1] + lst[indx2] > check):
                    indx2 -= 1
                elif (lst[indx1] + lst[indx2] < check):
                    indx1 += 1
            
        return output

        