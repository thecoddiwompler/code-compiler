import requests
import os
from dotenv import load_dotenv

load_dotenv()


# Get API Key from environment path

api_key = os.getenv("API_KEY")


# GET language list from Online Code Compiler API using requests library

def get_language(api_key):

    url = os.getenv("LANGUAGE_LIST_URL")

    host = os.getenv("HOST")
    
    headers = {
        "X-RapidAPI-Key" : api_key,
        "X-RapidAPI-Host" : host
    }

    response = requests.get(url=url, headers=headers)

    data = response.json()

    return data


# Get the language details in JSON list and define the path to dump the language list

language_extractor = get_language(api_key)

file_path = "input/language_list.txt"


# Truncate the file_path if it exists or create a new one and Write all the Language names from language_extractor

with open(file_path, mode='w') as file:

    for language_detail in language_extractor:
        file.write(language_detail['name']+'\n')