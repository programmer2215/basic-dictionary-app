import requests as req
import json

print("ENTER -1 TO EXIT PROGRAM")
while True:
    search_term = input("Word: ")
    if search_term == "-1":
        break

    data = req.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{search_term}")
    data = json.loads(data.content)
    try:
        word = data[0]["word"]
        try:
            phonetic = data[0]['phonetic']
        except KeyError:
            phonetic = '¯\_(ツ)_/¯'
        print("==============")
        print(f"""
word: {word}
Phonetic: {phonetic}

Meanings:""")
        for meaning in data[0]['meanings']:
            print(meaning["partOfSpeech"] + ": ")
            for i, definition in enumerate(meaning["definitions"]):
                print(f"""
    {i + 1}) {definition["definition"]}""")
        print("==============")
    except KeyError:
        print(f":( couldn't find a definition for {search_term}")
        
print("Bye Bye!!")
