# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input().strip())  # number of entries
phone_book = {}

# Read the phone book entries
for _ in range(n):
    name, number = input().strip().split()
    phone_book[name] = number

# Read queries until EOF (End of File)
while True:
    try:
        query = input().strip()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break
