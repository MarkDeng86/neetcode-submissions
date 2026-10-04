

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        multiplier = 1

        for i in range(len(nums)):
            output[i] = multiplier
            multiplier *= nums[i]

        multiplier = 1
        for j in range(len(nums)-1, -1 , -1):
            output[j] *= multiplier
            multiplier *= nums[j]

        return output
        # n = 48
        # 1, 1, 2, 8

        # m = 48
        # 1 * 48 , 1 * 24 = 28,2*6 = 12 ,8*1 =8
