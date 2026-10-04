class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        indx1 = 0
        indx2 = len(numbers)-1
        val = numbers[indx1] + numbers[indx2]
        while(val != target):
            if(val < target):
                indx1 += 1
            elif (val > target):
                indx2 -=1
            val = numbers[indx1] + numbers[indx2]
        return [indx1+1,indx2+1]