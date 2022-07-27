class Solution:
    def __init__(self,arr,k) -> None:
        self.arr = arr
        self.k = k

    def findLeastNumOfUniqueInts(self) -> int:
        unique = list(set(self.arr))
        
