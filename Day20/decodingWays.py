class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        dp = [0 for i in range(len(s))]
        dp[0] = 1
        for i in range(1,len(dp),1):
            if s[i]=='0' and s[i-1]=='0':
                dp[i] = 0
            elif s[i]!='0' and s[i-1]=='0':
                dp[i] = dp[i-1]
                
            elif s[i]=='0' and s[i-1]!='0':
                if s[i-1]=='1' or s[i-1]=='2':
                    if i>=2: #to avoid index out of bound
                        dp[i] = dp[i-2]
                    else:
                        dp[i] = 1
                else:
                    dp[i] = 0
            else:
                if int(s[i-1:i+1])<=26:
                    if i>=2:
                        dp[i] = dp[i-1]+dp[i-2]
                    else:
                        dp[i] = dp[i-1] + 1
                else:
                    dp[i] = dp[i-1]
        return dp[len(dp)-1]
                
        