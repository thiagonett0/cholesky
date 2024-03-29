"""
Descrição: código que executa a Decomposição de Cholesky versão Gaxpy.
"""


import sys
sys.path.append( 'path' )

import linalg as la


def cholesky(A):

    """
    Descrição: calcula o triângulo de Cholesky e reescreve na matriz A. O algoritmo segue conforme o discutido
            em Algoritmo 4.2.1, página 144 de Matrix Computations, Golub e Van Loan, com algumas observações:

                i) em ambos os loops de repetição for, os elementos anteriores ao selecionado são alterados.
                    Sendo assim, caso não armazene o elemento da diagonal conforme o código, o algoritmo 
                    executa a decomposição incorretamente;
                ii) confere se a matriz satisfaz a condição de positiva definida;
    
    Entrada(s):
                i) A (list): matriz simétrica a ser decomposta;
                ii) produtoEscalar (func): função que executa o produto escalar entre dois vetores;
    
    Saída(s):
                i) A (list): matriz de entrada sobre-escrita pela matriz triângulo de Cholesky.
    """

    diag = A[0][0]
    for j in range(len(A)):
        if j > 0:
            for p in range(j, len(A)):
                A[p][j] -= la.dotProduct(A[p][:j], A[j][:j])
                diag = A[j][j]
        for q in range(j, len(A)):
            if diag > 0:
                A[q][j] /= (diag**0.5)
            else:
                print(f"Não é positiva definida.")
                return None
    return A
