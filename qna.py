# imports 
import requests
import dotenv
import os

# .env init
dotenv.load_dotenv()

# ask queries
def ask(que):
    url = os.getenv('QNA_URL')

    payload = '{"question":"' + que + '"}'
    headers = {
        'Authorization': 'EndpointKey ' + os.getenv('QNA_AUTH_KEY'),
        'Content-Type': 'application/json',
        'Cookie': os.getenv('QNA_COOKIE')
    }

    response = requests.request("POST", url, headers=headers, data = payload)

    return response.json()['answers'][0]['answer']

# search results
def search(que):
    url = os.getenv('QNA_URL')

    payload = '{"question":"' + que + '","top":3}'
    headers = {
        'Authorization': 'EndpointKey ' + os.getenv('QNA_AUTH_KEY'),
        'Content-Type': 'application/json',
        'Cookie': os.getenv('QNA_COOKIE')
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    
    answers = [{
        'answer': ans['answer'],
        'qid': ans['id']
    } for ans in response.json()['answers']]
    

    return answers