mensaje5 = "RT mundo RT juan el mundo"
mensaje5a = mensaje5.find("RT", 0, 2)
if mensaje5a == -1:
	print("No encontrado")
else:
	print(mensaje5a)
	