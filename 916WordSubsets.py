from typing import Counter
import collections

class Solution:
    def wordSubsets(self, words1, words2):
        dict1 = Counter(''.join(words2))
        ra = []
        for word in words1:
            needed = True
            dict2 = Counter(list(word))
            for letter in words2:
                if dict2[letter] != dict1[letter]:
                    needed == False
            if needed : ra.append(word)
        return ra

#solution by lee
class Solution:
    def wordSubsets(self, words1, words2):
        count = collections.Counter()
        for b in words2:
            count |= collections.Counter(b)
        return [a for a in words1 if not count - Counter(a)]


a = Solution()
print(a.wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode",'a'], words2 = ["l","e"]))