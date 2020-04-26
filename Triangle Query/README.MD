# Triangle Query 
Problem Code: TRIQRY
## [Problem Statement](https://www.codechef.com/LTIME83B/problems/TRIQRY) :
You are given N points (numbered 1 through N) in a Cartesian coordinate system. For each valid i, the coordinates of the i-th point are (xi,yi).
You should answer Q queries (numbered 1 through Q). For each valid i, in the i-th query:
You are given two points L=(li,0) and R=(ri,0).
Consider an isosceles right triangle such that its hypothenuse is the line segment between the points L and R (two of its vertices) and the vertex opposite to it lies above the x-axis.
The answer to this query is the number of points among the given N points which lie inside or on the perimeter of this triangle.

## Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.The first line of each test case contains two space-separated integers N and Q.N lines follow. For each valid i, the i-th of these lines contains two space-separated integers xi and yi.Q more lines follow. For each valid i, the i-th of these lines contains two space-separated integers li and ri.
## Ouput
For each test case, print a single line containing Q space separated integers. For each valid i, the i-th of these integers should be the answer to the i-th query.

### Constraints

1≤T≤100

1≤N,Q≤10^6

0≤xi,yi≤10^6 for each valid i

0≤ li< ri≤10^6 for each valid i

the sum of N over all test cases does not exceed 10^6
the sum of Q over all test cases does not exceed 10^6

#### Subtasks

Subtask #1 (50 points):

N≤10^5

r1−l1=r2−l2=…=rN−lN

the sum of N over all test cases does not exceed 10^5
the sum of Q over all test cases does not exceed 10^5

Subtask #2 (50 points): original constraints

#### Example Input

1

6 3

1 2

14 7

6 3

8 7

11 10

14 2

0 10

2 22

11 17

#### Example Output

1 3 1

#### Explanation

Example case 1: 

![](https://abhinavutkarsh728.s3.amazonaws.com/Tri.PNG)