class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        p=list(set(allowed))
        count=0
        for i in words:
            word=set(i)
            for j in word:
                if j not in p:
                    count+=1
                    break
        return len(words)-count
        