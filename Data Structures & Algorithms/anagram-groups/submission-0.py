class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = {}
        for i in strs:
            newMap = [0] * 26
            for j in i:
                index = ord(j) - ord('a')
                newMap[index] += 1
            if wordMap.get(tuple(newMap)) is None:
                wordMap[tuple(newMap)]  = [i]
            else :
                wordMap[tuple(newMap)].append(i)
        return wordMap.values()