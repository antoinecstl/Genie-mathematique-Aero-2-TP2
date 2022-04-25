"PARTIE 1: STOCKAGE DES MATRICES TRIDIAGONALES"

# Q1 : On remarque que la matrice A est de taille n² tandis que la matrice Â est de taille 3*n. La matrice Â est donc la plus petite en termes de stockage.

#Q2 : 

import numpy as  np

def TRIreduite(A):
    n,m = A.shape
    Atd = np.zeros((n,3))
    C1 = np.diag(A,-1)
    C1 = np.insert(C1, 0, 0)
    C2 = np.diag(A,0)
    C3 = np.diag(A,1)
    C3 = np.append(C3,0)
    Atd = np.column_stack((C1,C2,C3))

    print(Atd)

def TRIcomplete(Atd):
    n,m = Atd.shape
    A = np.zeros((n,m))
    D1 = Atd.T[0]
    D2 = Atd.T[1]
    D3 = Atd.T[2]
    V1 = np.diag(D1[1:],-1)
    V2 = np.diag(D2,0)
    V3 = np.diag(D3[:-1],1)
    V4 = V1 + V2 + V3
    print(V4)

#Q3 :

def produitTRIvect(Atd,X):
    S = np.array(0)
    n,m = X.shape
    j = 0
    for i in range(1,n):
        if j < n-2:
            nl = Atd[i] #Prends les vecteurs lignes de Atd
            nd = nl[0]*X[j] + nl[1]*X[j+1] + nl[2]*X[j+2]
            j = j + 1
            S = np.column_stack((S,nd))  
    S = np.delete(S,0)  #Enlève le 0 initial de la matrice S.

    #Partie pour le début et la fin de Atd 
    pl = Atd[0]                     #Prends le premier vecteurs lignes de Atd 
    pv = pl[1]*X[0] + pl[2]*X[1]    #Multiplie les composantes de A et X avec les bons index
    S = np.insert(S,0,pv)           #Ajoute cette nouvelle donnée dans le vecteur en index 0 
    dl = Atd[n-1]                   #Prends le dernier vecteur ligne de Atd 
    dv = dl[0]*X[n-2] + dl[1]*X[n-1]#Multiplie avec les dernières composantes de X
    S = np.append(S,dv)             #Ajoute le dernier produit scalaire à la fin du vecteur solution
    print(S)