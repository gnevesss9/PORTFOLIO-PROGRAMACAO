while True:
    try:
        num1_str = (input("Primeiro número: "))
        num1_int = int(num1_str)

        operador = input("Operador (+, -, *, /): ")
        if operador not in "+-*/":
            print(f"Erro: Operador '{operador}' inválido. Use +, -, * ou /\n")
            continue

        try:
            num2_str = input("Segundo número: ")
            num2_int = int(num2_str)
            if operador == '/' and num2_int == 0:
                print("Erro: Não é possível dividir por zero. Tente novamente.\n")
                continue
            
            if operador == '+':
                resultado = num1_int + num2_int
            elif operador == '-':
                resultado = num1_int - num2_int
            elif operador == '*':
                resultado = num1_int * num2_int
            elif operador == '/':
                resultado = num1_int / num2_int
            
            print("Resultado: ", resultado)
            break

        except ValueError:
            print(f"Erro: '{num2_str}' não é um número válido. Tente novamente.\n")
            continue

    except ValueError:
        print(f"Erro: '{num1_str}' não é um número válido. Tente novamente.\n")
        continue

# Código feito por Guilherme Neves
# Github: https://github.com/gnevesss9/PROJETOS