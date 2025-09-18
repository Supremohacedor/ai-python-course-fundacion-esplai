"""
29. Escribe un archivo fecha_actual.py que muestre la fecha y hora actual en
formato dd-mm-yyyy HH:MM:SS usando datetime .
"""
import datetime

time = datetime.datetime.now()

print(time.strftime("%d-%m-%G %H:%M:%S"))