import datetime
import pytz

dt =  datetime.datetime.now()
dt = dt.strftime("%A %d %B %Y %H:%M")
print(dt) #Hora actual según el odenador en el que se ejecuta el comando 

print(pytz.all_timezones) #para saber el código de cualquier zona horaria. Aquí puedes buscar el código de la zona horaria que te interesa

zona_horaria_que_sea = input("Introduce la zona horaria en la que está tu preciosa novia: ")

dt_zona_horaria_que_sea = datetime.datetime.now(pytz.timezone(zona_horaria_que_sea)) 

print(dt_zona_horaria_que_sea.strftime("%A %d %B %Y %H:%M")) #hora en la parte del mundo que quieras 

