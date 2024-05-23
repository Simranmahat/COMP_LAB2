import math
import sys
def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q 
    # Create new arrays L and R
    L = [0]*(n1+1)
    R = [0]*(n2+1)
    
    # Copy data to L and R arrays
    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j+1]
    
    L[n1] = sys.maxsize
    R[n2] = sys.maxsize
    i = 0
    j = 0  
    # Merge the two arrays back into A
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def MergeSort (A, p, r):
    if p<r:
        q=math.floor((p+r)/2)
        MergeSort(A,p,q)
        MergeSort(A,q+1,r)
        Merge(A,p, q, r)