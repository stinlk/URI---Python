# Tempo de Jogos em Minutos - 1047 - NAO RESOLVIDO.
h_inicial, min_inicial, h_final, min_final = map(int, input().split())

total_hora = h_final - h_inicial

if total_hora < 0:
    total_hora = 24 + (h_final - h_inicial)
total_min = min_final - min_inicial

if total_min < 0:
    total_min = 60 + (min_final - min_inicial)
    total_hora -= 1

if (h_inicial == min_inicial) and (h_final == min_inicial):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

else:
    print(f"O JOGO DUROU {total_hora} HORA(S) E {total_min} MINUTO(S)")
