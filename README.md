Problem:

There is a horizontal row of n cubes. The length of each cube is given. You need to create
a new vertical pile of cubes. The new pile should follow these directions: 

if cubei
is on top of cubej then sideLengthj>= sideLengthi.

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks. After every "Yes"/ "No" print the volume of all the cubes.
When parsing the inputs create an object for every cube and put it into a data structure of your choice. When processing the cubes take them from that data structure.

Multithreading: Create a simple producer-consumer setup. Create two threads - one to read the input test case by test case and to store it in the data structure with the cubes, and a second thread that takes the cubes one by one from the same structure and makes the needed calculations.

Input Format:
The first line contains a single integer T, the number of test cases.
For each test case, there are 2 lines.
The first line of each test case contains n, the number of cubes.
The second line contains n space separated integers, denoting the sideLengths of each
cube in that order.

Sample number Input:
2
6
4 3 2 1 3 4
3
1 3 2

Constraints

1 <= T <= 5

1 <= n <= 10
5

1 <= sideLength < 2
31

Output Format
For each test case, output a single line containing either "Yes" or "No" without the quotes
followed by the volume of all the cubes in the test case.

Sample Output:
Yes 191
No 36

Explanation :
In the first test case, pick in this order: left - 4, right - 4, left - 3, right - 3, left - 2, right - 1.
In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.

