# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

# SP – R$67.836,43
# RJ – R$36.678,66
# MG – R$29.229,88
# ES – R$27.165,48
# Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado 
# teve dentro do valor total mensal da distribuidora.

def calculaPercentual(estado, valorTotal):
    
    return estado*100 / valorTotal
   


SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
Outros = 19849.53

valorTotal = SP+RJ+MG+ES+Outros


print("O percentual mensal de São Paulo foi: {:.2f}%".format(calculaPercentual(SP, valorTotal)))
print("O percentual mensal do Rio de Janeiro foi: {:.2f}%".format(calculaPercentual(RJ, valorTotal)))
print("O percentual mensal de Minas Gerais foi: {:.2f}%".format(calculaPercentual(MG, valorTotal)))
print("O percentual mensal do Espirito Santo foi: {:.2f}%".format(calculaPercentual(ES, valorTotal)))
print("O percentual mensal de Outros estados foi: {:.2f}%".format(calculaPercentual(Outros, valorTotal)))
