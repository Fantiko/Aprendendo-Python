valor = int(input())
n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0

print(valor)

while valor >= 100:
    valor -= 100
    n100 += 1
while valor >= 50:
    valor -= 50
    n50 += 1
while valor >= 20:
    valor -= 20
    n20 += 1
while valor >= 10:
    valor -= 10
    n10 += 1
while valor >= 5:
    valor -= 5
    n5 += 1
while valor >= 2:
    valor -= 2
    n2 += 1
while valor >= 1:
    valor -= 1
    n1 += 1

print(n100, "nota(s) de R$ 100,00")
print(n50, "nota(s) de R$ 50,00")
print(n20, "nota(s) de R$ 20,00")
print(n10, "nota(s) de R$ 10,00")
print(n5, "nota(s) de R$ 5,00")
print(n2, "nota(s) de R$ 2,00")
print(n1, "nota(s) de R$ 1,00")


