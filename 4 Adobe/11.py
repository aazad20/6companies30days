class Solution:

    def amendSentence(self, s):
        ans=s[0].lower()
        for i in s[1:]:
            if i.islower():
                ans+=i
            else:
                ans+=" "
                ans+=i.lower()
        return ans
