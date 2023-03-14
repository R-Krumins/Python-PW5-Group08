#ricards
import re
import urllib.request
from bs4 import BeautifulSoup as bs

url = 'https://www.imdb.com/title/tt6084202/'                       # Default url leads to Latvian movie 'Blizzard of Souls'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/110.0'})
html = urllib.request.urlopen(req).read()
soup = bs(html, 'html.parser')

def get_name():
    name = soup.find('h1').text.upper()
    print(f'Title: \"{name}\"\n')

def get_top_credits():
    re_top_credits = re.compile('.*principal-credits.*')            # Regex for <div> that contains 'top credits'- director, writer, stars
    div_top_credits = soup.find('div', {'class':re_top_credits})    # Finds div that contains top stars (credits in html) 
    list_top_credits = div_top_credits.find_all('li', {'data-testid':'title-pc-principal-credit'})
    for item in list_top_credits:
        item_text = item.text
        if item_text.__contains__('Director'):
            print('Director: ', end='')
        elif item_text.__contains__('Writer'):
            print('\nWriters: ', end='')
        elif item_text.__contains__('Stars'):
            print('\nStars: ', end='')
        for li in item.find_all('li'):
            print(li.find('a').text +'   ', end='')

def get_awards():
    li_awards = soup.find('li', {'data-testid':'award_information'})
    awards = li_awards.find('label').text
    print(f'\nAwards: {awards}')

def get_cast():
    re_cast = re.compile('.*title-cast__grid*.')                    # Regex for <div> that contains all cast and roles
    div_all_cast = soup.find('div', {'class':re_cast}).find_all('div', {'data-testid':'title-cast-item'}) # Finds individual <div>'s that contains top stars (credits in html)
    print('\nList of cast and their roles:\n')
    i = 1
    for item in div_all_cast:
        actor = item.find('a', {'data-testid':'title-cast-item__actor'}).text
        role = ''
        try:
            role = item.find('a', {'data-testid':'cast-item-characters-link'}).find('span').text
        except:
            print(f'  {i}. {actor}')
            i+=1
            continue
        print(f'  {i}. {role} played by {actor}')
        i+=1

def execute():
    get_name()
    get_top_credits()
    try:
        get_awards()
    except:
        print('\n! No nominations yet !')
    get_cast()

execute()