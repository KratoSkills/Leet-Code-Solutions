#include <string>
#include <vector>

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1 || numRows >= s.size()) {
            return s;
        }

        std::vector<std::string> rows(numRows);
        int index = 0, step = 1;

        for (char c : s) {
            rows[index] += c;
            if (index == 0) {
                step = 1;
            } else if (index == numRows - 1) {
                step = -1;
            }
            index += step;
        }

        std::string res;
        for (std::string row : rows) {
            res += row;
        }

        return res;
    }
};
