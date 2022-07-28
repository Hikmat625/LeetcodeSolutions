# pythonastic solution
class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        a = [i[::-1] for i in a]
        s = ' '.join(a)
        return s