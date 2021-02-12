#Good, till now these challenges have been for intermediates, now we bump up the
#standard.

"""
For two strings A and B with the same length N, we will say that they are equivalent if the following rule holds:
For each pair of integers l and r (1≤l≤r≤N), the substring of A between the l-th and r-th character (inclusive) is a palindrome if and only if the substring
of B between the l-th and r-th character (inclusive) is a palindrome.

You are given a string S with length N. Find the number of sets P⊂{1,2,…,N} such that there is a character c and a string X which is equivalent to S and
satisfies Xp=c for each p∈P. Since the answer may be large, compute it modulo 998,244,353.

Input
 - The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
 - The first and only line of each test case contains a single string S with length N.
Output
 - For each test case, print a single line containing one integer ― the number of subsets of characters that can be equal to each other in some string
 - equivalent to S, modulo 998,244,353.

Constraints
 - 1≤T≤1,000
 - 1≤N≤2,000
 - S contains only lowercase Latin letters

Example Input
2
aaa
aba
Example Output
8
5


Your challenge input is : 
3
abd
ihds
jkes


Square the whole number formed by the correct output of this input, you shall have a username of a discord account (add #9869) send a friend request to this
person and dm him the code you used for this challenge. If he deems it correct, he will add you to a secret discord server within a time span of 72 hours,
whereby if anybody shares information in this server, they will be immediately disqualified.
"""
