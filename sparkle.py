import discord
import colorama
from colorama import Fore
from colorama import Back
from colorama import Style
from pypresence import Presence
import os
import requests
import time
import random
import init
import sys
import subprocess

client = discord.Client()

def Clear():
    os.system('')
Clear()

RPC = Presence("935976521875730462")
RPC.connect()
RPC.update(state='Welcome To Our Hell', details='discord.gg/TCyGay6ADE', large_image='largerimage',small_image="smallimage",large_text="discord.gg/TCyGay6ADE",small_text="Welcome To Our Hell")

print(f"""

                                     {Fore.WHITE}██████{Fore.GREEN}╗{Fore.WHITE}██████{Fore.GREEN}╗  {Fore.WHITE}█████{Fore.GREEN}╗ {Fore.WHITE}██████{Fore.GREEN}╗ {Fore.WHITE}██{Fore.GREEN}╗  {Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╗     {Fore.WHITE}███████{Fore.GREEN}╗
                                    {Fore.WHITE}██{Fore.GREEN}╔════╝{Fore.WHITE}██{Fore.GREEN}╔══{Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╔══{Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╔══{Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}║ {Fore.WHITE}██{Fore.GREEN}╔╝{Fore.WHITE}██{Fore.GREEN}║     {Fore.WHITE}██{Fore.GREEN}╔════╝
                                    {Fore.GREEN}╚{Fore.WHITE}█████{Fore.GREEN}╗ {Fore.WHITE}██████{Fore.GREEN}╔╝{Fore.WHITE}███████{Fore.GREEN}║{Fore.WHITE}██████{Fore.GREEN}╔╝{Fore.WHITE}█████{Fore.GREEN}═╝ {Fore.WHITE}██{Fore.GREEN}║     {Fore.WHITE}█████{Fore.GREEN}╗  
                                     {Fore.GREEN}╚═══{Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╔═══╝ {Fore.WHITE}██{Fore.GREEN}╔══{Fore.WHITE}██{Fore.GREEN}║{Fore.WHITE}██{Fore.GREEN}╔══{Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}██{Fore.GREEN}╔═{Fore.WHITE}██{Fore.GREEN}╗ {Fore.WHITE}██{Fore.GREEN}║     {Fore.WHITE}██{Fore.GREEN}╔══╝  
                                    {Fore.WHITE}██████{Fore.GREEN}╔╝{Fore.WHITE}██{Fore.GREEN}║     {Fore.WHITE}██{Fore.GREEN}║  {Fore.WHITE}██{Fore.GREEN}║{Fore.WHITE}██{Fore.GREEN}║  {Fore.WHITE}██{Fore.GREEN}║{Fore.WHITE}██{Fore.GREEN}║ {Fore.GREEN}╚{Fore.WHITE}██{Fore.GREEN}╗{Fore.WHITE}███████{Fore.GREEN}╗{Fore.WHITE}███████{Fore.GREEN}╗
                                    {Fore.GREEN}╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝
""")  

token = input(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}Token{Fore.WHITE}: ")
head = {'Authorization': str(token)}
headers = {'Authorization': token, 'Content-Type': 'application/json'} 
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head) 

if src.status_code == 401:
        print(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}Token Accepted...")
        exit()
elif src.status_code == 200:
        print(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}Token Accepted...")
else:
        print(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.RED}~{Fore.WHITE}] {Fore.RED}{Style.BRIGHT}Internal Error!")
        input()
        exit()

while True:
    T = input(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}Message{Fore.WHITE}: ")
    if T=="text":
        exit(0)
    else:
        print(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}Loading Please Wait...")
        break

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send (T)
      print(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}SentMSG{Fore.WHITE}: {user.name}")
    except:
       print(f"{Fore.WHITE}{Style.BRIGHT}[{Fore.GREEN}~{Fore.WHITE}] {Fore.GREEN}{Style.BRIGHT}FailedMSG{Fore.WHITE}: {user.name}")

client.run(token, bot=False)