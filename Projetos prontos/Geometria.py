#!/usr/bin/env python3

import math 
import os

def limpar_tela():
  os.system('cls' if os.name == 'nt' else 'clear')

def p():
  print(" ")
  print(" ")

def tringulo():
  
  for i in range(0,5):
   base=(i*2+1)
   espaços=(5-i)
   
   print(" "* espaços, "#"* base, " "* espaços)

def triangulo_retangulo():
  
  for i in range(0,6):
   base2=(i*2+1)
   print("#"*base2)

def escaleno():
  
  for i in range(0,7):
    x = (i*2)
    espaços= (i+1)
    print(" " * espaços, "#" * x)

def triangle(base):
  
  for i in range(0, base):
   espaços= (6-i)
   print (" "* espaços, '#' * (i * 2 + 1))

def cone(base):
    
    for i in range(0, base):
        x = (base - 1) - i
        espaços = (i+2)
        print (" "* espaços, '#' * (x * 2 + 1))

base = 9

metade_cima = math.ceil(base / 2) + 1
metade_baixo = math.ceil(base / 2)

def quadrado():
  
  for i in range(0,4):
    tralhas=(i-i+11)
    print("#"*tralhas) 
    
def retangulo():
  
  for i in range(0,4):
    tralhas=(i-i+22)
    print("#"*tralhas)
  
def cilindro():
   
   for i in range(0,10):
     espaços = 3
     tralhas = (13)
     print(" " * espaços, "#" * tralhas)

def fazuL():
    for i in range(0,10):
     espaços = 3
     tralhas = (13)
     print(" " * espaços, "#" * tralhas)

def fazueli():
    print("#" * 13) 
    print("#" * 13) 
    
def coracao():
  for i in range(1,3):
   espaço1=(3-i)
   x = (i * 2 + 1)
   espaço2= (5 - i * 2)
   print(" " * espaço1 , "#"* x, " " * espaço2, "#" * x)

def coracao2():
 
 for i in range(0,7):
   x= (13- i*2)
   espaços =(i + 1)
   print(" " * espaços, "#" * x)

def olhos():
  
  for i in range(0,3):
   if i == 0:
    print("=======     =======")
  if i == 1:
    print("|<|||>|    |<|||>|")
  if i == 2:
    print("|<|||>| ◍◍  |<|||>|")
  

def boca():
  for i in range(4, 5):
    x = (i - i + 10)
    espaços=(i - i + 3 )
    print(" "* espaços, "◍" * x)
    
def fazuL():
    for i in range(0,6):
     espaços = 3
     tralhas = (5)
     print(" " * espaços, "#" * tralhas)

def fazueli():
    print(" " * 3, "#" * 13) 
    print(" " * 3, "#" * 13) 
    p()
    print("     Até programando você é esquerdista hein \n     FazuL agora...")

limpar_tela()

while True:
  
  resposta = input("\n Opçôes: \n \n  1 - Triângulo \n  2 - Triângulo retângulo \n  3 - Escaleno \n  4 - Diamante \n  5 - Quadrado \n  6 - Retângulo \n  7 - Cilindro \n  8 - Coração \n  9 - Rosto \n 10 - Sair \n\n Digite uma delas: ")

  limpar_tela()

  if resposta == "1":
   p()
   tringulo()

  elif resposta == "2":
   p()
   triangulo_retangulo()
  
  elif resposta == "3":
    escaleno()
  
  elif resposta == "4":
   p()
   triangle(metade_cima)
   cone(metade_baixo)
  
  elif resposta == "5":
    p()
    quadrado()
  
  elif resposta == "6":
    p()
    retangulo()
  
  elif resposta == "7":
    cilindro()
    
  
  elif resposta == "8":
    p()
    coracao()
    coracao2()
    
  elif resposta == "9":
    p()
    olhos()
    boca()

  elif resposta == "10":
    break
  
  elif resposta == "13":
    p()
    fazuL()
    fazueli()
    
  else:
   print ("\nRESPOSTA INVÁLIDA!")

