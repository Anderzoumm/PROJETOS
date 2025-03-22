def calculadora():
    while True:
        print("\n--- Calculadora Simples ---")
        print("Operações disponíveis:")
        print("1: Adição (+)")
        print("2: Subtração (-)")
        print("3: Multiplicação (*)")
        print("4: Divisão (/)")
        print("5: Sair")

        escolha = input("Escolha uma operação (1/2/3/4/5): ")

        if escolha == '5':
            print("Saindo da calculadora...")
            break

        if escolha in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida! Por favor, digite números válidos.")
                continue

            if escolha == '1':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif escolha == '2':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif escolha == '3':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        else:
            print("Opção inválida! Por favor, escolha uma operação válida.")

if __name__ == "__main__":
    calculadora()