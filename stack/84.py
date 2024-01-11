class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return heights[0]

        result = 0
        stack = list()

        for index , height in enumerate(heights):
            start = index
            
            while start and stack[-1][1] > height:
                i , h = stack.pop()
                result = max(result , (index-i)*h)
                start = i
            stack.append((start , height))

        for index , height in stack:
            result = max(result , (len(heights)-index)*height)

        return result