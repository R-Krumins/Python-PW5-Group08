import urllib.request
import json
import os

clearLine = lambda: print('\033[1A\x1b[2K', end='')

def clearConsole():
    os.system('cls')
    print('{0}\n{1}\n{0}'.format('*'*60, 'GEO FINDER 3000'.center(60)))

def printTable(data):
    lenght = len(max(data.values(), key=len))+2
    if lenght < 20: lenght = 20

    print('-'*(lenght*2+3))
    for k, v in data.items():
        print('| {:<{l}}| {:<{l}}|'.format(k.replace('_', ' ').upper(), v, l=lenght-1))
        print('|{0}{1}{0}|'.format('-'*lenght,'+'))

def ask(prompt):
    while True:
        try:
            answer = float(input(prompt))
            clearConsole()
            return str(answer)        
        except:
            clearLine()
            print('Error: Invalid input!')

def requestData(url):  
    try:
        return json.loads(urllib.request.urlopen(url).read().decode())['address']
    except urllib.error.URLError:
        print('Error: unable to fetch data. Check internet connection.')
    except KeyError:
        print('Error: invalid coordinates')
    except:
        print('Error: something went horribly wrong')
    
    print('\n\nPress <Enter> to retry!')
    input()
    return None
    
def clean(data):
    data.pop('country_code')
    data.pop('postcode')
    
    for k in data.keys():
        if k.startswith('ISO'): 
            data.pop(k)
            break

    
def run():
    clearConsole()
    lat = ask('Input latitude: ')   
    lon = ask('Input longitude: ')

    url = 'https://nominatim.openstreetmap.org/reverse?lat={}&lon={}&format=json'.format(lat, lon)
    data = requestData(url)
    if data == None: return

    clean(data)
    printTable(data)
    
    print('\n\nPress <Enter> to try new coordinates')
    input()

while True:
    run()





