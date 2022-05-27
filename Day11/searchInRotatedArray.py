class Solution:
    def pivotedSearch(self,arr,n,k):
        pivot = self.findPivot(arr,0,n-1)
        if pivot==-1:
            return self.binary(arr,0,n-1,k)
        if arr[pivot]==k:
            return pivot
        if arr[0]<=k:
            return self.binary(arr,0,pivot-1,k)
        return self.binary(arr,pivot+1,n-1,k)
    def findPivot(self,arr,low,high):
        if high<low:
            return -1
        if low==high:
            return low
        mid = (low+high)//2
        if mid<high and arr[mid]>arr[mid+1]:
            return mid
        if low<mid and arr[mid]<arr[mid-1]:
            return mid-1
        if arr[low]>=arr[mid]:
            return self.findPivot(arr,low,mid-1)
        return self.findPivot(arr,mid+1,high)
    def binary(self,arr,low,high,k):
        if high<low:
            return -1
        mid = (low+high)//2
        if arr[mid]==k:
            return mid
        if k<arr[mid]:
            return self.binary(arr,low,mid-1,k)
        return self.binary(arr,mid+1,high,k)
    def search(self, nums: List[int], target: int) -> int:
        getIndex = self.pivotedSearch(nums,len(nums),target)
        return getIndex
        