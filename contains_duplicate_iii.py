class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: list[int], indexDiff: int, valueDiff: int
    ) -> bool:

        if valueDiff < 0:
            return False

        buckets = {}
        width = valueDiff + 1

        for i, num in enumerate(nums):
            bucket = num // width

            if bucket in buckets:
                return True

            if bucket - 1 in buckets and abs(num - buckets[bucket - 1]) <= valueDiff:
                return True

            if bucket + 1 in buckets and abs(num - buckets[bucket + 1]) <= valueDiff:
                return True

            buckets[bucket] = num

            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                old_bucket = old_num // width
                del buckets[old_bucket]

        return False
