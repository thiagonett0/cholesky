# Decomposição de Cholesky

Esse repositório possui o método de Decomposição de Cholesky.


### Convenção 1

Qualquer matriz possui linhas e colunas inicialmente indexadas por 0.


### Convenção 2

Matrizes são representadas por letras maiúsculas em negrito; vetores, por minúsculas.


### Definição 1 (Simetria)

Seja uma matriz quadrada $\mathbf{A} \in \mathbb{R}^{n \times n}$ com entradas $a_{i j}$. $\mathbf{A}$ é dita simétrica se e somente se satisfizer

$$
\begin{equation}
    a_{i j} = a_{j i} \textrm{    } \forall i, j = 0, 1, \ldots, n-1
\end{equation}
$$


### Definição 2 (Positiva-Definida)

Seja uma matriz $\mathbf{A} \in \mathbb{R}^{m \times n}$. $\mathbf{A}$ é dita positiva-definida se e somente se satisfizer


$$
\begin{equation}
    v^{T} \mathbf{A} v > 0 \textrm{    } \forall v \in \mathbb{R}^{m \times 1}
\end{equation}
$$


### Definição 3 (Triangularidade Inferior)

Seja uma matriz $\mathbf{L} \in \mathbb{R}^{n \times n}$ com entradas $l_{i j}$. $\mathbf{L}$ é dita triangular inferior se e somente se satisfizer


$$
\begin{equation}
    \textbf{L} \textrm{     }: l_{i j} = 0 \forall j > i 
\end{equation}
$$


### Definição 4 (Triangularidade Superior)

Seja uma matriz $\mathbf{L} \in \mathbb{R}^{n \times n}$ com entradas $l_{i j}$. $\mathbf{L}$ é dita triangular superior se e somente se satisfizer


$$
\begin{equation}
    \textbf{L} \textrm{     }: l_{i j} = 0 \forall i > j 
\end{equation}
$$


### Convenção 3

Matrizes triangulares são representadas por $\mathbf{L}$.


### Decomposição de Cholesky


Seja uma matriz $\mathbf{A}$ simétrica e positiva-definida. Então, $\mathbf{A}$ satisfaz

$$
\begin{equation}
    \mathbf{L} \mathbf{L}^{T} = \mathbf{A} \textrm{    }: l_{i i} > 0
\end{equation}
$$

tal que $\mathbf{L}$ é única. Essa decomposição é chamada de Decomposição de Cholesky.

**Demonstração:**


Algoritmo 4.2.1, página 144 de [1].


# Referências

[1] Matrix Computations; GOLUB, Gene H., VAN LOAN, Charles F.; 3ed, 1996. ISBN: 0-8018-5414-8