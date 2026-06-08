class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> check_dict;
        for (int i = 0; i < nums.size(); i++){
            int remainder = target - nums[i];
            if(check_dict.find(remainder)!=check_dict.end()){
                return{check_dict[remainder],i};
            }
            check_dict[nums[i]] = i;
        }
        return {};
    }
};
