class Solution:

    def encode(self, strs: list[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> list[str]:
        num = ""
        res = []
        i=0
        while i < len(s):

            if s[i].isdigit():
                num +=s[i]
                i+=1
            if s[i] == "#":

                res.append(s[i+1:i+int(num)+1])
                i+=int(num) +1
                num = ""

                
            
        return res
