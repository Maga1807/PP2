def largestAltitude(self, gain):
        ans=[]
        ans.append(0)
        for i in range(0,len(gain)):
            tmp=ans[i]+gain[i]
            ans.append(tmp)
            
        return max(ans)