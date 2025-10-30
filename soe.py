
def SieveOfEratosthenes(n):
    prime=[True]*(n+1)
    prime[0] = prime[1] = False
    p=2
    while p*p<=n:
        if prime[p]:
            for i in range(p*p,n+1,p): 
                prime[i]=False
        p+=1
    return prime