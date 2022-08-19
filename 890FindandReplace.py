class Solution:
    def findAndReplacePattern(self, words, pattern):
        def encrypt(word):
            a = {}
            num = 0
            code = ''
            for i in word:
                if i not in a:
                    a[i] = str(num)
                    num += 1
                code += a[i]
            return code
        return encrypt(pattern)
a = Solution()

print(a.findAndReplacePattern([],['abba']))                