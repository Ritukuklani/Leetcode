class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c1, c2 = 0, 0
        vowel = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(s)//2):
            if s[i].lower() in vowel:
                c1+=1
            if s[len(s)//2+i].lower() in vowel:
                c2+=1
        return c1==c2