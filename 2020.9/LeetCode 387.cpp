#include<vector>
#include<math.h>
#include<algorithm>
#include<string>
#include<iostream>
using namespace std;
class Solution {
public:
    //����  �����ܹ� �ռ任ʱ��
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
        //����C++�� find���� ���һ�ַ���ǰ��������Ӻ���ǰ
        //��λ��һ���Ļ� �Ͳ��ظ�
        for (size_t i = 0; i < s.size(); i++) {
            if (s.find(s[i]) == s.rfind(s[i]))
                return i;
        }
        return -1;
    }
};
