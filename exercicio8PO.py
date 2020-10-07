# -*- coding: utf -8 -*-
"""Usando recursividade, faça um programa que calcule a soma dos valores de
um vetor."""

meu_vetor = [] #criando vetor
for i in range(10): # definindo quantas vezes vai repetir
	numero = input(" Informe um número: ")
	meu_vetor.append(int(numero)) #preenchendo vetor


def soma_vetor(meu_vetor):
    if len(meu_vetor) == 1:
        return meu_vetor[0]
    else:
        return meu_vetor[0] + soma_vetor(meu_vetor[1:]) # # primeiro elemento somado com o retorno da função para
        # o resto da lista de forma recursiva

print(soma_vetor(meu_vetor))

