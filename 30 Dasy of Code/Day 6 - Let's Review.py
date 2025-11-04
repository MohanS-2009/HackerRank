# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())  # number of test cases

for _ in range(t):
    s = input().strip()
    even_chars = ""
    odd_chars = ""
    
    for i in range(len(s)):
        if i % 2 == 0:
            even_chars += s[i]
        else:
            odd_chars += s[i]
    
    print(even_chars, odd_chars)
