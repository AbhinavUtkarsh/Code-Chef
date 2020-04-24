# Matrix Decomposition 
Problem Code: MATBREAK
## [Problem Statement](https://www.codechef.com/COOK117B/problems/MATBREAK) :
You are given a square matrix M with N rows (numbered 1 through N) and N columns (numbered 1 through N
). Initially, all the elements of this matrix are equal to A . The matrix is broken down in N step (numbered 1 through N ); note that during this process, some elements of the matrix are simply marked as removed, but all elements are still indexed in the same way as in the original matrix. For each valid i, the i-th step consists of the following:

Elements M1,N−i+1,M2,N−i+1,…,Mi−1,N−i+1 are removed.
Elements Mi,N−i+1,Mi,N−i+2,…,Mi,N are removed.
Let's denote the product of all 2i−1 elements removed in this step by pi
. Each of the remaining elements of the matrix (those which have not been removed yet) is multiplied by pi.
Find the sum p1+p2+p3+…+pN . Since this number could be very large, compute it modulo 10^9+7 .

## Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows. The first and only line of each test case contains two space-separated integers N and A.

## Output
For each test case, print a single line containing one integer ― the sum of products at each step modulo 109+7.

## Constraints
1≤T≤250

1≤N≤10^5

0≤A≤10^9 the sum of N over all test cases does not exceed 10^5

### Example Input

1

3 2

### Example Output

511620149