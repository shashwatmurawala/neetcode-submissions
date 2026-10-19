# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs: List[Pair], s: int, e: int) -> None:
        if e - s + 1 <= 1:
            return
        
        piv = pairs[e]
        left = s
        for i in range(s, e):
            if pairs[i].key < piv.key:
                pairs[i], pairs[left] = pairs[left], pairs[i]
                left += 1
        
        pairs[e], pairs[left] = pairs[left], pairs[e]
        self.quickSortHelper(pairs, s, left - 1)

        # Quick sort right side
        self.quickSortHelper(pairs, left + 1, e)
        
