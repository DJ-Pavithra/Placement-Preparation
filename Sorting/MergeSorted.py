class Solution(object):
    def merge(self, nums1, m, nums2, n):
        last=m+n-1
        while m>0 and n>0:
          if nums1[m-1] > nums2[n-1]:
            nums1[last] = nums1[m-1]
            m -=1
          else:
            nums1[last] = nums2[n-1]
            n -=1
          last -=1
        
        while n>0:
            nums1[last]=nums2[n-1]
            n,last = n-1, last-1

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
solution = Solution()
solution.merge(nums1, m, nums2, n)
print(f"Merged array: {nums1}")

# or just add both arrays and sort(but not in-place and not optimal)

nums3= nums1[:m] + nums2[:n]
nums3.sort()
print(f"Sorted array: {nums3}")