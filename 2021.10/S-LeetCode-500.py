from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set("qwertyuiop")
        set2 = set("asdfghjkl")
        set3 = set("zxcvbnm")
        ans = []
        for word in words:
            temp = word.lower()
            temp = set(temp)
            if temp & set1 == temp or temp & set2 == temp or temp & set3 == temp:
                ans.append(word)
        return ans
