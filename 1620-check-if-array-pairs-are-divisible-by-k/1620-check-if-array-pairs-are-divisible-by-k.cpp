class Solution {
public:
    bool canArrange(vector<int>& arr, int k) {
        unordered_map<int, int> remainder_count;

        // Count the remainders
        for (int num : arr) {
            int remainder = ((num % k) + k) % k;  // Handle negative numbers correctly
            remainder_count[remainder]++;
        }

        // Check pairs
        for (const auto& entry : remainder_count) {
            int rem = entry.first;

            // Special case for remainder 0, there must be an even number of such elements
            if (rem == 0) {
                if (remainder_count[rem] % 2 != 0) {
                    return false;
                }
            }
            // // Special case for remainder k/2 when k is even, there must be an even number of such elements
            // else if (k % 2 == 0 && rem == k / 2) {
            //     if (remainder_count[rem] % 2 != 0) {
            //         return false;
            //     }
            // }
            else {
                // For other remainders, the number of elements with remainder 'rem' must match
                // the number of elements with remainder 'k - rem'
                if (remainder_count[rem] != remainder_count[k - rem]) {
                    return false;
                }
            }
        }

        return true;
    }
};
