def fourSum(self, arr, k):
    
    arr.sort()
    ans = []
    n = len(arr)
    for i in range(0,n-3,1):
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,n-2,1):
            if j!=i+1 and arr[j]==arr[j-1]:
                continue
            start = j+1
            end = n-1
            while start<end:
                currSum = arr[i]+arr[j]+arr[start]+arr[end]
                if currSum<k:
                    start+=1
                elif currSum>k:
                    end-=1
                else:
                    ans.append([arr[i],arr[j],arr[start],arr[end]])
                    start+=1
                    end-=1
                    while start<end and arr[start]==arr[start-1]:
                        start+=1
                    while start<end and arr[end]==arr[end+1]:
                        end-=1
    return ans