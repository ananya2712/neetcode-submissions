class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSumCount = {}

        prefixSum = 0
        count = 0

        prefixSumCount[0] = 1

        for i in range(n):
            # Add current element to prefix sum
            prefixSum += nums[i]

            # Calculate the prefix sum that needs to be removed
            remove = prefixSum - k

            # If this prefix sum has been seen before,
            # add its count to the result
            if remove in prefixSumCount:
                count += prefixSumCount[remove]

            # Update the frequency of the current prefix sum
            prefixSumCount[prefixSum] = prefixSumCount.get(prefixSum, 0) + 1
        return count
