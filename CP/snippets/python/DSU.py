class DSU:
    def __init__(self, n):
        self.par = list(range(n+1))

    def addComp(self, comps):
        for comp in comps:
            p = comp[0]
            for i in comp[1:]:
                self.par[i] = p

    def find(self, a):
        if self.par[a]==a: return a
        cur = a
        while cur!=self.par[cur]:
            cur = self.par[cur]
        self.par[a] = cur
        return self.par[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a==b: return
        self.par[b] = a
