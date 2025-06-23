from random import choice

# Simula a média de acertos ao chutar todas as alternativas de uma prova com questões de múltipla escolha (A-E),
# considerando 100 tentativas de simulação e assumindo escolhas aleatórias para resposta e gabarito.
def ops():
	return choice("abcde")

def esc_qst(qst):
	erradas = 0
	for n in range(qst):
		if ops() != ops():
			erradas += 1
	return qst - erradas

def calc_media(qst):
	resuls = []
	for i in range(100):
		resul = esc_qst(qst)
		resuls.append(resul)
	return sum(resuls) / len(resuls)

qst = int(input("Quantidade de questão: "))		
resul = calc_media(qst)
print(f"Se chutar {qst} questão, acertará {resul:.2f} questão")