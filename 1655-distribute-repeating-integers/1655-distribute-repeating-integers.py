from typing import List
from collections import Counter

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq = list(Counter(nums).values())
        m = len(quantity)

        # sum of quantities for every subset
        subset_sum = [0] * (1 << m)
        for mask in range(1 << m):
            total = 0
            for i in range(m):
                if mask & (1 << i):
                    total += quantity[i]
            subset_sum[mask] = total

        dp = {0}

        for f in freq:
            new_dp = set(dp)

            for mask in dp:
                remaining = ((1 << m) - 1) ^ mask
                sub = remaining

                while sub:
                    if subset_sum[sub] <= f:
                        new_dp.add(mask | sub)

                    sub = (sub - 1) & remaining

            dp = new_dp

            if (1 << m) - 1 in dp:
                return True

        return False