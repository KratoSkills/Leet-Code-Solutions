#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> char_set;
        int l = 0, max_len = 0;

        for (int r = 0; r < s.size(); r++) {
            while (char_set.find(s[r]) != char_set.end()) {
                char_set.erase(s[l]);
                l++;
            }
            char_set.insert(s[r]);
            max_len = max(max_len, r - l + 1);
        }

        return max_len;
    }
};
