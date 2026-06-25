class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        high = 0
        low = 0
        for i in gain:
            low += i
            high = max(high,low)
        return high