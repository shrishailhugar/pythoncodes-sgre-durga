class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        # print(nums1.extend(nums2))
        # print(nums1)
        # print(sum(nums1))
        # print(len(nums1))
        return sum(nums1)/len(nums1)


l1=[1,3]
l2=[2]
s=Solution()
print(s.findMedianSortedArrays(l1,l2))