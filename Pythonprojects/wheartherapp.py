import requests
import time

def weather(city):
       appiid = "3e6b4e9511a850c213bde4c129818267"

       url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={appiid}'
       response = requests.get(url)

       res= response.json()


       condition = res['weather'][0]['main']
       description = res['weather'][0]['description']
       temp = res['main']['temp']
       print(f"Condition:{condition}\nDescription:{description}\nTemp:{temp}")
while True:
       weather('India')
       time.sleep(5)