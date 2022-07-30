from typing import Counter


class Solution:
    def containsDuplicate(self, nums):
        a = {}
        for num in nums:
            if num in a:
                return True
            else: a[num] = str(num)
        return False

a = Solution()

print(a.containsDuplicate([1,2,3]))