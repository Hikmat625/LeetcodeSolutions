class Solution:
    def sortedSquares(self, nums):
        point1 = 0
        point2 = len(nums) - 1
        ra = []
        while point1 <= point2:
            if abs(nums[point1]) <= abs(nums[point2]): 
                ra.append(nums[point2]**2)
                point2 -= 1
            else:  
                ra.append(nums[point1]**2)
                point1 += 1
        return ra[::-1]