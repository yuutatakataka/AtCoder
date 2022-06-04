alice = 0
bob = 0

N = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)

for i in range(N):
    b = (a[i]) 
    if i%2 == 0:
        alice = alice+b
    else:
        bob = bob+b
f = alice-bob
print(f)