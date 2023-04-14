import random
import string
import colorama
from colorama import Fore, Style, Back
import os
import json

os.system("clear")

balance = 0

num = float(input("Amount to deposit: "))

balance += num
print(f"Balance: {balance}")

with open('balance.json', 'w') as k:
    json.dump({"balance": balance}, k)
k.close()

characters = string.ascii_letters + string.digits
blobid = ''.join(random.choices(characters, k=12))