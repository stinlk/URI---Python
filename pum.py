# Pum - 1142

qtt = int(input()) # Quantidade de linhas que vai ser imprimido.
comeco = 0 # Contagem dos numeros.
saber = 0 # Saber quantidade de vezes q foi imprimido para imprimir PUM.
lista = []
for i in range(qtt):
    comeco += 1
    saber += 1

    lista.append(comeco)
    

    if saber == 3:
        saber = 0
for i in range(len(lista)):
    
    print(lista[i],"PUM", end='')