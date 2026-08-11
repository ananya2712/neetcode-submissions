class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        sorted_items = cnt.most_common()
        return sorted_items[0][0]