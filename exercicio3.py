import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

valores= []
total=0
tamanho=0

for item in dados:
    if item['valor']!=0:        #Retirando os zeros da conta
        valores.append(item['valor'])
        total+=item['valor']
        tamanho=tamanho+1

media = (total)/(tamanho)
dias=0
menor = valores[0]
maior = valores[0]

for valor in valores:
    if valor>maior:
        maior=valor
    if valor<menor:
        menor=valor
    if valor>media:
        dias=dias+1
    


print("O número de dias com faturamento em que o faturamento foi maior que a média: {} ".format(dias))
print("O menor valor ocorrido dentre os dias com faturamento: {}".format(menor))
print("O maior valor ocorrido em um dia foi: {}".format(maior))
