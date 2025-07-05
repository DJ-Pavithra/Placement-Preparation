# Sort Characters By Frequency
# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
class Solution:
    def frequencySort(self, s: str) -> str:
        count_map = {}
        def sort_by_freq(item):
            return -item[1]
        for item in s:
            count_map[item] = count_map.get(item, 0) + 1
        sorted_items = sorted(count_map.items(),key=sort_by_freq)
        res=""
        for key,value in sorted_items:
            res +=key*value
        return res
        
sol=Solution()
print(sol.frequencySort("tree"))  # Output: "eetr" or "eert"
