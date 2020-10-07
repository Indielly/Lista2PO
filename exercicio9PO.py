# -*- coding: utf -8 -*-
"""9. Escreva um programa que, para n>0, escreva:
∑ i×(i+1)
i=1
n"""

n = int(input(" Informe um número: "))

soma = 0

for i in range(n):
	soma += i *(i+1)

print(soma)

