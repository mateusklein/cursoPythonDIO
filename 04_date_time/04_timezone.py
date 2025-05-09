#pip install pytz
from datetime import datetime, timezone, timedelta
import pytz

print("=========usando pytz============")
data = datetime.now(pytz.timezone("Europe/Oslo"))

print(data)

data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))
print(data2)

print("=============sem usar pytz==============")

data_oslo = datetime.now(timezone(timedelta(hours=2), "OSL"))
data_saopaulo = datetime.now(timezone(timedelta(hours=-3), "SP")) #O SEGUNDO ARGUMENTO É OPCIONAL E SÓ É USADO QUANDO CHAMA tzname

print(data_oslo, data_oslo.tzname())
print(data_saopaulo, data_saopaulo.tzname())
