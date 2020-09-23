#include<vector>
#include<math.h>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
class Solution {
public:
    //初版  还行能过 空间换时间
    int firstUniqChar1(string s) {
        int alaphbet[26] = { 0 };
        for (size_t i = 0; i < s.size(); i++)
        {
            alaphbet[s[i] - 97] += 1;
        }
        for (size_t i = 0; i < s.size(); i++)
        {
            if (alaphbet[s[i] - 'a'] == 1) {
                return i;
            }
        }
        return -1;
    }
    int firstUniqChar1(string s) {
        //利用C++的 find函数 如果一字符从前往后找与从后往前
        //找位置一样的话 就不重复
        for (size_t i = 0; i < s.size(); i++) {
            if (s.find(s[i]) == s.rfind(s[i]))
                return i;
        }
        return -1;
    }
};
