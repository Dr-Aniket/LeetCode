class Solution {
public:
    int dp[2001][2001];
    unordered_map<int,int> mp;

    bool possible(vector<int>& stones, int n, int cur_i, int k) {
        if (cur_i == n - 1)
            return true;

        if(dp[cur_i][k]!=-1)
            return dp[cur_i][k];

        bool crossed = false;

        for (int nxt = k - 1; nxt <= k + 1; nxt++)
            if (nxt > 0) {
                int nxt_stone = stones[cur_i] + nxt;
                if(mp.find(nxt_stone) != mp.end())
                    crossed = crossed || possible(stones, n, mp[nxt_stone], nxt);
                }


        dp[cur_i][k] = crossed;
        return crossed;
    }

    bool canCross(vector<int>& stones) {
        if (stones[1] != 1)
            return false;

        int n = stones.size();

        for(int i=0;i<n;i++)
            mp[stones[i]] = i;
        memset(dp, -1, sizeof(dp));
        return possible(stones, n, 0, 0);
    }
};