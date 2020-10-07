from exercicio6po import *

def e_adjacente(v1, v2):
    for i in grafo[v1]:
        for j in grafo[v2]:
            if i == j:
                return v2
    return False

# Exercicio 7
print("\nVértices adjacentes\n")

vertice = int(input("Informe um vertice [0-5]: "))

for v in grafo:
    if v != vertice:
        check = e_adjacente(vertice, v)
        if check:
            print(check)