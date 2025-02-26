from time import sleep
import webbrowser
import urllib.parse
import sys
import os
from pathlib import Path
import requests


def google(query):
    
    query=urllib.parse.quote_plus(query)
    webbrowser.open(f'https://www.google.com/search?q={query}')
    sleep(1)

    return

def getDorks(target):
    
    user=str(Path.home())
    if not os.path.isdir(f'{user}/.dorker'):
        os.makedirs(f'{user}/.dorker')
    
    files = os.listdir(f'{user}/.dorker')
    for file in files:
        try:
            with open(f'{user}/.dorker/{file}', 'r') as file:
                for line in file:
                    engine = line.split(' ')[0]
                    query = line[len(engine)+1:-1]
                    query = query.replace('TARGET',target)

                    match engine:

                        case "google":
                            google(query)
    
        except OSError:
            print(f"Reading {user}/.dorker/{file} failed")

    return

def main():
    
    if len(sys.argv)>1:
        getDorks(sys.argv[1])

    else:
        print('usage: dorker searchterm')

    return 0


if __name__ == "__main__":
    main()
