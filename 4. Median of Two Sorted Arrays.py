class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        a=(nums1+nums2)
        a=sorted(a)
        print(a)
        l=int(len(a)/2)
        if(len(a)%2==0):
            print(float(a[l-1]+a[l])/2)
            return float(a[l-1]+a[l])/2
        else:
            print(float(a[l]),45)
            return(float(a[l]))
        