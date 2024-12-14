# Somando inteiros consecutivos - 1149
# Objetivo: Fazer a soma de uma sequencia de inteiros positivos.

a, n = map(int, input().split())

while n <= 0:
    N = int(input("Digite:"))
    n = N
    a = a
soma = 0
for i in range(n):
    soma = a + i + a

print(soma)