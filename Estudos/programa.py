#!/usr/bin/env python3

import sys

def main():
  if len(sys.argv) != 2:
    print("Uso: ./programa.py <camisa>")
    sys.exit(1)

  camisa = sys.argv[1]

  print(f"camisa {camisa}")

if __name__ == "__main__":
  main()

