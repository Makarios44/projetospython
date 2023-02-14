valor1 = float (input("digite o primeiro numero\n"))
valor2 = float (input("digite o segundo numero\n"))
print ("esolha uma operação ")
print("1-Adicção\n 2-Subtração\n 3-Multiplicação\n 4-Divisão\n 5-Divisão inteira \n 6-Modulo da divisão\n 7-Exponenciação")
num =int  (input("escolha sua opção\n"))
if num == 1:
    print (valor1 + valor2)
elif num == 2:
    print (valor1 - valor2)
elif num == 3:
   print (valor1 * valor2)
elif num == 4:
    print (valor1 / valor2)
elif num == 5:
    print (valor1 // valor2)
elif num == 6:
    print(valor1 % valor2 )
elif num == 7:
    print (valor1 ** valor2)
else:
    print("numero da operção digitado é invalido")

 
print("xau!! até a proxima")