class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for word in strs:
            result+= str(len(word))+"#" + word
        return result
    def decode(self, s: str) -> List[str]:
        print(s)
        wordLen = ""
        result = []
        i=0
    
        while i<len(s):
           # print(wordLen,"wordLen")
           # print(s[i],"index:",i)
            if s[i] != "#":
                wordLen+=s[i]
                i+=1
            elif s[i] == "#":
                intLen = int(wordLen)
                wordLen = ""
                result.append(s[i+1:intLen+i+1])
                i+=intLen+1

                
            
        return result
