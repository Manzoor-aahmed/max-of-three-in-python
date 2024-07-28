def max_of_three(p,q,r):
    if p>=q and p>=r:
      return p
    elif q>=p and q>=r :
       return q
    else : 
        return r
    

s = int(input("enter the number :"))
t = int(input("enter the number :"))
u = int(input("enter the number :"))


print("Max of Three Numbers is :",max_of_three(s,t,u))