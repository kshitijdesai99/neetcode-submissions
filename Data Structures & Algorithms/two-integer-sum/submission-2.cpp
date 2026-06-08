class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int,int>> A;
        for (int i = 0; i< nums.size(); i++){
            A.push_back({nums[i],i});
        }
        sort(A.begin(), A.end());

        int i = 0, j = nums.size() - 1;
        while (i<j){
            int cur = A[i].first + A[j].first;
            if (cur == target){
                auto idx1 = A[i].second;
                auto idx2 = A[j].second;
                if (idx1>idx2) swap(idx1,idx2);
                return {idx1,idx2};
            }
            else if (cur < target){
                i++;
            }
            else{
                j--;
            }
        }
        return {};
    }
};
