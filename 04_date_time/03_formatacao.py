#usa strftime e strptime
import datetime

d = datetime.datetime.now()
date_str = "29/04/2025 15:02"
mascara = "%d/%m/%Y %H:%M"

print(d.strftime(mascara))


dd = datetime.datetime.strptime(date_str, mascara)
print(dd)
