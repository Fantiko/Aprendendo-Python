

a, b, c = map(int, input().split(" "))

maiorAB = (a + b + abs(a - b)) / 2

maiorAC = (maiorAB + c + abs(maiorAB - c)) / 2

print("{:.0f} eh o maior".format(maiorAC))
