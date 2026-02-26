class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)
        st, left, dp = [], [-1] * n, [0] * n
        
        # Pass 1: Monotonic Stack
        for i, x in enumerate(books):
            # Check if stack top violates the "strictly increasing" slope
            while st and books[st[-1]] >= x - (i - st[-1]): st.pop()
            if st: left[i] = st[-1]
            st.append(i) # Crucial: add current index to stack
        
        # Pass 2: DP Calculation
        for r, x in enumerate(books):
            l = left[r] + 1 # Use 'r', not 'i'
            cnt = min(x, r - l + 1)
            b, e = x - cnt + 1, x
            
            # Sum of arithmetic progression
            total_sum = (b + e) * cnt // 2
            
            # Add the safe sequence sum from the left boundary
            dp[r] = total_sum + (dp[left[r]] if left[r] != -1 else 0)
        
        return max(dp) if dp else 0