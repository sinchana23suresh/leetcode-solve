// 1 ms | 12.5 MB
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l=0
        h=0
        a=[]
        while l<m and h<n:
            if nums1[l]<=nums2[h]:
                a.append(nums1[l])
                l+=1
            else:
                a.append(nums2[h])
                h+=1
        while l<m:
            a.append(nums1[l])
            l+=1
        while h<n:
            a.append(nums2[h])
            h+=1
        for i in range(len(a)):
            nums1[i]=a[i]
        return nums1
        