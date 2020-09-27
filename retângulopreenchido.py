"""
Recebe dois números inteiros correspondentes à largura e altura,
e devolve uma cadeia de caracteres representando um retângulo,
sendo "#" os que estão na borda e " " os que preenchem o retângulo.
"""

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

valor_total_altura = altura
valor_total_largura = largura

while altura>0: 
	if altura == 1 or altura == valor_total_altura: 
		print(largura * "#")
	else:
		largura_inicial = 1
		while largura_inicial <= largura:
			if largura_inicial == 1 or largura_inicial == largura:
				print("#", end = "")
			else:
				print(" ", end = "")
			largura_inicial = largura_inicial + 1
		print("")

	altura = altura - 1

