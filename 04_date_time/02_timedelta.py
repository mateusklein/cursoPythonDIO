from datetime import datetime, timedelta

tipo_carro = 'G' #P, M, G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if(tipo_carro=='P'):
    print("==========PEQUENO=============")
    print("data de entrada: ", data_atual)
    data_entrega = data_atual + timedelta(minutes=tempo_pequeno)
    print("data de saida: ", data_entrega)
elif(tipo_carro=='M'):
    print("==========MEDIO=============")
    print("data de entrada: ", data_atual)
    data_entrega = data_atual + timedelta(minutes=tempo_medio)
    print("data de saida: ", data_entrega)
else:
    print("==========GRANDE=============")
    print("data de entrada: ", data_atual)
    data_entrega = data_atual + timedelta(minutes=tempo_grande)
    print("data de saida: ", data_entrega)
