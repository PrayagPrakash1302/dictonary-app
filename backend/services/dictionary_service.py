import requests

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def fetch_word_data(word:str):
    response=requests.get(API_URL+word)

    if response.status_code!=200:
        return None
    
    data=response.json()[0]

    meanings = []
    synonyms = set()

    #Synonyms 
    for syn in data.get("synonyms", []):
        synonyms.add(syn)

    for meaning in data["meanings"]:
        for syn in meaning.get("synonyms", []):
            synonyms.add(syn)
        for definition in meaning["definitions"]:
            meanings.append(definition["definition"])
            for syn in definition.get("synonyms",[]):
                synonyms.add(syn)

    return {
        "word":word,
        "meanings":meanings,
        "synonyms":list(synonyms)
    }
