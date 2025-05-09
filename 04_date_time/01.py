from datetime import date, datetime, time

data = date(2025, 4, 28)

print("=========date==========")
print(data)
print("dia: ", data.day)
print("mes: ", data.month)
print("ano: ", data.year)

data_hora = datetime(2025, 4, 28, 17, 11, 10)

print("=========datetime==========")
print(data_hora)
print(data_hora.hour)
print(data_hora.minute)
print(data_hora.second)


print("=========time==========")
hour = time(17,15,0)
print(hour)
