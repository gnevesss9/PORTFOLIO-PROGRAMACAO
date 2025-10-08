def inteiro_binario(inteiro):
     if inteiro < 0:
          print("Insira um número inteiro não negativo.")
          return
     print(bin(inteiro)[2:])


def binario_inteiro(binario):
     print(int(binario, 2))


def calcular_bit_paridade(byte, tipo="par"):
     uns = byte.count("1")
     if tipo == "par":
          return "0" if uns % 2 == 0 else "1"
     elif tipo == "impar":
          return "1" if uns % 2 == 0 else "0"
     else:
          print("Tipo inválido. Use 'par' ou 'impar'.")


def verificar_paridade(byte, bit_paridade, tipo="par"):
    uns = byte.count("1") + int(bit_paridade)
    if tipo == "par":
        if uns % 2 == 0:
            print("Paridade válida")
        else:
            print("Paridade inválida")
    elif tipo == "impar":
        if uns % 2 == 1:
            print("Paridade válida")
        else:
            print("Paridade inválida")
    else:
        print("Tipo inválido. Use 'par' ou 'impar'.")