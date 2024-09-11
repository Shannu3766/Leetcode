class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sent1 = sentence1.split()
        sent2 = sentence2.split()
        n1=len(sent1)
        n2=len(sent2)
        if n1>n2:
            n1,n2=n2,n1
            sent1,sent2 = sent2[:],sent1[:]
        i=0
        while i < n1 and sent1[i] == sent2[i]:
            i+=1
        while i < n1 and sent1[i] == sent2[n2-n1+i]:
            i+=1
        return i==n
    