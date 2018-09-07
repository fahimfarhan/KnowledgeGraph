from datetime import date, datetime

today = date.today()
print(today)

inicio = datetime.now()
print(inicio.strftime('%d-%m-%Y'))