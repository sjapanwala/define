#!/usr/bin/env python3
import requests, sys, math, time

def get_raw(word):
    API = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(API)
    if response.status_code != 200:
        print(f"\033[91mERR!: \033[0mApi Did Not Respond \033[90m({response.status_code})\033[0m")
        exit()
    else:
        api_return = response.json()
        #print(api_return)
        return api_return

def construction_min(api_data):
    """
    """
    word = api_data[0]['word']
    #print(api_data[0]['phonetic'])
    if 'phonetic' not in api_data[0]:
        phonetic = '\033[90mNo Phonetic Available'
    else:
        phonetic = f"\033[35m{api_data[0]['phonetic']}"
    definitions = []
    for meaning in api_data[0]['meanings']:
        top_definitions = meaning['definitions'][:1]
        for definition in top_definitions:
            definitions.append([meaning['partOfSpeech'], definition['definition'], meaning['synonyms'], meaning['antonyms']])
    #print(top_inf)
    print(f"\n{len(word) * ' '}\033[1;95m{word.capitalize()}\n\033[0m{(len(word) + (int(len(word) / 2))) * " "}{phonetic}")
    #print(nouns)
    for definition in definitions:
        print(f'\n\033[34m{definition[0].capitalize()}\n↳ \033[97m{definition[1]}\033[0m')
        for i,synonyms in enumerate(definition[2]):
            if i < 2:
                print(f' \033[92m↳  {synonyms}\033[0m')
        for j,antonyms in enumerate(definition[3]):
            if j < 2:
                print(f' \033[91m↳  {antonyms}\033[0m')

        
def main():
    recognized_args = ['-d']
    if len(sys.argv) < 2:
        print(f"\033[91mERR!: \033[0mPlease Enter An Arg")
        exit()
    elif sys.argv[1] not in recognized_args:
        print(f"\033[91mERR!: '{sys.argv[1]}' \033[0mIs Not A Recognized Args")
    elif sys.argv[1] == '-d':
        if len(sys.argv) < 3:
            print(f"\033[91mERR!: \033[0mPlease Enter A Word To Define")
            exit()
        api_data = get_raw(sys.argv[2])
        construction_min(api_data)
    

if __name__ == "__main__":
    main()
