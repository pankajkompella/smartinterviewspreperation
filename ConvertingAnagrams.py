"""Given two strings A and B, find the minimum number of characters that needs to be deleted from these 2 strings to make them anagrams of each other. An anagram is a rearrangement of the letters of one word to form another word. In other words, some permutation of string A must be same as string B.
Input Format
First line of input contains T - number of test cases. Its followed by T lines, each line contains 2 space separated strings - A and B. 
Constraints
1 <= T <= 1000 
1 <= len(A), len(B) <= 1000 
'a' <= A[i],B[i] <= 'z' 
Output Format
For each test case, print the minimum number of deletions required, separated by new line.
Sample Input 0
2
smart interviews
data structures
Sample Output 0
9
12"""
t=int(input())
for _ in range(t):
    a,b=input().split()
    da={chr(k):0 for k in range(97,123)}
    db={chr(k):0 for k in range(97,123)}
    for c in a:
        da[c]+=1
    for c in b:
        db[c]+=1
    c=0
    for d in range(97,123):
        c+=abs(da[chr(d)]-db[chr(d)])
    print(c)
    
