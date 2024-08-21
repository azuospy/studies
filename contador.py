#!/usr/bin/env python3



import string
import unicodedata

def remover_acento(texto):
    """Remove acentos de caracteres no texto"""
    texto_normalizado = unicodedata.normalize('NFD', texto)
    return ''.join(c for c in texto_normalizado if unicodedata.category(c) != 'Mn')

def contar_vogais(texto):
    """Conta o número de vogais no texto"""
    vogais = "aeiouAEIOU"
    texto_normalizado = remover_acento(texto)
    contagem = sum(1 for char in texto_normalizado if char in vogais)
    return contagem

def contar_consoantes(texto):
    """Conta o número de consoantes no texto"""
    texto_normalizado = remover_acento(texto)
    consoantes = ''.join(c for c in string.ascii_letters if c not in "aeiouAEIOU")
    contagem = sum(1 for char in texto_normalizado if char in consoantes)
    return contagem

def contar_palavras(texto):
    """Conta o número de palavras no texto"""
    texto_normalizado = remover_acento(texto)
    palavras = texto_normalizado.split()
    return len(palavras)

def main():
    while True:
        print("\nEscolha o tipo de contagem:")
        print("1. Contar vogais")
        print("2. Contar consoantes")
        print("3. Contar palavras")
        print("4. Sair")

        while True:
            escolha = input("Digite o número da opção desejada (1/2/3/4): ")
            if escolha in ('1', '2', '3', '4'):
                break
            else:
                print("Opção inválida! Escolha 1, 2, 3 ou 4.")

        if escolha == '4':
            print("Saindo do programa.")
            break

        texto = input("Digite o texto: ")

        if escolha == '1':
            resultado = contar_vogais(texto)
            print(f"O número de vogais no texto é: {resultado}")
        elif escolha == '2':
            resultado = contar_consoantes(texto)
            print(f"O número de consoantes no texto é: {resultado}")
        elif escolha == '3':
            resultado = contar_palavras(texto)
            print(f"O número de palavras no texto é: {resultado}")

if __name__ == "__main__":
    main()
