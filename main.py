# Pedro Henrique Serrato de Castro

#ler as linhas dos arquivos
arquivo = open("file.txt", "r")
mensagem = arquivo.readlines()

file = open("file.txt", "r")
firstline = int(file.readline())


#vetores criados
vet = []
contador = 0

#tirar as barras dos arquivos
for linha in mensagem:
    tirarBarra = linha.strip()
    vet.append(tirarBarra)

#quantidade de operacoes
if firstline == 1:
  print("Será feito ", firstline, " Operação\n")
else:
  print("Serão feitos ", firstline, " Operações\n")
  
#logicas de cada operacoes (u=uniao, i=intersecao, d=diferenca, c=produto Cartesiano)
for linha in range(len(vet)):
  if contador < firstline:
    if "U" in vet[linha] and not "," in vet[linha]:
      vetU = []
      uni1 = vet[linha + 1].split(', ')
      uni2 = vet[linha + 2].split(', ')

      for i in range(len(uni1)):
        vetU.append(uni1[i])

      for j in range(len(uni2)):
        if uni2[j] not in vetU:
          vetU.append(uni2[j])

      vet1 = ', '.join(uni1)
      vet2 = ', '.join(uni2)
      uniao = ', '.join(vetU)
      print("União: Conjunto 1 {", vet1, "}, Conjunto 2 {", vet2, "}, Resultado: {", uniao, "}")
      print("-" * 50)

      contador += 1

    elif "I" in vet[linha] and not "," in vet[linha]:
      vetI = []
      inter1 = vet[linha + 1].split(', ')
      inter2 = vet[linha + 2].split(', ')

      for i in range(len(inter1)):
        for j in range(len(inter2)):
          if inter1[i] == inter2[j] and not inter1[i] in vetI:
            vetI.append(inter1[i])

      vet1 = ', '.join(inter1)
      vet2 = ', '.join(inter2)
      intersecao = ', '.join(vetI)

      print("Interseção: Conjunto 1 {", vet1, "}, Conjunto 2 {", vet2, "}, Resultado: {", intersecao, "}")
      print("-" * 50)

      contador += 1

    elif "D" in vet[linha] and not "," in vet[linha]:
      vetD = []
      dif1 = vet[linha+1].split(', ')
      dif2 = vet[linha+2].split(', ')

      for i in range(len(dif1)):
        if dif1[i] not in dif2:
          vetD.append(dif1[i])

      vet1 = ', '.join(dif1)
      vet2 = ', '.join(dif2)
      diferenca = ', '.join(vetD)
      print("Diferença: Conjunto 1 {", vet1, "}, Conjunto 2 {", vet2, "}, Resultado: {", diferenca, "}")
      print("-" * 50)

      contador += 1

    elif "C" in vet[linha] and not "," in vet[linha]:
      cart1 = vet[linha + 1].split(', ')
      cart2 = vet[linha + 2].split(', ')

      vet1 = ', '.join(cart1)
      vet2 = ', '.join(cart2)

      print("Produto Cartesiano: conjunto 1 {", vet1, "}, conjunto 2 {", vet2, "}, Resultado:", end="") 

      for i in range(len(cart1)):
        for j in range(len(cart2)):         
          print("{", cart1[i], ",", cart2[j], "}, ", end="")

      print("\n","-" * 49)      
      contador += 1