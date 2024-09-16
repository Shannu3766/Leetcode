class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times=[]
        for time in timePoints:
            h,m=map(int,time.split(":"))
            times.append(h*60+m)
        times.sort()
        mi=999
        for i in range(len(times)-1):
            mi=min(mi,times[i+1]-times[i])
        mi=min(mi,24*60-times[-1]+times[0])
        return mi