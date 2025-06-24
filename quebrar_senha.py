##Programa simula a quebra de uma senha numérica gerando tentativas aleatórias até acertar.
# Ele calcula quantas tentativas são necessárias, em média, para adivinhar a senha digitada.

from random import randint

def ttv_senha(qnt):
	return "".join([str(randint(0, 9)) for i in range(qnt)])
	
def qbr_senha(senha):
	senha = str(senha)
	ttv = 0
	qnt = len(senha)
	while True:
		if ttv_senha(qnt) == senha:
			ttv += 1
			break
		ttv += 1
	return ttv

	
while True:
	senha = int( input("Digite sua senha: "))
	resul = qbr_senha(senha)
	print(f"É necessário {resul} tentativas para quebra a senha {senha} \n")