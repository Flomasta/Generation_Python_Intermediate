a, b = (int(input()) for i in range(2))

print(a + b, a - b, a * b, a / b, a // b, a % b, (a ** 10 + b ** 10) * 0.5, sep='\n') if b > 0 else None
