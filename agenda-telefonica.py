nome = []
telefone= []
opcao =0
while opcao !=6:
 
 print ("BEM VINDO A NOSSA AGENDA TELEFONICA:\n opções: \n 1- Listar contatos: \n 2-Inserir contatos: \n 3-Alterar contato: \n 4-Buscar contato:\n 5-Remover contato:\n 6-Sair")
 opcao = int (input(""))
#aqui eu insiro contatos
 if opcao == 2:
    agenda = input ("digita o nome:")
    numeros = int(input ("digita um telefone:"))
    
    nome.append(agenda)
    telefone.append(numeros)
#aqui eu listo os contatos
 if opcao == 1:
    for v in range(0, len(nome)):
     print("Nome:---",nome[v],":","contato:---",telefone[v])
#aqui eu listo os contatos
 if opcao == 3:
    alterar = input("qual contato voce desej alterar?")
    for n in range (0,len(nome)):
        if nome[n] == alterar:
         nome[n] = input("digite o novo nome")
         telefone[n] = int( input("digite o novo telefone"))
#aqui eu busco os contatos
 if opcao == 4:
     achado = False
     achar = input("qual contato voce deseja buscar na agenda?")
     for b in range (0,len(nome)):
         if nome[b]== achar:
             achado = True
             print(nome[b],telefone[b]) 
     if not achado:
      print("nome não encontrado")
#aqui  eu removo algum contato
 if opcao == 5:
    remover = input("qual contato você que excluir")
    for r in range (0,len(nome)):
        if nome[r] == remover:
            del nome[r]
            del telefone[r]
 

#aqui eu saio do codigo
 if opcao == 6:
    print('Obrigado por usar nossa agenda, volte sempre! :)')

 if opcao == 7:
    arquivo = open('pfv.txt', 'w')







