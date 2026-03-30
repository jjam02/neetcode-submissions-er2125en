class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        result = []
        for num in nums:
            freq[num] = freq.get(num,0)+1
        print(freq)
        for i in range(k):
            result.append(max(freq.items(), key=lambda x: x[1])[0])
            freq[max(freq.items(), key=lambda x: x[1])[0]] = 0

        return result
        
        