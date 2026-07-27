class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Count frequencies
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        # Sort after the loop is finished
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(sorted_items[i][0])

        return result