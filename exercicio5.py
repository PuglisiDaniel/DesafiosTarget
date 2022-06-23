# 5) Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou 
# pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;


# def tamanho(entrada):
#     aux=0
#     for i in entrada:
#         aux=aux+1

#     return aux

entrada = input()
invertida=''
tamanhoDaString = len(entrada)#caso possa usar len

#tamanhoDaString = tamanho(entrada) #Caso não possa usar len

for i in range(tamanhoDaString):
    invertida += entrada[tamanhoDaString-1]
    tamanhoDaString = tamanhoDaString-1
print(invertida)


