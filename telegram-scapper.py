from telethon.sync import TelegramClient
import configparser
import csv
import os
import sys

def clear_screen():
    # Clear the terminal screen for Windows
    os.system('cls' if os.name == 'nt' else 'clear')

# Read configuration file
cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    clear_screen()
    print("[!] Run python setup.py first to configure your API credentials!")
    sys.exit(1)

# Connect to Telegram
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    clear_screen()
    client.sign_in(phone, input('Enter the code: '))

clear_screen()

# Use the provided group link
group_link_or_username = "https://t.me/HOPPY_pepe"

# Resolve the group
try:
    target_group = client.get_entity(group_link_or_username)
except Exception as e:
    print(f"[!] Error: {str(e)}")
    sys.exit(1)

print('[+] Fetching Members...')
all_participants = client.get_participants(target_group, aggressive=True)

print('[+] Saving In file...')
with open("members.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
    for user in all_participants:
        username = user.username if user.username else ""
        first_name = user.first_name if user.first_name else ""
        last_name = user.last_name if user.last_name else ""
        name = (first_name + ' ' + last_name).strip()
        writer.writerow([username, user.id, user.access_hash, name, target_group.title, target_group.id])

print('[+] Members scraped successfully.')
