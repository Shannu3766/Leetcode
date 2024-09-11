class Solution:
    def getLucky(self, s: str, k: int) -> int:
        vals=""
        for i in s:
            vals+=str(ord(i)-96)
        print(vals)
        for _ in range(k):
            value=0
            for i in vals:
                value+=int(i)
            vals=str(value)
        return int(vals)
        # return 0