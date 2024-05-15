from collections import defaultdict
class DisjointSet():
    def __init__(self,n):
        self.parent = [i for i in  range(n)]
        self.rank = [0] * n
    def findParent(self,node):
        if self.parent[node] != node:
          self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    def unionRank(self,u,v):
        pu = self.findParent(u)
        pv = self.findParent(v)
        if pu == pv:
          return 
        if self.rank[pu]<self.rank[pv]:
          self.parent[pu] = pv
        elif self.rank[pv]<self.rank[pu]:
          self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[pu] += 1
class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        ds = DisjointSet(n+1)
        #  create a dictionary set to store the names
        dct = {}   # email --> index of acc
        for i,a in enumerate(accounts):
            for mail in a[1:]:
                if mail in dct:
                    ds.unionRank(i,dct[mail])
                else:
                    dct[mail] = i
        # Traversing in the nodes and assigning them to their parents
        mergeMail = defaultdict(list)  # index of account --> list of mails
        for e,i in dct.items():
            leader = ds.findParent(i)
            mergeMail[leader].append(e)
            
        # appending the sorted list and the names to the ans list 
        ans = []    
        for i,emails in mergeMail.items():
            name = accounts[i][0]
            ans.append([name]+ sorted(mergeMail[i]))
        return ans
