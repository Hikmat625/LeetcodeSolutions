class Solution:
    def minimumOperations(self, nums) -> int:
        def getSmallest(nums):
            for i in nums:
                if i > 0 : return i
        
        nums = sorted(nums)
        counter = 0
        while nums[-1]>0:
            num = getSmallest(nums)
            for i , _ in enumerate(nums):
                nums[i] = nums[i] - num
            counter += 1
        return counter

a = Solution()
print(a.minimumOperations([1,5,0,3,5]))    