class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return 0
        
        # 1. PRE-COMPUTE PREFIX SUMS
        # Allows us to calculate Sum(p+1...q-1) in O(1)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
            
        # 2. BEST INCREASING PREFIX (Ending at Peak P)
        # best_p[i] = max sum of strictly increasing subarray ending at i (length >= 2)
        best_p = [float('-inf')] * n
        curr_inc_sum = nums[0]
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # Either (prev + current) OR (accumulated_increasing_sum + current)
                best_p[i] = max(nums[i] + nums[i-1], nums[i] + curr_inc_sum)
                curr_inc_sum = best_p[i]
            else:
                # Strictly increasing condition broken, reset
                curr_inc_sum = nums[i]

        # 3. BEST INCREASING SUFFIX (Starting at Valley Q)
        # best_q[i] = max sum of strictly increasing subarray starting at i (length >= 2)
        best_q = [float('-inf')] * n
        curr_suff_sum = nums[n-1]
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                best_q[i] = max(nums[i] + nums[i+1], nums[i] + curr_suff_sum)
                curr_suff_sum = best_q[i]
            else:
                curr_suff_sum = nums[i]

        # 4. LINEAR SCAN OVER DECREASING SLOPES (p...q)
        # We need p < q and nums[p...q] to be strictly decreasing.
        # Total Sum = (best_p[p] - prefix_sum[p+1]) + (prefix_sum[q] + best_q[q])
        
        max_total = float('-inf')
        i = 0
        while i < n - 1:
            # Look for a strictly decreasing segment
            if nums[i] > nums[i+1]:
                start = i
                while i < n - 1 and nums[i] > nums[i+1]:
                    i += 1
                end = i
                
                # Within this decreasing slope [start...end], find optimal p and q
                # p must appear before q (p < q)
                current_max_p_term = float('-inf')
                
                for k in range(start, end + 1):
                    # Check if k can be our valley (q)
                    # We can only have a valley if we've seen a valid peak (p) before it
                    if k > start and best_q[k] != float('-inf'):
                        q_term = prefix_sum[k] + best_q[k]
                        if current_max_p_term != float('-inf'):
                            max_total = max(max_total, current_max_p_term + q_term)
                    
                    # Check if k can be our peak (p)
                    if best_p[k] != float('-inf'):
                        p_term = best_p[k] - prefix_sum[k+1]
                        current_max_p_term = max(current_max_p_term, p_term)
            else:
                i += 1
                
        return int(max_total)