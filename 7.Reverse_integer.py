class Solution:
    def reverse(self, x: int) -> int:
        k=0
        if x<0:
            k=str(x)[1:]
            k=-1*int(k[::-1])
        else:
            k= int(str(x)[::-1])
        if -2**31<k and k<2**31-1:
            return k
        else:
            return 0