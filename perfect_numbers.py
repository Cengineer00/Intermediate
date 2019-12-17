def perfect(n):
    x=0
    for i in range(1,n):
        if n%i==0:
            x=x+i
    if x==n:
        return True
    elif x>n:
        return 5
    
def perfect_numbers(n):
    l1=[]
    l2=[]
    l3=[]
    for i in range(1,n):
        if perfect(i)==True:
            l1.append(i)
        elif perfect(i)==5:
            l2.append(i)
        else:
            l3.append(i)
    
    return (l1,l2,l3)
