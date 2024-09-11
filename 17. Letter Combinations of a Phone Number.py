class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        word={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        vals=[]
        for i in digits:
            if len(vals)==0:
                vals=word[i]
            else:
                ns=[]
                for j in vals:
                    for k in word[i]:
                        ns.append(j+k)
                vals=ns
        return vals

        