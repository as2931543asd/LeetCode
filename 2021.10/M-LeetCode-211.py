class WordDictionary:
    # 暴力求解
    # TODO 采用字典树优化
    def __init__(self):
        self.dict = []

    def addWord(self, word: str) -> None:
        self.dict.append(word)

    def search(self, word: str) -> bool:
        temp = set(self.dict)
        if not temp:
            return False
        for dic in temp:
            if len(dic) == len(word):
                count = 0
                for i in range(len(word)):
                    if word[i] == dic[i] or word[i] == '.':
                        i += 1
                    else:
                        break
                    count = i
                if count == len(dic):
                    return True
        return False

