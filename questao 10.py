piloto = str(input(" Digite o nome do piloto: "))
distancia = float(input(" Digite a distância percorrida em km: "))
tempo = float(input(" Digite o tempo garto em horas: "))

velocidade_media = distancia / tempo

print(f"A velocidade mé de {piloto} foi {velocidade_media:.2f} km/h")