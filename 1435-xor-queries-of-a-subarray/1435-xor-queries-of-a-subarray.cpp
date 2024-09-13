class Solution {
public:
    vector<int> xorQueries(vector<int>& arr, vector<vector<int>>& queries) {
        vector<int> ans;
        int a;
        for(int j=0; j < queries.size(); ++j){
            a = arr[queries[j][0]];
            for(int i=queries[j][0]+1;i<=queries[j][1];i++){
                a = a^arr[i];
            }
            ans.push_back(a);
        }

        return ans;
    }
};