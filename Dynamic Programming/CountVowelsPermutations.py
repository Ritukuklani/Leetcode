class Solution:
    import collections
    def countVowelPermutation(self, n: int) -> int:
#           Using backtracking   
#         vowel = ['a', 'e', 'i', 'o', 'u']
#         def backtrack(vowel, curr):
#             if len(curr)==n:
#                 self.result+=1
#                 return
#             if len(curr)>n:
#                 return
#             if curr[-1] == 'a':
#                 backtrack(vowel, curr + ['e'])
#             elif curr[-1] == 'e':
#                 for char in ['a', 'i']:
#                     backtrack(vowel, curr + [char])
#             elif curr[-1]=='i':
#                 for char in ['a', 'e', 'o', 'u']:
#                     backtrack(vowel, curr + [char])
#             elif curr[-1] == 'o':
#                 for char in ['i', 'u']:
#                     backtrack(vowel, curr + [char])
#             elif curr[-1] == 'u':
#                 backtrack(vowel, curr + ['a'])
                    
#         self.result = 0
#         for i in range(len(vowel)):
#             backtrack(vowel, [vowel[i]])
#         return self.result

# Using DP

        prevs = {'a':1, 'e':1, 'i':1, 'o':1, 'u':1}
        for i in range(1, n):
            cur = collections.defaultdict(int)
            for prev, count in prevs.items():
                if prev == 'a':
                    cur['e'] += count
                elif prev == 'e':
                    for nextch in ['a', 'i']:
                        cur[nextch] += count
                elif prev == 'i':
                    for nextch in ['a', 'e', 'o', 'u']:
                        cur[nextch] += count 
                elif prev == 'o':
                    for nextch in ['i', 'u']:
                        cur[nextch] += count
                elif prev == 'u':
                    cur['a'] += count
            prevs = cur
        return sum(prevs.values()) % 1000000007
        