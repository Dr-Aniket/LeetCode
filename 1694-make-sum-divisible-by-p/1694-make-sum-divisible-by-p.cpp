class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        int n = nums.size();
        long long sum = 0;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            sum %= p;
        }
        if (sum == 0) {
            return 0;
        }
        unordered_map<long long, int> mp;
        mp[0] = -1;
        long long prefix = 0;
        int ans = n;
        for (int i = 0; i < n; i++) {
            prefix += nums[i];
            prefix %= p;
            long long need = (prefix - sum + p) % p;
            if (mp.find(need) != mp.end()) {
                ans = min(ans, i - mp[need]);
            }
            mp[prefix] = i;
        }
        return ans == n ? -1 : ans;
    }
};