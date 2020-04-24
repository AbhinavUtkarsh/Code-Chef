# Factor Tree 
Problem Code: FCTRE

## [Problem Statement](https://www.codechef.com/LRNDSA01/problems/FCTRL) :

Chef lives in a country called ChefLand. The country can be represented as a tree of N cities (numbered 1 through N) connected by N−1 roads. For each valid i, the cost of a house in city i is Ai.

You should answer Q queries. In each query, you are given cities u and v
(possibly identical); Chef is planning to buy houses in these cities. Chef's happiness quotient is equal to the product of the costs of houses in all cities which lie on the simple path between u and v (both inclusive). Since Chef loves playing with factors, he is asking you to tell him the number of factors of his happiness quotient, modulo 1,000,000,007 (10^9+7).

## Input
The first line of the input contains a single integer Tdenoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N.Each of the next N−1 lines contains two space-separated integers x and y denoting that cities x and y are connected by a road.The following line contains N space-separated integers A1,A2,…,AN. The following line contains a single integer Q. Each of the next Q lines contains two space-separated integers u and v
describing a query.

## Output

For each query, print a single line containing one integer ― the number of factors of the happiness quotient modulo 1,000,000,007 (10^9+7).

## Constraints
1≤T≤3

1≤N,Q≤10^5

1≤Ai≤10^6 for each valid i the sum of N over all test cases does not exceed 10^5

Subtasks

Subtask #1 (10 points): N,Q≤10^3


Subtask #2 (30 points): N≤10^3


Subtask #3 (60 points): original constraints


### Example Input

1

5

1 2

1 3

2 4

2 5

2 6 4 3 5

2

1 4

2 2

### Example Output

9

4