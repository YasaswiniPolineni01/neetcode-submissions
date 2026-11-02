
class Solution:
    def topKFrequent(self, nums, k):

        # Step 1: Count frequencies
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Step 2: Create buckets
        buckets = []

        for i in range(len(nums) + 1):
            buckets.append([])

        # Step 3: Place elements into buckets
        for num in frequency:
            count = frequency[num]
            buckets[count].append(num)

        # Step 4: Collect top k elements
        result = []

        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result


        