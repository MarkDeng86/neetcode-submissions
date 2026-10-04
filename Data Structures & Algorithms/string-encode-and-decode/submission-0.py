class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = ""
        for word in strs:
            encode += str(len(word)) + "#"
            encode += word
        return encode

    def decode(self, s: str) -> List[str]:
        index = 0
        lengthStr = ""
        output = []
        while(index < len(s)):
            if (s[index] == "#"):
                n = int(lengthStr)
                output.append(s[index+1:index+1+n])
                index += 1+n
                lengthStr = ""
            else:
                lengthStr += s[index]
                index +=1
        return output
            