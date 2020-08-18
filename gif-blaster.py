import requests
from dotenv import load_dotenv
import os
import random
import time
load_dotenv()

categories = ['dog', 'cat', 'bird', 'funny']
phoneNumber = os.getenv("PHONE_NUMBER")

URL="http://api.giphy.com/v1/gifs/random"

startTime = time.time()
runTime = 25200 # 7 hours in seconds
waitTime = 1800 # 30 minutes in seconds

while (time.time() - startTime) < runTime:
    randCategory = random.randint(0, len(categories) - 1)
    PARAMS = {'api_key': os.getenv("API_KEY"), 'tag': categories[randCategory]}
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    gifLink = data["data"]["url"]

    print("Sending", categories[randCategory], "GIF:", gifLink)

    command = 'osascript sendMessage.scpt ' + phoneNumber + ' ' + gifLink

    os.system(command)
    time.sleep(waitTime)

print("Finished!")

