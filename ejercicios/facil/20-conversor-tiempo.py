""" 
Crea una función que reciba días, horas, minutos y segundos (como enteros)
y retorne su resultado en milisegundos.
"""

def time_milliseconds_converter(days: int, hours: int, minutes: int, seconds: int):
  days_in_milliseconds = int(days) * 24 * 60 * 60 * 1000
  hours_in_milliseconds = int(hours) * 60 * 60 * 1000 
  minutes_in_milliseconds = int(minutes) * 60 * 1000 
  seconds_in_milliseconds = int(seconds) * 1000
  result_milliseconds = days_in_milliseconds + hours_in_milliseconds + minutes_in_milliseconds + seconds_in_milliseconds
  return result_milliseconds

print(time_milliseconds_converter(1,0,0,0))  # 86400000


