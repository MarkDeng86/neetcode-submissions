class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(heights)-1
        width = right - left
        
        while(left < right):
            width = right - left
            check = width * min(heights[left],heights[right])
            maxArea = max(maxArea, check)

            if (heights[left]> heights[right]):
                prev = heights[right]
                while(left < right and heights[right] <= prev):
                    right -= 1
            else:
                prev = heights[left]
                while(left < right and heights[left] <= prev):
                    left += 1
        return maxArea