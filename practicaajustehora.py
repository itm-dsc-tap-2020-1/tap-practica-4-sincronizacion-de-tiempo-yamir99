import datetime
from time import ctime
import ntplib
import os
import time
#fecha y hora de la peticion
x1 = datetime.datetime.now()
print ("Fecha y hora en la que se hace la solicitud: %s" % x1)

#fehca y hora del servidor
servidor_de_tiempo = "time-e-g.nist.gov"
print("\nObteniendo la hora del servidor")
cliente_ntp = ntplib.NTPClient()
respuesta = cliente_ntp.request(servidor_de_tiempo)
hora_actual = datetime.datetime.strptime(ctime(respuesta.tx_time), "%a %b %d %H:%M:%S %Y")

#Fecha y hora de llegada de la peticion
x2 = datetime.datetime.now()
print ("Fecha y hora en la que llega la solicitud %s" % x2)

#imprimir la hora del sevidor
print("La fecha y hora del servidor es: " + str(hora_actual) )

t1 = int(x1.second)
t2 = int(x2.second)
tf =int((t2-t1)/2)
print ("El ajuste sera de: ",tf," segundos")

tajustado = int(hora_actual.second)+tf
fecha = "la nueva fecha es: "
fecha = fecha + str(hora_actual.year)+"-0"+str(hora_actual.month)+"-"+str(hora_actual.day)+" "+str(hora_actual.hour)+":"+str(hora_actual.minute)+":"+str(tajustado)
#print (x2-x1)
print (fecha)

#ajuste fecha
print("Ajustando tiempo:")
y=hora_actual.minute
fajustada=""
if y>9:
    fajustada = "0"+str(hora_actual.month)+""+str(hora_actual.day)+""+str(hora_actual.hour)+""+str(hora_actual.minute)+""+str(hora_actual.year)
else:
    fajustada = "0"+str(hora_actual.month)+""+str(hora_actual.day)+""+str(hora_actual.hour)+"0"+str(hora_actual.minute)+""+str(hora_actual.year)
#fajustada = +
os.system('date -u %s' % fajustada)
