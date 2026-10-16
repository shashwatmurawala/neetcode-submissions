# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return []
        op = []
        op.append(pairs[:])
        for i in range(1, len(pairs)):
            j = i - 1
            tempi = i
            while tempi > 0 and pairs[j].key > pairs[tempi].key:
                temp = pairs[tempi]
                pairs[tempi] = pairs[j]
                pairs[j] = temp
                tempi -= 1
                j -= 1
            op.append(pairs[:])
            
        return op

