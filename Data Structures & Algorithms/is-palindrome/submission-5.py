class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "!!!!" + s
        
        # s = s.translate(str.maketrans('', '', ".,!?;:'\"()[]{}<>-"))
        # j=len(s)-1
        # print(s)
        # for i in range(len(s)):
        #     print((s[i]).lower(),(s[j]).lower())
        #     if (s[i]).lower() != (s[j]).lower():
        #         return False
        #     j-=1


        # return True
        #TWO POINTER SYSTEM 
        j=len(s)-1
        for i in range(len(s)):
            if not (s[i].isalnum()):
                continue
            while not (s[j].isalnum()):
                j-=1
            if s[i].lower()!= s[j].lower():
                return False
            j-=1
        return True
