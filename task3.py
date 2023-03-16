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
            return str(answer)        
        except:
            clearLine()
            print('Error: Invalid input!')

 
def run():
    clearConsole()
    lat = ask('Input lattitude: ')
    clearConsole()
    lon = ask('Input longtitude: ')

    url = 'https://nominatim.openstreetmap.org/reverse?lat=[x]&lon=[y]&format=json'.replace('[x]', lat).replace('[y]', lon)
    clearConsole()
    
    try:
        data= json.loads(urllib.request.urlopen(url).read().decode())['address']
    except:
        print('Error: Inavlid coordinates!')
        print('\n\nPress <Enter> to retry!')
        input()
        return

    
    printTable(data)
    print('\n\nPress <Enter> to try new coordinates')
    input()

while True:
    run()





