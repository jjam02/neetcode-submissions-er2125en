class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freqS1 = [0]*26
        freqS2 = [0]*26
        l=0
        for letter in s1:
           # print(ord(letter)-ord("a"))
            freqS1[ord(letter)-ord("a")] +=1
        for right in range(len(s2)):
            freqS2[ord(s2[right])-ord("a")] +=1
            while right-l+1 > len(s1):
                freqS2[ord(s2[l])-ord("a")] -=1
                l+=1
            # print(s2[l:right+1],(l,right),len(s1))
            # print(freqS2)
            # print("S1",freqS1)
            if freqS1 == freqS2:
                return True

        

        return False
        