from typing import Counter
#not finished yet

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ht = {}
        for i , s in enumerate(s1):
            ht[s] = i
        left = 0
        right = len(s1)
        while right < len(s2):
            inclusive = True
            for i in range(left,right):
                if s2[i] not in ht:
                    left = i
                    right = i + len(s1)
                    inclusive = False
            if inclusive : return True
                
        return False
Counter()
a = Solution()
print(a.checkInclusion('ac','abafafa'))