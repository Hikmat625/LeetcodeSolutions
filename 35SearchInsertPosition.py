class Solution:
    def search(self, nums, target: int) -> int:
        left = 0
        right = len(nums)
        while right - left != 1:
            index = (right + left)//2
            if target == nums[index] : return index 
            if target > nums[index] :
                left = index
            else: right = index
        return left + 1 

a = Solution()
print(a.search([1,3,5,6],5))