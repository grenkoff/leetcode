# https://leetcode.com/problems/generate-parentheses/

class Solution:
    # Neetcode Backtracking Solution
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(open_n, closed_n):
            if open_n == closed_n == n:
                res.append("".join(stack))
                return

            if open_n < n:
                stack.append("(")
                backtrack(open_n + 1, closed_n)
                stack.pop()
            if closed_n < open_n:
                stack.append(")")
                backtrack(open_n, closed_n + 1)
                stack.pop()

        backtrack(0, 0)
        return res


a = Solution()

assert a.generateParenthesis(3) == ["((()))","(()())","(())()","()(())","()()()"]
assert a.generateParenthesis(1) == ["()"]




# Brute Force
    # Time: O(2**2n * n), Space: O(2**2n * n)
    # def bruteForce(self, n: int) -> List[str]:
    #     def generate(A = []):
    #         if len(A) == 2*n:
    #             if valid(A):
    #                 ans.append("".join(A))
    #         else:
    #             A.append('(')
    #             generate(A)
    #             A.pop()
    #             A.append(')')
    #             generate(A)
    #             A.pop()

    #     def valid(A):
    #         bal = 0
    #         for c in A:
    #             if c == '(': bal += 1
    #             else: bal -= 1
    #             if bal < 0: return False
    #         return bal == 0

    #     ans = []
    #     generate()
    #     return ans

      
    # Backtracking
    # Time: O(4**n / n**0.5), Space: O(4**n / n**0.5)
    # def generateParenthesis(self, n: int) -> List[str]:
    #     ans = []
    #     def backtrack(S = [], left = 0, right = 0):
    #         if len(S) == 2 * n:
    #             ans.append("".join(S))
    #             return
    #         if left < n:
    #             S.append("(")
    #             backtrack(S, left+1, right)
    #             S.pop()
    #         if right < left:
    #             S.append(")")
    #             backtrack(S, left, right+1)
    #             S.pop()
    #     backtrack()
    #     return ans
    
    
    # Closure Number
    # Time: O(4**n / n**0.5), Space: O(4**n / n**0.5)
    # def closureNumber(self, N):
    #     if N == 0: return ['']
    #     ans = []
    #     for c in range(N):
    #         for left in self.generateParenthesis(c):
    #             for right in self.generateParenthesis(N-1-c):
    #                 ans.append('({}){}'.format(left, right))
    #     return ans
    
    
    # DP Solution
    # Time: O(?), Space: O(?)
    # def dpSolution(self, n):
    #     dp = [[] for i in range(n + 1)]
    #     dp[0].append('')
    #     for i in range(n + 1):
    #         for j in range(i):
    #             dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
    #     return dp[n]