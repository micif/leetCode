class Solution(object):
    def majorityElement(self, nums):
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1  
        max_count = 0
        max_element = None
        for key, value in hash_map.items():
            if value > max_count:
                max_count = value
                max_element = key
        return max_element
