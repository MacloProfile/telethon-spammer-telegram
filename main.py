from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import os


def clear_console():
    if os.name in ('nt', 'dos'): #Check OS name for using correct command
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass


def change_title():
    if os.name in ('nt', 'dos'):
        try:
            os.system('title "Spammer Bomber"')
        except:
            pass
    else:
            pass


clear_console()
change_title()


class color : 
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'


dociteam = color.Cyan + """
                        M   a   c   l   o   '   s       t   e   a   m
"""

print(dociteam)


API_ID = int(input(color.Yellow+"[+] Enter Your API_ID : "+color.White))
API_HASH = str(input(color.Yellow+"[+] Enter Your API_HASH : "+color.White))
PHONE = str(input(color.Yellow+"[+] Enter Your Phone Number With Country Code (Ex : +12345...) : "+color.White))
COUNTER = int(input(color.Yellow+"[+] How Many Messages Do You Want To Send To One? : "+color.White))

client = TelegramClient('session', API_ID, API_HASH)
client.start()
print(color.Green+"[+] Lets Start...\n")


def get_users(path):
    users = []
    try:
        with open(path, 'r') as file:
            for line in file:
                users.append(line.strip())
    except FileNotFoundError:
        print(f"Error: File not found at path '{path}'")
    return users


def get_message(path):
    try:
        with open(path, 'r') as file:
            text = file.read()
            return text
    except FileNotFoundError:
        print(f"Error: File not found at path '{path}'")


async def main():

    if not await client.is_user_authorized():
        await client.send_code_request(PHONE)
        try:
            await client.sign_in(PHONE, input(color.Yellow+'[+] Enter the code : '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input(color.Yellow+'[+] Password : '))

    users_list = get_users("USERS.txt")
    for mess in users_list:
        message = get_message("MESSAGES.txt")
        await client.send_message(mess, message)

with client:
    client.loop.run_until_complete(main())