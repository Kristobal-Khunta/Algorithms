# n here, we have 2**(N-1) as half for N level. And our base case is when N equals to 1. Then we are determine based on K's value like we are at 2nd level. So it seems we are going with 0-indexed N. But N is 1-indexed for this question. However, it still gives us correct answer.

# Anyway, here is my modified solution going 1-indexed:

# Since N and K are both 1-indexed. On level N, we have 2^(N-1) elements. And half should be 2^(N-2). And Our base case is N==1 where K can only be 1 holding value 0.
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        half = 2 ** (N - 2)
        if K <= half:
            return self.kthGrammar(N - 1, K)
        else:
            return 1 if self.kthGrammar(N - 1, K - half) == 0 else 0
