import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        ans = []
        heapq.heapify(hp)
        for i in range(0,k,1): 
            dis = -1*(points[i][0]**2 + points[i][1]**2)
            heapq.heappush(hp,[dis,[points[i][0],points[i][1]]])
        for i in range(k,len(points),1):
            dis = -1*(points[i][0]**2 + points[i][1]**2)
            if hp[0][0]<dis:
                heapq.heappop(hp)
                heapq.heappush(hp,[dis,[points[i][0],points[i][1]]])
        for i in range(0,len(hp),1):
            ans.append(hp[i][1])
        return ans
                
            
            
            
        