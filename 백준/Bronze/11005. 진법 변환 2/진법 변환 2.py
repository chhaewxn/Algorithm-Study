N, B = map(int, input().split())
digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''

while N:
    result = digits[N % B] + result
    N //= B
    
print(result)