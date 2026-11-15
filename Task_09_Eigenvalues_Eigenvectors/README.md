# Task 9: Eigenvalues and Eigenvectors

## 1. Introduction

This task explores eigenvalues and eigenvectors of square matrices using NumPy.

An eigenvector is a non-zero vector whose direction remains unchanged when multiplied by a square matrix. The relationship is expressed as:

\[
Av=\lambda v
\]

Where:

- \(A\) represents a square matrix.
- \(v\) represents an eigenvector.
- \(\lambda\) represents an eigenvalue.

The eigenvalue indicates how much the eigenvector is scaled when multiplied by the matrix.

Eigenvalues and eigenvectors are useful in several areas of computing and engineering, including network analysis, vibration analysis, stability studies, data science and Principal Component Analysis (PCA).

## 2. Original Problem

The original program uses an adjacency matrix to represent a small undirected network containing four nodes: A, B, C and D.

An adjacency matrix represents connections between nodes. A value of 1 indicates that two nodes are connected, while 0 indicates that they are not directly connected.

The original adjacency matrix is:

\[
A=
\begin{bmatrix}
0&1&1&0\\
1&0&1&1\\
1&1&0&1\\
0&1&1&0
\end{bmatrix}
\]

### 2.1 Input and Mathematical Operations

**Input:**

- A 4 × 4 adjacency matrix representing the network connections.
- Four network nodes labelled A, B, C and D.

**Mathematical operations:**

1. Calculate eigenvalues and eigenvectors using `np.linalg.eig()`.
2. Identify the dominant eigenvalue using `np.argmax()`.
3. Extract the corresponding dominant eigenvector.
4. Normalize the eigenvector so that the importance scores sum to 1.
5. Verify the eigenvalue equation using matrix multiplication.
6. Calculate the verification error using the Euclidean norm.

### 2.2 Original Program

File: `Task_09_eigenvalues.py`

The program calculates the dominant eigenvalue and its corresponding eigenvector, then uses the normalized eigenvector to estimate the relative importance of each network node.

### 2.3 Original Output

```text id="9rj1ef"
Dominant eigenvalue: 2.5615528128088276
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 2.6921477609369894e-15
```

### 2.4 Interpretation of Original Output

- The dominant eigenvalue is approximately 2.5616.
- Nodes B and C have the highest importance scores, approximately 0.2808 each.
- Nodes A and D have importance scores of approximately 0.2192 each.
- The scores add up to approximately 1 because the dominant eigenvector was normalized.
- The very small verification error confirms that the calculated eigenvalue and eigenvector satisfy the equation \(Av=\lambda v\) to numerical precision.

The experiment demonstrates how eigenvector centrality can identify structurally important nodes in a network.

## 3. Parameter Modification

The network structure was modified by introducing a new connection between nodes A and D.

**Original adjacency matrix:**

\[
A=
\begin{bmatrix}
0&1&1&0\\
1&0&1&1\\
1&1&0&1\\
0&1&1&0
\end{bmatrix}
\]

**Modified adjacency matrix:**

\[
A=
\begin{bmatrix}
0&1&1&1\\
1&0&1&1\\
1&1&0&1\\
1&1&1&0
\end{bmatrix}
\]

The corresponding Python changes were:

```python id="0x3p9z"
A = np.array([
    [0., 1., 1., 1.],
    [1., 0., 1., 1.],
    [1., 1., 0., 1.],
    [1., 1., 1., 0.]
])
```

Both corresponding matrix entries were changed because the network is undirected.

### 3.1 Modified Output

```text id="95s8lo"
Dominant eigenvalue: 3.0
Eigenvector-based importance:
A: 0.2500
B: 0.2500
C: 0.2500
D: 0.2500
Verification error: 0.0
```

### 3.2 Interpretation of Modified Output

- The dominant eigenvalue increased from approximately 2.5616 to 3.0.
- All four nodes now have equal importance scores of 0.2500.
- The verification error is zero.
- Adding the connection between A and D made the network fully connected, giving every node the same structural importance.

**Conclusion:** Changing the connections in a network changes its adjacency matrix and can affect its eigenvalues and eigenvectors. This demonstrates how eigenvalue analysis can be used to study network structure.

## 4. Real-World Application: Campus Facility Connectivity Analysis

### 4.1 Problem Description

A university has several facilities connected through shared digital services and communication links.

The facilities include:

1. Library
2. Computer Labs
3. Lecture Halls
4. Administration
5. Student Centre

The aim is to identify which facilities are structurally more important based on their connections to other facilities.

An adjacency matrix is used to represent the connections. Eigenvector centrality is then calculated to estimate the relative structural importance of each facility.

### 4.2 Assumptions

1. The campus network is represented by five facilities.
2. Each facility is represented as a node.
3. A connection between two facilities is represented by 1.
4. The absence of a direct connection is represented by 0.
5. The network is undirected, meaning connections are represented in both directions.
6. The network structure remains constant during the analysis.
7. The network is a simplified illustrative example rather than a representation of actual university infrastructure.

### 4.3 Input

The adjacency matrix is:

\[
A=
\begin{bmatrix}
0&1&1&0&0\\
1&0&1&1&0\\
1&1&0&1&1\\
0&1&1&0&1\\
0&0&1&1&0
\end{bmatrix}
\]

The nodes are ordered as follows:

- Node 1: Library
- Node 2: Computer Labs
- Node 3: Lecture Halls
- Node 4: Administration
- Node 5: Student Centre

### 4.4 Program

File: `Task_09_real_world.py`

The program:

1. Defines the adjacency matrix representing campus facility connections.
2. Calculates the eigenvalues and eigenvectors using NumPy.
3. Identifies the dominant eigenvalue.
4. Extracts the corresponding dominant eigenvector.
5. Normalizes the eigenvector to obtain importance scores.
6. Displays the importance score of each facility.
7. Verifies the eigenvalue equation.

### 4.5 Actual Output

```text id="q7c9df"
Dominant eigenvalue: 2.93543233197003
Campus facility importance:
Library: 0.1593
Computer Labs: 0.2136
Lecture Halls: 0.2541
Administration: 0.2136
Student Centre: 0.1593
Verification error: 1.7342238036525468e-15
```

### 4.6 Interpretation of Results

The calculated importance scores show the relative structural importance of the five facilities.

- **Lecture Halls:** Have the highest importance score of 0.2541, indicating the strongest structural importance in the network.
- **Computer Labs:** Have an importance score of 0.2136.
- **Administration:** Also has an importance score of 0.2136.
- **Library:** Has an importance score of 0.1593.
- **Student Centre:** Has an importance score of 0.1593.

The verification error is approximately \(1.73\times10^{-15}\), which is extremely close to zero. This confirms that the calculated eigenvalue and eigenvector satisfy the eigenvalue equation to numerical precision.

The results demonstrate how eigenvector centrality can be used to identify structurally influential facilities in an interconnected network.

These scores represent connectivity within the simplified model, not actual facility usage or performance.

## 5. Conclusion

This task demonstrated how eigenvalues and eigenvectors can be calculated and applied in network analysis.

The original experiment showed how the dominant eigenvector can be normalized to calculate the relative importance of network nodes.

The parameter modification demonstrated that adding a connection changes the network structure, resulting in a different dominant eigenvalue and equal importance scores for all four nodes in the modified network.

The campus facility application further demonstrated how eigenvector centrality can identify structurally important facilities based on their connections.

Overall, eigenvalues and eigenvectors are useful mathematical tools in scientific computing, particularly in network analysis and other applications involving matrices.

## 6. Files in This Folder

```text id="1fj9zv"
Task_09_Eigenvalues/
│
├── Task_09_eigenvalues.py
├── Task_09_real_world.py
└── README.md
```

## 7. Libraries Used

- **NumPy:** Used for matrix representation, eigenvalue and eigenvector calculations, normalization and numerical verification.

