import requests
import threading
from colorama import Fore
url = 'https://www.myplates.com/api/licenseplates/passenger/lone-star-black/'

plate = input('Enter the name of the plate')

if len(plate) > 6:
    print("Plate is too long")
    plate = input('Enter the name of the plate')
elif len(plate) == 1:
    print("Plate is empty")
    plate = input('Enter the name of the plate')

response = requests.get(url+plate).text

if(response[11:12] =='a'):
    print(Fore.GREEN + plate + "Available")
else:
    print(Fore.RED + plate + "Invalid")

