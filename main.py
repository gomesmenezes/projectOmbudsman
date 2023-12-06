ombudsman = []
option = 0

while option != 5:
  print('=========OUVIDORIA=========')
  print('1) Listar as reclamações')
  print('2) Adicionar nova reclamação')
  print('3) Remover uma reclamação')
  print('4) Pesquisar uma reclamação por código')
  print('5) Sair')

  print('==================')
  option = int(input('Digite a opção: '))
  print('==================')

  if option == 1:
    if len(ombudsman) > 0:
      for i in range(len(ombudsman)):
        print(str(i + 1) + ') ' + (ombudsman[i]))
    else:
      print('Nenhuma reclamação cadastrada no sistema!')
  
  elif option == 2:
    newReclamation = input('Fale sobre sua reclamação: ')
    ombudsman.append(newReclamation)
    length = len(ombudsman)
    print('Reclamação cadastrada com sucesso, iremos atentamente analisar sua reclamação! (CODIGO: {})'.format(len(ombudsman)))

  elif option == 3:
    for i in range(len(ombudsman)):
      print(str(i + 1) + ') ' + (ombudsman[i]))
      print('==================')
    removeCodReclamation = int(input('Digite o código da sua reclamção que deseja remover: '))
    if 0 <= removeCodReclamation <= len(ombudsman):
      ombudsman.pop(removeCodReclamation - 1)
      print('Reclamação removida com sucesso!')
    else:
      print('Código inválido')
      
  elif option == 4:
    searchReclamation = int(input('Digite o código da reclamação: '))
    if 0 <= searchReclamation <= len(ombudsman):
      successSearch = ombudsman[searchReclamation - 1]
      print(f"Elemento no índice {searchReclamation}: {successSearch}")
    else:
      print('Código inválido')