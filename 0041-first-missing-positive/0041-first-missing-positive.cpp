class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        sort(nums.begin(), nums.end()); // Step 1: Sort the array
        
        int smallestPositive = 1; // Step 2: Start checking from 1

        for (int num : nums) { 
            if (num == smallestPositive) { 
                smallestPositive++; // Move to the next expected positive number
            }
        }

        return smallestPositive; // Step 3: Return the first missing positive number
    }
};
