# User function Template for python3
'''
Given two strings. The task is to find the length of the longest common substring.
'''

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        dp = [[-1] * (m + 1) for i in range(n + 1)]
        for i in range(m + 1):
            dp[0][i] = 0
        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # print(S1[i-1],S2[j-1])
                if S1[i - 1] == S2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0
        # print(dp)
        max_val = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if dp[i][j] > max_val:
                    max_val = dp[i][j]
        return max_val


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = input().strip().split(" ")
        n, m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()

        ob = Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends