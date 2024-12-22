def print1_to_10(n):
    if n<=100:
        print(n)
        print1_to_10(n+1)
print1_to_10(1)