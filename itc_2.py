def la_suite(n):
    u_0=1
    for i in range(n):
        u_0 = u_0 * (1/2) +1
    return u_0

def la_suite_v2(n):
    if n==0:
        return 1
    else:
        return la_suite_v2(n-1)*1/2 +1

def plus_petit_element(L):
    if len(L)==1:
        return L[0]
    if len(L)==2:
        if L[0]>=L[1]:
            return L[1]
        else:
            return L[0]
    elif L[0] <= L[1]:
        return plus_petit_element([L[0]]+L[2:])
    else:
        return plus_petit_element(L[1:])
        
def dicho(x,L):
    debut=0
    fin=len(L)-1
    pivot = (debut + fin) // 2
    if len(L)==0:
        return False
    if L[pivot] == x:
        return True
    if L[pivot] > x:
        return(dicho(x,L[:pivot]))
    else:
        return(dicho(x,L[pivot+1:]))
        
def test(f):
    Res = []

    # 1: L est vide
    L = []
    x = 1
    Res.append(f(x,L)==False)

    # 2: len(L) pair - x dans L - 1° terme
    L = [1,2,3,4]
    x = 1
    Res.append(f(x,L)==True)
    # 3: len(L) pair - x dans L - Dernier terme
    L = [1,2,3,4]
    x = 4
    Res.append(f(x,L)==True)
    # 4: len(L) pair - x dans L - Dedans
    L = [1,2,3,4]
    x = 2
    Res.append(f(x,L)==True)

    # 5: len(L) impair - x dans L - 1° terme
    L = [1,2,4]
    x = 1
    Res.append(f(x,L)==True)
    # 6: len(L) impair - x dans L - Dernier terme
    L = [1,2,4]
    x = 4
    Res.append(f(x,L)==True)
    # 7: len(L) impair - x dans L - Dedans
    L = [1,2,4]
    x = 2
    Res.append(f(x,L)==True)

    # 8: len(L) pair - x n'est pas dans L - Avant
    L = [1,2,3,4]
    x = -1
    Res.append(f(x,L)==False)
    # 9: len(L) pair - x n'est pas dans L - Après
    L = [1,2,3,4]
    x = 5
    Res.append(f(x,L)==False)
    # 10: len(L) pair - x n'est pas dans L - Dedans
    L = [1,2,3,4]
    x = 2.5
    Res.append(f(x,L)==False)

    # 11: len(L) impair - x n'est pas dans L - Avant
    L = [1,2,4]
    x = -1
    Res.append(f(x,L)==False)
    # 12: len(L) impair - x n'est pas dans L - Après
    L = [1,2,4]
    x = 5
    Res.append(f(x,L)==False)
    # 13: len(L) impair - x n'est pas dans L - Dedans
    L = [1,2,4]
    x = 2.5
    Res.append(f(x,L)==False)

    print(Res) # Permet d'identifier le lieu du bug
    return Res == [True]*13

Res = test(dicho)
print('La fonction est correcte ?',Res)