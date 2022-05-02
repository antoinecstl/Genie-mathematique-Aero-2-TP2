"PARTIE 3 : Résolution de système tridiagonaux "

import numpy as  np

#Question 1 

def TriLUResol(M,b):
    Mcomp = TRIComplete(M)
    n,m = Mcomp.shape
    #On résout Ly = b 
    y = b[0]
    for i in range(1,n):
        s = b[i]-M[i][0]*y[i-1]
        y = np.append(y,s)
    #On a maintenant y et maintenat on résout Ux = y
    x = np.zeros(n-1)
    xn =y[n-1]/M[n-1][1]
    x = np.insert(x,n-1,xn) # Ajoute aux vecteur x sa dernière composante 
    for i in range(0,n-1):
        nd = (y[n-i-2]-M[n-i-2][2]*x[n-i-1])/M[n-i-2][1]
        x = np.insert(x,n-i-1,nd) 
        x = np.delete(x,n-i-2)
    return x

#Question 2
def triResol(Atd,b):
    M =  triLU(Atd)
    x = TriLUResol(M,b)
    return x