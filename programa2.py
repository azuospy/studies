#!/usr/bin/env python3

import sys

def main():
  if len(sys.argv) != 3:
    print("Uso: ./programa.py <A> <B>")
    sys.exit(1)

  b = int(sys.argv[2])
  a = int(sys.argv[1])
  
  soma = a + b
  
  print(f"A soma de {a} + {b} é igual a: {soma}")

if __name__ == "__main__":
  main()

