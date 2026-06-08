class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> dict;
        for (int i = 0; i<nums.size();i++){
            int diff = target - nums[i];
            if(dict.find(diff)!=dict.end()){
                return{dict[diff],i};
            }
            dict[nums[i]] = i; 
        }
        return{};
    }
};
