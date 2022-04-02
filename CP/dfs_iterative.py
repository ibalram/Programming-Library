def dfs(s,par):
    st = [[s,par]]
    sz = [1]*(n+1)
    while st:
        s,par = st.pop()
        f = 1
        for i in gr[s]:
            if i==par: continue
            st.append([i,s])
            f = 0
        if f:

