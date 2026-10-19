class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a= nums1 + nums2
        a.sort()
        b= len(a)
        if b%2 !=0:
            return (a[(b-1)//2])/1.000
        else :
            return (a[(b//2)-1]+a[b//2])/2.0