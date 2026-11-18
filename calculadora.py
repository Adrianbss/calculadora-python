# 1. FUNÇÕES MATEMÁTICAS

def somar_calculadora(number1, number2):
    return number1 + number2

def subtrair_calculadora(number1, number2):
     return number1 - number2

def multiplicar_calculadora(number1, number2):
     return number1 * number2

def dividir_calculadora(number1, number2):
     return number1 / number2

# 3. FUNÇÃO PRINCIPAL

def receber_numeros():
    number1 = float(input("Digite o primeiro número: "))
    number2 = float(input("Digite o primeiro número: "))
    return number1,number2


# 3. FUNÇÃO PRINCIPAL

def main():

    print("===== CALCULADORA PYTHON =====")

    continuar = "s"

    while continuar == "s":

        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Encerrar")

        try:

            escolha = int(input("Escolha uma opção: "))

        except ValueError:
            print("Erro. Digite uma opção entre 1-5")
            continue
                 
        if escolha == 1:

            try:           
                number1, number2 = receber_numeros()

                resultado = somar_calculadora(number1,number2)
                print(f"O resultado da adição entre {number1} e {number2} é: {resultado}")
                       
            except ValueError:
        
                print("Inválido. Válido apenas dígitos.")
            
        elif escolha == 2:
     
            try:
       
                number1 = float(input("Digite o primeiro número: "))
                number2 = float(input("Digite o segundo número: "))
       
                resultado = subtrair_calculadora(number1,number2)
                print(f"O resultado da subtração entre {number1} e {number2} é: {resultado}")
               
            except ValueError:

                print("Inválido. Válido apenas dígitos.")


        elif escolha == 3:
     
            try:

                number1 = float(input("Digite o primeiro número: "))
                number2 = float(input("Digite o segundo número: "))

                resultado = multiplicar_calculadora(number1,number2)
                print(f"O resultado da multiplicação entre {number1} e {number2} é: {resultado}")
        
            except ValueError:
                print("Inválido. Válido apenas dígitos.")

    
        elif escolha == 4:

            try:
            
                number1 = float(input("Digite o primeiro número: "))
                number2 = float(input("Digite o segundo número: "))

                resultado = dividir_calculadora(number1,number2)
                print(f"O resultado da divisão entre {number1} e {number2} é: {resultado}")

            except ZeroDivisionError:
                print("Divisão por 0 não é possível!")
            except ValueError:
                print("Inválido. Válido apenas dígitos.")
    

        elif escolha == 5:
            print("Encerrando calculadora...")
            break

        else:
            print("Inválido. Digite (1-5)")

        print("s - continuar")
        print("f - fechar")
    
        while True:
            continuar = input("Deseja continuar? ").lower()

            if continuar == "s":
                break 
            elif continuar == "f":
                print("Encerrando calculadora... Até logo!")
                break 
            else:
                print("Opção inválida! Digite 's' para continuar ou 'f' para fechar.")

        if continuar == "f":
             break

if __name__ == "__main__":
    main()
