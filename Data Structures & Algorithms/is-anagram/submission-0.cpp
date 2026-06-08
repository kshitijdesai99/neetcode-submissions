class Solution {
public:
    bool isAnagram(string s, string t){
        if (s.length() != t.length()){
            return false;
        }

        vector<int> countz(26,0);
        for (int i = 0; i < s.length(); i++){
            countz[s[i] - 'a']++;
            countz[t[i] - 'a']--;
        }

        for (int val : countz){
            if (val != 0){
                return false;
            }
        }
        return true;
    }
};
