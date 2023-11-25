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


# Compile the code by sending POST request to Online Code Compiler API

def compile_code(language_id, api_key):

    # Grab the User input from input.txt and read it.
    
    input_path = "input/input.txt"

    with open(input_path, mode='r') as file:
        user_input = file.read()

    
    # Grab the user code from code.txt file

    code_path = "input/code.txt"

    with open(code_path, mode='r') as file:
        code = file.read()


    # Grab the host and url from Environment file

    host = os.getenv("HOST")
    url = os.getenv("COMPILE_CODE_URL")


    # Define the headers for the api call

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": host
    }


    # Define the body for the api call

    payload = {
        "language": language_id,
        "version": "latest",
        "code": code,
        "input": user_input
    }


    # Hit the API to compile the code

    response = requests.post(url=url, json=payload, headers=headers)

    
    data = response.json()

    return data



# Get the language details in JSON list and get the language_id from User input of language name

language_extractor = get_language(api_key)

language_name = input("Enter your choice of language. You can refer to language_list.txt in input folder for reference :  ")

for language_detail in language_extractor:
    if language_detail['name'].lower() == language_name.lower():
        language_id = language_detail['id']
        break


# Compile the code and write the result into /bin in output.txt

output = compile_code(language_id, api_key)

with open("bin/output.txt", mode='w') as file:
    file.write(output['output'])