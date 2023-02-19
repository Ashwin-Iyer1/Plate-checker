import requests
import threading
from itertools import combinations

url = 'https://www.myplates.com/api/licenseplates/passenger/lone-star-black/'

# plate = input('Enter the name of the plate')

# if len(plate) > 6:
#     print("Plate is too long")
#     plate = input('Enter the name of the plate')
# elif len(plate) == 1:
#     print("Plate is empty")
#     plate = input('Enter the name of the plate')

# response = requests.get(url+plate).text

# if(response[11:12] =='a'):
#     print(Fore.GREEN + plate + "Available")
# else:
#     print(Fore.RED + plate + "Invalid")


chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
i = 1
res = []

for sub in range(2, 5):
    res.extend(combinations(chars, sub + 1))
def convertTuple(tup):
    str = ''
    for item in tup:
        str = str + item
    return str
def getresponse(url):
    if(url[11:12] =='a'):
        print('\033[0;32m'+convertTuple(plates) + " Available")
        with open("available-plates.txt", "a") as file1:
            file1.write(convertTuple(plates) + "\n")
    else:
        print('\033[91m'+convertTuple(plates) + " Invalid")
for plates in res:
    if(len(plates) == 1):
        response = requests.get(url+plates[0]).text
        getresponse(response)
    if(len(plates) == 2):
        response = requests.get(url+plates[0]+plates[1]).text
        getresponse(response)
    if(len(plates) == 3):
        response = requests.get(url+plates[0]+plates[1]+plates[2]).text
        getresponse(response)
    if(len(plates) == 4):
        response = requests.get(url+plates[0]+plates[1]+plates[2]+plates[3]).text
        getresponse(response)
    if(len(plates) == 5):
        response = requests.get(url+plates[0]+plates[1]+plates[2]+plates[3]+plates[4]).text
        getresponse(response)
    if(len(plates) == 6):
        response = requests.get(url+plates[0]+plates[1]+plates[2]+plates[3]+plates[4]+plates[5]).text
        getresponse(response)
