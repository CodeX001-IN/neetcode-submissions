class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a={}
        
        for i in nums:
            if i not in a:
                a[i]=nums.count(i)
        b=dict(sorted(a.items(), key=lambda item: item[1], reverse=True))

        return list(b.keys())[:k] 
        
        