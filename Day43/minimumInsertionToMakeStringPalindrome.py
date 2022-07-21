class Solution:
    def minInsertions(self, S: str) -> int:
        dp = [[0 for i in range(len(S))]for j in range(len(S))]
        for g in range(0,len(S),1):
            i = 0 
            j = g
            for k in range(g,len(S),1):
                if g==0:
                    dp[i][k] = 1  #1 for 1st diagonal
                elif g==1:
                    if S[i]==S[k]:
                        dp[i][k] = 2 # length of two i both matches its 2 else 1
                    else:
                        dp[i][k] = 1
                else:
                    if S[i]==S[k]:
                        dp[i][k] = dp[i+1][k-1]+2
                    else:
                        dp[i][k] = max(dp[i][k-1],dp[i+1][k])
                i+=1
        return len(S)-dp[0][len(S)-1]
        