class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        query=list(set([tuple(q) for q in queries]))
        query_vals={}
        # out=[]
        for i in query:
            b=arr[i[0]:i[1]+1]
            xor_value = b[0]
            for num in b[1:]:
                xor_value ^= num
            query_vals[i]=xor_value
        out=[]
        for i in queries:
            out.append(query_vals[tuple(i)])
        return out
        