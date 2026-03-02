class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int maxSum = nums[0];  // Stores the maximum sum found
        int currentSum = 0;     // Tracks sum of current subarray

        for (int num : nums) {
            if (currentSum < 0) 
                currentSum = 0; // Reset if the sum is negative
            
            currentSum += num;  // Add current element
            maxSum = max(maxSum, currentSum); // Update max sum
        }

        return maxSum;
    }
};
