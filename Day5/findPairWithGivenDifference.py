def findPair(self, arr, L,N):
    arr.sort()
    start = 0
    end = 1
    while start<L and end<L:
        if start!=end and arr[end]-arr[start]==N:
            return 1
        elif arr[end]-arr[start]<N:
            end+=1
        else:
            start+=1
    return 0