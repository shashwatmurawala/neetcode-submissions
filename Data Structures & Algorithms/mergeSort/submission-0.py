# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if(len(pairs) <= 1):
            return pairs
        
        left = self.mergeSort(pairs[:len(pairs)//2])
        right = self.mergeSort(pairs[len(pairs)//2:])
        op = []
        l = 0
        r = 0
        while l < len(left) and r < len(right):
            if(left[l].key <= right[r].key):
                op.append(left[l])
                l+= 1
            else:
                op.append(right[r])
                r+= 1
        while l < len(left):
            op.append(left[l])
            l+= 1
        while r < len(right):
            op.append(right[r])
            r+= 1
        return op