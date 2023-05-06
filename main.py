import requests
import fade
import os
import time
import ctypes
from colorama import Fore
from threading import Thread

text = """888b    888        d8888 888b    888 888     888  .d8888b.  
8888b   888       d88888 8888b   888 888     888 d88P  Y88b 
88888b  888      d88P888 88888b  888 888     888 888    888 
888Y88b 888     d88P 888 888Y88b 888 888     888 888        
888 Y88b888    d88P  888 888 Y88b888 888     888 888        
888  Y88888   d88P   888 888  Y88888 888     888 888    888 
888   Y8888  d8888888888 888   Y8888 Y88b. .d88P Y88b  d88P 
888    Y888 d88P     888 888    Y888  "Y88888P"   "Y8888P"

                Not a Normal Username Checker
            https://firox.cf - github.com/Firoxus
""" 
noobs = []
names = []
threadc = 10

for line in open('usernames.txt','r'):
   names.append(line.strip())

def divide(stuff):
   return [stuff[i::threadc] for i in range(threadc)]

def validate(users):
   global noobs
   for user in users:
       try:
           if (requests.get(f'https://auth.roblox.com/v1/usernames/validate?request.username={user}&request.birthday=1337-04-20').json()['code']) == 0:
               noobs.append(user)
       except Exception as e:
           print('Error:', e)
           pass
faded_text = fade.purplepink(text)
os.system('cls')
start_time = time.time()
response = requests.get('http://www.google.com')
end_time = time.time()

latency = (end_time - start_time) * 1000 # Convert to milliseconds

if latency < 15:
    stats_msg = "7 seconds per 1K usernames."
elif latency < 30:
    stats_msg = "17 seconds per 1K usernames."
elif latency < 40:
    stats_msg = "23 seconds per 1K usernames."
elif latency < 50:
    stats_msg = "27 seconds per 1K usernames."
elif latency < 100:
    stats_msg = "60 seconds per 1K usernames."
elif latency < 130:
    stats_msg = "100 seconds per 1K usernames."
elif latency < 150:
    stats_msg = "120 seconds per 1K usernames."
else:
    stats_msg = "Unknown or over 100ms latency."

latency_str = "{:.0f}".format(latency)

ctypes.windll.kernel32.SetConsoleTitleW(f"NANUC V3 | Developed by github.com/Firoxus | Current latency: {latency_str}ms | Stats with your latency: {stats_msg}")
print(faded_text)
print(f"\n{Fore.WHITE}[{Fore.MAGENTA}NANUC V3{Fore.WHITE}] Checking usernames...")
threads = []
for i in range(threadc):
   threads.append(Thread(target=validate,args=[divide(names)[i]]))
for thread in threads:
   thread.start()
for thread in threads:
   thread.join()

print(f"\n{Fore.WHITE}[{Fore.MAGENTA}NANUC V3{Fore.WHITE}] Writing valid usernames into the .txt!")
with open('valid_usernames.txt','a') as f:
   for noob in noobs:
       f.write(noob + '\n')
print(f"\n{Fore.WHITE}[{Fore.MAGENTA}NANUC V3{Fore.WHITE}] Finished. Waiting 360 seconds before exiting.")
time.sleep(360)
