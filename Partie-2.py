"PARTIE 2 : DÉCOMPOSITION LU "

import numpy as  np

def DecompositionLU(A):
    nbligne=len(A)      #Récupère le nombre de ligne de la matrice A
    nbcoll=len(A[0])    #Récupère le nombre de colonne de la matrice A
    L = np.eye(nbligne) #Crée une matrice identité de taille le nombre de ligne de A
    
    for i in range (0,nbligne-1): #Application de la décomposition LU par triple boucle
        for j in range (i+1, nbligne):
            L[i][i] = 1
            L[nbligne-1][nbcoll-1] = 1
            a = A[j][i]
            for l in range (i, nbcoll):
                L[j][i] = a/A[i][i]
                A[j][l] = A[j][l] - (a/A[i][i]) * A[i][l]
                
    return L,A


def triLU(Â):
    c1 = np.delete(Â[:, 0],0,0).T     #Colonne avec les composantes de la matrice L (Lower&tridiagonale)
    c2 = Â[:, 1].T                    #Colonne avec les composantes diagonales de la matrice U 
    c3 = np.delete(Â[:, 2], -1, 0).T  #Colonne avec les composantes diagonales supérieures d'un de la matrice U  
    nbligne = len(c2)                   
    l = [1 for i in range(4)]           
    M = np.zeros((nbligne, 3))          
    for i in range(0, nbligne-1):
        l[i] = c1[i]/c2[i]
        
        c2[i+1] = c2[i+1] - l[i]*c3[i]

    M[:, 0] = np.concatenate(([0], l))
    M[:, 1] = c2
    M[:, 2] = np.concatenate((c3, [0]))
    
    return M
                