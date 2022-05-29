class Solution:
    def flooding(self,sr,sc,image,vis,m,n,newColor,oc):
        if sr<0 or sc<0 or sr>=m or sc>=n or vis[sr][sc]==1 or image[sr][sc]!=oc:
            return 
        vis[sr][sc] = 1
        image[sr][sc]=newColor
        self.flooding(sr-1,sc,image,vis,m,n,newColor,oc)
        self.flooding(sr+1,sc,image,vis,m,n,newColor,oc)
        self.flooding(sr,sc-1,image,vis,m,n,newColor,oc)
        self.flooding(sr,sc+1,image,vis,m,n,newColor,oc)
    def floodFill(self, image, sr, sc, newColor):
        m = len(image)
        n = len(image[0])
        vis = [[0 for i in range(n)] for j in range(m)]
        self.flooding(sr,sc,image,vis,m,n,newColor,image[sr][sc])
        return image
        