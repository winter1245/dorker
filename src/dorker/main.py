import argparse
import re
from time import sleep
import webbrowser
import urllib.parse
import sys
import os
from pathlib import Path
import requests

parser = argparse.ArgumentParser()
parser.add_argument("search", help="The searchterm e.g. copany name")
parser.add_argument("files", help="The pattern files in ~/.docker/ to use", nargs='*')
parser.add_argument("-v", "--verbose",action="store_true", help="more verbose logging")
args = parser.parse_args()

def google(query):
    
    query=urllib.parse.quote_plus(query)
    webbrowser.open(f'https://www.google.com/search?q={query}')
    
    if args.verbose:
        print(f'https://www.google.com/search?q={query}')
    
    sleep(1)

    return

def github(query):
    
    type= re.findall(r"type=[^ \n]+", query)
    if len(type)>0: # dont encode type
        type= '&' + type[0]
        query=urllib.parse.quote_plus(query[:-len(type)]) + type
    else:
        query=urllib.parse.quote_plus(query)
    
    webbrowser.open(f'https://github.com/search?q={query}')
    
    if args.verbose:
        print(f'https://github.com/search?q={query}')
    
    sleep(1)


def getDorks(target,userfiles):
    
    user=str(Path.home())
    if not os.path.isdir(f'{user}/.dorker'):
        os.makedirs(f'{user}/.dorker')
   
    files = os.listdir(f'{user}/.dorker')
    for file in files:
        if file in userfiles:
            try:
                with open(f'{user}/.dorker/{file}', 'r') as file:
                    for line in file:
                        engine = line.split(' ')[0]
                        query = line[len(engine)+1:-1]
                        query = query.replace('TARGET',target)

                        match engine:

                            case "google":
                                google(query)

                            case "github":
                                github(query)
    
            except OSError:
                print(f"Reading {user}/.dorker/{file} failed")

    return

def main():
    
    for i in range(len(args.files)):
        args.files[i]+='.txt'

    getDorks(args.search,args.files)


    return 0


if __name__ == "__main__":
    main()
