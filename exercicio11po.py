# -*- coding: utf -8 -*-

n = int(input(" Informe um número: "))

somatorio = 0

for i in range(n):
	somatorio += 2*i-1 / (-2)**i+1

print(somatorio)