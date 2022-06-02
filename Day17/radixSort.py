def radixSort(arr):
	maxVal = -999999
	for i in range(0,len(arr),1):
		maxVal = max(maxVal,arr[i])
	exp = 1
	while exp<=maxVal:
		countSort(arr,exp)
		exp = exp*10

def countSort(arr,exp):
	freq = [0 for i in range(10)]
	for i in range(0,len(arr),1):
		freq[(arr[i]//exp) % 10] += 1
	
	for s in range(0,len(freq),1):
		if s==0:
			continue
		else:
			freq[s] = freq[s]+freq[s-1]
	ans = [0 for i in range(len(arr))]
	for i in range(len(arr)-1,-1,-1):
		pos = freq[(arr[i]//exp)%10]-1
		ans[pos] = arr[i]
		freq[(arr[i]//exp)%10]-=1
	for i in range(0,len(arr),1):
		arr[i] = ans[i]

arr  = [5,2,9,8,7,1,4,3,2,3,8]
radixSort(arr)
print(arr)