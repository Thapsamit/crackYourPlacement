class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n==1:
            return 1
        arr = [0 for i in range(n+1)]
        arr[1] = 1
        twoPtr = 1
        threePtr = 1
        fivePtr = 1
        i = 2
        while i<=n:
            val2 = arr[twoPtr]*2
            val3 = arr[threePtr]*3
            val5 = arr[fivePtr]*5
            if val2<val3 and val2<val5:
                arr[i]=val2
                i+=1
                twoPtr+=1
            elif val3<val2 and val3<val5:
                arr[i]=val3
                i+=1
                threePtr+=1
            elif val5<val2 and val5<val3:
                arr[i]=val5
                i+=1
                fivePtr+=1
            elif val2==val3 and val2<val5:
                arr[i] = val2
                i+=1
                twoPtr+=1
                threePtr+=1
            elif val3==val5 and val3<val2:
                arr[i]=val3
                i+=1
                threePtr+=1
                fivePtr+=1
            elif val2==val5 and val2<val3:
                arr[i]=val2
                i+=1
                twoPtr+=1
                fivePtr+=1
            else:
                arr[i]=val2
                i+=1
                twoPtr+=1
                threePtr+=1
                fivePtr+=1
        print(arr)
        return arr[n]
            
        
        