class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if k == 0: return
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums

#https://leetcode.com/problems/rotate-array/discuss/269948/4-solutions-in-python-(From-easy-to-hard)
#better solution than mine