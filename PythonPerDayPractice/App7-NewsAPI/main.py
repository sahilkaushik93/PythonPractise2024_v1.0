import requests
import time
import sys
sys.path.append('E:\Job & Interview Kit\Revision Material\DS & Algos - Python & JavaScript\PythonPractise2024\PythonPerDayPractice')
import utilities

topic = "tesla"

url = f"https://newsapi.org/v2/everything?q={topic}&from=2024-04-04&sortBy=publishedAt&apiKey=7e0e07ed88764a0f894d5bbd46f3f567&language=en"

response = requests.get(url=url)

news = response.json()

message = f"Subject: Today News related to {topic} - {time.ctime()}"

for i in news['articles']:
    message = message + "\n\nNews:\n" + str(i.get('description')) + "\n" + i.get('url')

utilities.send_email(message=message)
    

    
    
