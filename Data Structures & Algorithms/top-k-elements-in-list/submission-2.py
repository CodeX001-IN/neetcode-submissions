from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        sorted_nums = [items[0]for items in count.most_common(k)]
        return sorted_nums