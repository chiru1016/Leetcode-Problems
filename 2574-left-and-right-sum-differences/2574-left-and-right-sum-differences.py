class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = 0
        ans = []
        rightSum = sum(nums)
        for a in nums:
            leftSum += a
            ans.append(abs(rightSum - leftSum))
            rightSum -= a
        return ans




        