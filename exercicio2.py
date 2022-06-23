# // 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o 
# // próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# // escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci 
# // e  retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci(numero, guarda):
      
  guarda.append(1)
  guarda.append(0) #guardando os primeiros valores da sequencia
  guarda.append(1)

  for i in range(2, numero+1):
      guarda.append(guarda[i]+guarda[i-1])#add proximos valores

  
def estaNaSequencia(numero, guarda):#verificando se número pertence a sequência
    pertence = False;

    for item in guarda:
        if item == numero:
            pertence=True

    if pertence:
         return "O número {} PERTENCE a sequência de fibonacci".format(numero)
    else:
        return "O número {} NÃO pertence a sequência de fibonacci".format(numero)


numero = int(input())
if numero==0 or numero ==1 or numero==2:
    print("O número {} pertence a sequência de fibonacci".format(numero))
else:
    guarda=[] ##criando lista para guardar sequência

    fibonacci(numero, guarda)

    print(estaNaSequencia(numero, guarda))
    


    
    




