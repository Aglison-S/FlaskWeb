diario = {"fulano":8.0, "sicrano":5.0}
for chave, valor in diario.items():
	print(chave, "-", valor)
	# OU 
	print("O NOME É:{} e a NOTA É:{}".format(chave, valor))