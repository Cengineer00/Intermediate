def pascal(x):
    base=[[1]]
    for i in range(x):
        base.append([0])
    for i in range(x-1):
        for j in range(i+1):
            base[i+1].append(0)
        base[i+1][0]=1
        base[i+1][-1]=1    
    base=base[:-1]
    
    for i in range(2,x):
        for j in range(1,i):
            base[i][j]=base[i-1][j-i]+base[i-1][j-i-1]
    return base
