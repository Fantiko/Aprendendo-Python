segundos = int(input())

# Cálculo das horas, minutos e segundos
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

# Impressão do resultado no formato horas:minutos:segundos
print(f"{horas}:{minutos:02d}:{segundos:02d}")
